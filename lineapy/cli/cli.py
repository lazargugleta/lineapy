from lineapy.data.types import SessionType
from lineapy.utils import UserError, info_log, report_error_to_user
import click
from lineapy.transformer.transformer import ExecutionMode, Transformer

"""
We are using click because our package will likely already have a dependency on flask and it's fairly well-starred.
"""

import click


def mode_to_enum(mode: str):
    if mode == "test":
        return ExecutionMode.TEST
    if mode == "dev":
        return ExecutionMode.DEV
    if mode == "prod":
        return ExecutionMode.PROD
    raise UserError("Unsupported mode input")


@click.command()
@click.option("--mode", default="dev", help="Either `dev`, `test`, or `prod` mode")
@click.argument("file_name")
def linea_cli(mode, file_name):
    execution_mode = mode_to_enum(mode)
    transformer = Transformer()
    try:
        lines = open(file_name, "r").readlines()
        original_code = "".join(lines)
        new_code = transformer.transform(
            original_code,
            session_type=SessionType.SCRIPT,
            session_name=file_name,
            execution_mode=execution_mode,
        )
        info_log("new_code", new_code)
        exec(new_code)
    except IOError:
        report_error_to_user("Error: File does not appear to exist.")


if __name__ == "__main__":
    linea_cli()
