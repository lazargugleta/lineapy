import logging
import os
import pathlib
import subprocess
import sys
import tempfile
from contextlib import redirect_stdout
from io import TextIOWrapper
from typing import Iterable, List, Optional

import click
import nbformat
import rich
import rich.syntax
import rich.tree
from nbconvert.preprocessors import ExecutePreprocessor

from lineapy.data.types import SessionType
from lineapy.db.db import RelationalLineaDB
from lineapy.db.utils import OVERRIDE_HELP_TEXT
from lineapy.exceptions.excepthook import set_custom_excepthook
from lineapy.graph_reader.apis import LineaArtifact
from lineapy.instrumentation.tracer import Tracer
from lineapy.plugins.airflow import sliced_airflow_dag
from lineapy.transformer.node_transformer import transform
from lineapy.utils.logging_config import (
    LOGGING_ENV_VARIABLE,
    configure_logging,
)
from lineapy.utils.utils import prettify

"""
We are using click because our package will likely already have a dependency on
  flask and it's fairly well-starred.
"""

logger = logging.getLogger(__name__)


@click.group()
@click.option(
    "--verbose",
    help="Print out logging for graph creation and execution",
    is_flag=True,
)
def linea_cli(verbose: bool):
    # Set the logging env variable so its passed to subprocesses, like creating a jupyter kernel
    if verbose:
        os.environ[LOGGING_ENV_VARIABLE] = "DEBUG"
    configure_logging()


@linea_cli.command()
@click.argument("file", type=click.File())
@click.argument("artifact_name")
@click.argument("artifact_value", type=str)
@click.option(
    "--visualize-slice",
    type=click.Path(dir_okay=False, path_type=pathlib.Path),
    help="Create a visualization for the sliced code, save it to this path",
)
def notebook(
    file: TextIOWrapper,
    artifact_name: str,
    artifact_value: str,
    visualize_slice: Optional[pathlib.Path],
):
    """
    Executes the notebook FILE, saves the value ARTIFACT_VALUE with name ARTIFACT_NAME, and prints the sliced code.

    For example, if your notebooks as dataframe with value `df`, then this will print the slice for it:

        lineapy notebook my_notebook.ipynb my_df df

    You can also reference side effect values, like `file_system`

        lineapy notebook my_notebook.ipynb notebook_file_system lineapy.file_system
    """
    # Create the notebook:
    notebook = nbformat.read(file, nbformat.NO_CONVERT)
    notebook["cells"].append(
        nbformat.v4.new_code_cell(
            generate_save_code(artifact_name, artifact_value, visualize_slice)
        )
    )

    # Run the notebook:
    setup_ipython_dir()
    exec_proc = ExecutePreprocessor(timeout=None)
    exec_proc.preprocess(notebook)

    # Print the slice:
    # TODO: duplicated with `get` but no context set, should rewrite eventually
    # to not duplicate
    db = RelationalLineaDB.from_environment()
    artifact = db.get_artifact_by_name(artifact_name)
    api_artifact = LineaArtifact(
        db=db,
        execution_id=artifact.execution_id,
        node_id=artifact.node_id,
        session_id=artifact.node.session_id,
        name=artifact_name,
    )
    print(api_artifact.code)


@linea_cli.command()
@click.argument(
    "path",
    type=click.Path(exists=True, dir_okay=False, path_type=pathlib.Path),
)
@click.argument("artifact_name")
@click.argument("artifact_value", type=str)
@click.option(
    "--visualize-slice",
    type=click.Path(dir_okay=False, path_type=pathlib.Path),
    help="Create a visualization for the sliced code, save it to this path",
)
def file(
    path: pathlib.Path,
    artifact_name: str,
    artifact_value: str,
    visualize_slice: Optional[pathlib.Path],
):
    """
    Executes python at PATH, saves the value ARTIFACT_VALUE with name ARTIFACT_NAME, and prints the sliced code.
    """
    # Create the code:
    code = path.read_text()
    code = code + generate_save_code(
        artifact_name, artifact_value, visualize_slice
    )

    # Run the code:
    db = RelationalLineaDB.from_environment()
    tracer = Tracer(db, SessionType.SCRIPT)
    # Redirect all stdout to stderr, so its not printed.
    with redirect_stdout(sys.stderr):

        transform(code, path, tracer)

    # Print the slice:
    artifact = db.get_artifact_by_name(artifact_name)
    api_artifact = LineaArtifact(
        db=db,
        execution_id=artifact.execution_id,
        node_id=artifact.node_id,
        session_id=artifact.node.session_id,
        name=artifact_name,
    )
    print(api_artifact.code)


def generate_save_code(
    artifact_name: str,
    artifact_value: str,
    visualize_slice: Optional[pathlib.Path],
) -> str:

    return (
        "\nimport lineapy\n"
        # Save to a new variable first, so that if artifact value is composite, the slice of creating it
        # won't include the `lineapy.save` line.
        f"linea_artifact_value = {artifact_value}\n"
        f"linea_artifact = lineapy.save(linea_artifact_value, {repr(artifact_name)})\n"
    ) + (
        f"linea_artifact.visualize({repr(str(visualize_slice.resolve()))})"
        if visualize_slice
        else ""
    )


