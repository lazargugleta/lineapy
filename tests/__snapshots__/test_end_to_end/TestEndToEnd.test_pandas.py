import datetime
from lineapy.data.types import *
from lineapy.utils import get_new_id

session = SessionContext(
    id=get_new_id(),
    environment_type=SessionType.SCRIPT,
    creation_time=datetime.datetime(1, 1, 1, 0, 0),
    file_name="[source file path]",
    code="import pandas as pd\ndf = pd.DataFrame([1,2])\ndf[0].astype(str)\nassert df.size == 2\n",
    working_directory="dummy_linea_repo/",
    libraries=[
        Library(
            id=get_new_id(),
            name="pandas",
        ),
    ],
)
lookup_1 = LookupNode(
    id=get_new_id(),
    session_id=session.id,
    name="__build_list__",
)
lookup_2 = LookupNode(
    id=get_new_id(),
    session_id=session.id,
    name="getattr",
)
literal_1 = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    value="DataFrame",
)
lookup_3 = LookupNode(
    id=get_new_id(),
    session_id=session.id,
    name="str",
)
lookup_4 = LookupNode(
    id=get_new_id(),
    session_id=session.id,
    name="getattr",
)
lookup_5 = LookupNode(
    id=get_new_id(),
    session_id=session.id,
    name="getitem",
)
literal_2 = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    value="astype",
)
lookup_6 = LookupNode(
    id=get_new_id(),
    session_id=session.id,
    name="getattr",
)
literal_3 = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    value="size",
)
lookup_7 = LookupNode(
    id=get_new_id(),
    session_id=session.id,
    name="eq",
)
import_1 = ImportNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=1,
    col_offset=0,
    end_lineno=1,
    end_col_offset=19,
    library=Library(
        id=get_new_id(),
        name="pandas",
    ),
    alias="pd",
)
literal_4 = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=2,
    col_offset=19,
    end_lineno=2,
    end_col_offset=20,
    value=1,
)
literal_5 = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=2,
    col_offset=21,
    end_lineno=2,
    end_col_offset=22,
    value=2,
)
literal_6 = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=3,
    col_offset=3,
    end_lineno=3,
    end_col_offset=4,
    value=0,
)
literal_7 = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=4,
    col_offset=18,
    end_lineno=4,
    end_col_offset=19,
    value=2,
)
argument_1 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    positional_order=0,
    value_node_id=import_1.id,
)
argument_2 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    positional_order=0,
    value_node_id=literal_4.id,
)
argument_3 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    positional_order=1,
    value_node_id=literal_5.id,
)
argument_4 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    positional_order=1,
    value_node_id=literal_1.id,
)
argument_5 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    positional_order=0,
    value_node_id=lookup_3.id,
)
argument_6 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    positional_order=1,
    value_node_id=literal_6.id,
)
argument_7 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    positional_order=1,
    value_node_id=literal_2.id,
)
argument_8 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    positional_order=1,
    value_node_id=literal_3.id,
)
argument_9 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    positional_order=1,
    value_node_id=literal_7.id,
)
call_1 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=2,
    col_offset=5,
    end_lineno=2,
    end_col_offset=17,
    arguments=[argument_1.id, argument_4.id],
    function_id=lookup_2.id,
)
call_2 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=2,
    col_offset=18,
    end_lineno=2,
    end_col_offset=23,
    arguments=[argument_2.id, argument_3.id],
    function_id=lookup_1.id,
)
argument_10 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    positional_order=0,
    value_node_id=call_2.id,
)
call_3 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=2,
    col_offset=0,
    end_lineno=2,
    end_col_offset=24,
    arguments=[argument_10.id],
    function_id=call_1.id,
)
variable_1 = VariableNode(
    id=get_new_id(),
    session_id=session.id,
    source_node_id=call_3.id,
    assigned_variable_name="df",
)
argument_11 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    positional_order=0,
    value_node_id=variable_1.id,
)
argument_12 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    positional_order=0,
    value_node_id=variable_1.id,
)
call_4 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=3,
    col_offset=0,
    end_lineno=3,
    end_col_offset=5,
    arguments=[argument_11.id, argument_6.id],
    function_id=lookup_5.id,
)
call_5 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=4,
    col_offset=7,
    end_lineno=4,
    end_col_offset=14,
    arguments=[argument_12.id, argument_8.id],
    function_id=lookup_6.id,
)
argument_13 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    positional_order=0,
    value_node_id=call_4.id,
)
argument_14 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    positional_order=0,
    value_node_id=call_5.id,
)
call_6 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=3,
    col_offset=0,
    end_lineno=3,
    end_col_offset=12,
    arguments=[argument_13.id, argument_7.id],
    function_id=lookup_4.id,
)
call_7 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=4,
    col_offset=7,
    end_lineno=4,
    end_col_offset=19,
    arguments=[argument_14.id, argument_9.id],
    function_id=lookup_7.id,
)
call_8 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=3,
    col_offset=0,
    end_lineno=3,
    end_col_offset=17,
    arguments=[argument_5.id],
    function_id=call_6.id,
)
