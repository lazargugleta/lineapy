import datetime
from lineapy.data.types import *
from lineapy.utils import get_new_id

session = SessionContext(
    id=get_new_id(),
    environment_type=SessionType.SCRIPT,
    creation_time=datetime.datetime(1, 1, 1, 0, 0),
    file_name="[source file path]",
    code="a = abs(11)\nb = min(a, 10)\nprint(b)\n",
    working_directory="dummy_linea_repo/",
    session_name=None,
    user_name=None,
    hardware_spec=None,
    libraries=[],
)
literal_1 = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=1,
    col_offset=8,
    end_lineno=1,
    end_col_offset=10,
    value=11,
)
literal_2 = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=2,
    col_offset=11,
    end_lineno=2,
    end_col_offset=13,
    value=10,
)
argument_1 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=None,
    col_offset=None,
    end_lineno=None,
    end_col_offset=None,
    keyword=None,
    positional_order=0,
    value_node_id=literal_1.id,
    value_literal=None,
)
argument_2 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=None,
    col_offset=None,
    end_lineno=None,
    end_col_offset=None,
    keyword=None,
    positional_order=1,
    value_node_id=literal_2.id,
    value_literal=None,
)
call_1 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=1,
    col_offset=0,
    end_lineno=1,
    end_col_offset=11,
    arguments=[argument_1.id],
    function_name="abs",
    function_module=None,
    locally_defined_function_id=None,
    assigned_variable_name="a",
    value=None,
)
argument_3 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=None,
    col_offset=None,
    end_lineno=None,
    end_col_offset=None,
    keyword=None,
    positional_order=0,
    value_node_id=call_1.id,
    value_literal=None,
)
call_2 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=2,
    col_offset=0,
    end_lineno=2,
    end_col_offset=14,
    arguments=[argument_2.id, argument_3.id],
    function_name="min",
    function_module=None,
    locally_defined_function_id=None,
    assigned_variable_name="b",
    value=None,
)
argument_4 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=None,
    col_offset=None,
    end_lineno=None,
    end_col_offset=None,
    keyword=None,
    positional_order=0,
    value_node_id=call_2.id,
    value_literal=None,
)
call_3 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=3,
    col_offset=0,
    end_lineno=3,
    end_col_offset=8,
    arguments=[argument_4.id],
    function_name="print",
    function_module=None,
    locally_defined_function_id=None,
    assigned_variable_name=None,
    value=None,
)