@linea_cli.command()
@click.option("--db-url", default=None, help=OVERRIDE_HELP_TEXT)
@click.option(
    "--slice",
    default=None,
    multiple=True,  # makes 'slice' variable a tuple
    help="Print the sliced code that this artifact depends on",
)
@click.option(
    "--export-slice",
    default=None,
    multiple=True,  # makes 'export-slice' variable a tuple
    help="Requires --slice. Export the sliced code that {slice} depends on to {export_slice}.py",
)
@click.option(
    "--export-slice-to-airflow-dag",
    "--airflow",
    default=None,
    help="Requires --slice. Export the sliced code from all slices to an Airflow DAG {export-slice-to-airflow-dag}.py",
)
@click.option(
    "--airflow-task-dependencies",
    default=None,
    help="Optional flag for --airflow. Specifies tasks dependencies in Airflow format, i.e. 'p value' >> 'y' or 'p value', 'x' >> 'y'. Put slice names under single quotes.",
)
@click.option(
    "--print-source", help="Whether to print the source code", is_flag=True
)
@click.option(
    "--print-graph",
    help="Whether to print the generated graph code",
    is_flag=True,
)
@click.option(
    "--visualize",
    help="Visualize the resulting graph with Graphviz",
    is_flag=True,
)
@click.option(
    "--arg",
    "-a",
    multiple=True,
    help="Args to pass to the underlying Python script",
)
@click.argument(
    "file_name",
    type=click.Path(exists=True, dir_okay=False, path_type=pathlib.Path),
)
def python(
    file_name: pathlib.Path,
    db_url: str,
    slice: List[str],  # cast tuple into list
    export_slice: List[str],  # cast tuple into list
    export_slice_to_airflow_dag: str,
    airflow_task_dependencies: str,
    print_source: bool,
    print_graph: bool,
    visualize: bool,
    arg: Iterable[str],
):
    set_custom_excepthook()
    tree = rich.tree.Tree(f"📄 {file_name}")

    db = RelationalLineaDB.from_environment(db_url)
    code = file_name.read_text()

    if print_source:
        tree.add(
            rich.console.Group(
                "Source code", rich.syntax.Syntax(code, "python")
            )
        )

    # Set the args to those passed in
    sys.argv = [str(file_name), *arg]
    # Change the working directory to that of the script,
    # To pick up relative data paths
    os.chdir(file_name.parent)

    tracer = Tracer(db, SessionType.SCRIPT)
    transform(code, file_name, tracer)

    if visualize:
        from lineapy.visualizer import Visualizer

        Visualizer.for_public(tracer).render_pdf_file()

    if slice and not export_slice and not export_slice_to_airflow_dag:
        for _slice in slice:
            tree.add(
                rich.console.Group(
                    f"Slice of {repr(_slice)}",
                    rich.syntax.Syntax(tracer.slice(_slice), "python"),
                )
            )

    if export_slice:
        if not slice:
            print("Please specify --slice. It is required for --export-slice")
            exit(1)
        for _slice, _export_slice in zip(slice, export_slice):
            # TODO use lgcontext's slice - need an instance for this
            full_code = tracer.slice(_slice)
            pathlib.Path(f"{_export_slice}.py").write_text(full_code)

    if export_slice_to_airflow_dag:
        if not slice:
            print(
                "Please specify --slice. It is required for --export-slice-to-airflow-dag"
            )
            exit(1)

        full_code = sliced_airflow_dag(
            tracer,
            slice,
            export_slice_to_airflow_dag,
            airflow_task_dependencies,
        )
        pathlib.Path(f"{export_slice_to_airflow_dag}.py").write_text(full_code)

    tracer.db.close()
    if print_graph:
        graph_code = prettify(
            tracer.graph.print(
                include_source_location=False,
                include_id_field=False,
                include_session=False,
                include_imports=False,
            )
        )
        tree.add(
            rich.console.Group(
                "፨ Graph", rich.syntax.Syntax(graph_code, "python")
            )
        )

    console = rich.console.Console()
    console.print(tree)


@linea_cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("jupyter_args", nargs=-1, type=click.UNPROCESSED)
def jupyter(jupyter_args):
    setup_ipython_dir()
    res = subprocess.run(["jupyter", *jupyter_args])
    sys.exit(res.returncode)


@linea_cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("ipython_args", nargs=-1, type=click.UNPROCESSED)
def ipython(ipython_args):
    setup_ipython_dir()
    res = subprocess.run(["ipython", *ipython_args])
    sys.exit(res.returncode)


@linea_cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("jupytext_args", nargs=-1, type=click.UNPROCESSED)
def jupytext(jupytext_args):
    setup_ipython_dir()
    res = subprocess.run(["jupytext", *jupytext_args])
    sys.exit(res.returncode)


def setup_ipython_dir() -> None:
    """
    Set the ipython directory to include the lineapy extension by default
    """
    ipython_dir_name = tempfile.mkdtemp()
    # Make a default profile with the extension added to the ipython and kernel
    # configs
    profile_dir = pathlib.Path(ipython_dir_name) / "profile_default"
    profile_dir.mkdir()
    settings = 'c.InteractiveShellApp.extensions = ["lineapy"]'
    (profile_dir / "ipython_config.py").write_text(settings)
    (profile_dir / "ipython_kernel_config.py").write_text(settings)

    os.environ["IPYTHONDIR"] = ipython_dir_name


if __name__ == "__main__":
    linea_cli()
