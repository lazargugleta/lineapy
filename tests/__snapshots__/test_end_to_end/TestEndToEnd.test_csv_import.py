import datetime
from pathlib import *
from lineapy.data.types import *
from lineapy.utils import get_new_id

session = SessionContext(
    id=get_new_id(),
    environment_type=SessionType.SCRIPT,
    creation_time=datetime.datetime(1, 1, 1, 0, 0),
    working_directory="dummy_linea_repo/",
    libraries=[],
)
source_1 = SourceCode(
    id=get_new_id(),
    code="""import pandas as pd
import lineapy

df = pd.read_csv(\'tests/simple_data.csv\')
s = df[\'a\'].sum()

lineapy.linea_publish(s, "Graph With CSV Import")
""",
    location=PosixPath("[source file path]"),
)
import_2 = ImportNode(
    id=get_new_id(),
    session_id=session.id,
    source_location=SourceLocation(
        lineno=2,
        col_offset=0,
        end_lineno=2,
        end_col_offset=14,
        source_code=source_1.id,
    ),
    library=Library(
        id=get_new_id(),
        name="lineapy",
    ),
)
variable_2 = VariableNode(
    id=get_new_id(),
    session_id=session.id,
    source_location=SourceLocation(
        lineno=5,
        col_offset=0,
        end_lineno=5,
        end_col_offset=17,
        source_code=source_1.id,
    ),
    source_node_id=CallNode(
        id=get_new_id(),
        session_id=session.id,
        source_location=SourceLocation(
            lineno=5,
            col_offset=4,
            end_lineno=5,
            end_col_offset=17,
            source_code=source_1.id,
        ),
        arguments=[],
        function_id=CallNode(
            id=get_new_id(),
            session_id=session.id,
            source_location=SourceLocation(
                lineno=5,
                col_offset=4,
                end_lineno=5,
                end_col_offset=15,
                source_code=source_1.id,
            ),
            arguments=[
                ArgumentNode(
                    id=get_new_id(),
                    session_id=session.id,
                    positional_order=0,
                    value_node_id=CallNode(
                        id=get_new_id(),
                        session_id=session.id,
                        source_location=SourceLocation(
                            lineno=5,
                            col_offset=4,
                            end_lineno=5,
                            end_col_offset=11,
                            source_code=source_1.id,
                        ),
                        arguments=[
                            ArgumentNode(
                                id=get_new_id(),
                                session_id=session.id,
                                positional_order=0,
                                value_node_id=VariableNode(
                                    id=get_new_id(),
                                    session_id=session.id,
                                    source_location=SourceLocation(
                                        lineno=4,
                                        col_offset=0,
                                        end_lineno=4,
                                        end_col_offset=41,
                                        source_code=source_1.id,
                                    ),
                                    source_node_id=CallNode(
                                        id=get_new_id(),
                                        session_id=session.id,
                                        source_location=SourceLocation(
                                            lineno=4,
                                            col_offset=5,
                                            end_lineno=4,
                                            end_col_offset=41,
                                            source_code=source_1.id,
                                        ),
                                        arguments=[
                                            ArgumentNode(
                                                id=get_new_id(),
                                                session_id=session.id,
                                                positional_order=0,
                                                value_node_id=LiteralNode(
                                                    id=get_new_id(),
                                                    session_id=session.id,
                                                    source_location=SourceLocation(
                                                        lineno=4,
                                                        col_offset=17,
                                                        end_lineno=4,
                                                        end_col_offset=40,
                                                        source_code=source_1.id,
                                                    ),
                                                    value="tests/simple_data.csv",
                                                ).id,
                                            ).id
                                        ],
                                        function_id=CallNode(
                                            id=get_new_id(),
                                            session_id=session.id,
                                            source_location=SourceLocation(
                                                lineno=4,
                                                col_offset=5,
                                                end_lineno=4,
                                                end_col_offset=16,
                                                source_code=source_1.id,
                                            ),
                                            arguments=[
                                                ArgumentNode(
                                                    id=get_new_id(),
                                                    session_id=session.id,
                                                    positional_order=0,
                                                    value_node_id=ImportNode(
                                                        id=get_new_id(),
                                                        session_id=session.id,
                                                        source_location=SourceLocation(
                                                            lineno=1,
                                                            col_offset=0,
                                                            end_lineno=1,
                                                            end_col_offset=19,
                                                            source_code=source_1.id,
                                                        ),
                                                        library=Library(
                                                            id=get_new_id(),
                                                            name="pandas",
                                                        ),
                                                        alias="pd",
                                                    ).id,
                                                ).id,
                                                ArgumentNode(
                                                    id=get_new_id(),
                                                    session_id=session.id,
                                                    positional_order=1,
                                                    value_node_id=LiteralNode(
                                                        id=get_new_id(),
                                                        session_id=session.id,
                                                        value="read_csv",
                                                    ).id,
                                                ).id,
                                            ],
                                            function_id=LookupNode(
                                                id=get_new_id(),
                                                session_id=session.id,
                                                name="getattr",
                                            ).id,
                                        ).id,
                                    ).id,
                                    assigned_variable_name="df",
                                ).id,
                            ).id,
                            ArgumentNode(
                                id=get_new_id(),
                                session_id=session.id,
                                positional_order=1,
                                value_node_id=LiteralNode(
                                    id=get_new_id(),
                                    session_id=session.id,
                                    source_location=SourceLocation(
                                        lineno=5,
                                        col_offset=7,
                                        end_lineno=5,
                                        end_col_offset=10,
                                        source_code=source_1.id,
                                    ),
                                    value="a",
                                ).id,
                            ).id,
                        ],
                        function_id=LookupNode(
                            id=get_new_id(),
                            session_id=session.id,
                            name="getitem",
                        ).id,
                    ).id,
                ).id,
                ArgumentNode(
                    id=get_new_id(),
                    session_id=session.id,
                    positional_order=1,
                    value_node_id=LiteralNode(
                        id=get_new_id(),
                        session_id=session.id,
                        value="sum",
                    ).id,
                ).id,
            ],
            function_id=LookupNode(
                id=get_new_id(),
                session_id=session.id,
                name="getattr",
            ).id,
        ).id,
    ).id,
    assigned_variable_name="s",
)
