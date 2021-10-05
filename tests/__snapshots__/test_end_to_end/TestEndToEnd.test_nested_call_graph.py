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
    code="a = min(abs(11), 10)",
    location=PosixPath("[source file path]"),
)
variable_1 = VariableNode(
    id=get_new_id(),
    session_id=session.id,
    source_location=SourceLocation(
        lineno=1,
        col_offset=0,
        end_lineno=1,
        end_col_offset=20,
        source_code=source_1.id,
    ),
    source_node_id=CallNode(
        id=get_new_id(),
        session_id=session.id,
        source_location=SourceLocation(
            lineno=1,
            col_offset=4,
            end_lineno=1,
            end_col_offset=20,
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
                        lineno=1,
                        col_offset=8,
                        end_lineno=1,
                        end_col_offset=15,
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
                                    lineno=1,
                                    col_offset=12,
                                    end_lineno=1,
                                    end_col_offset=14,
                                    source_code=source_1.id,
                                ),
                                value=11,
                            ).id,
                        ).id
                    ],
                    function_id=LookupNode(
                        id=get_new_id(),
                        session_id=session.id,
                        name="abs",
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
                    source_location=SourceLocation(
                        lineno=1,
                        col_offset=17,
                        end_lineno=1,
                        end_col_offset=19,
                        source_code=source_1.id,
                    ),
                    value=10,
                ).id,
            ).id,
        ],
        function_id=LookupNode(
            id=get_new_id(),
            session_id=session.id,
            name="min",
        ).id,
    ).id,
    assigned_variable_name="a",
)
