from lineapy.data.graph import Graph
from lineapy.data.types import (
    LiteralNode,
    Library,
    ImportNode,
    ArgumentNode,
    CallNode,
    VariableNode,
)
from tests.util import get_new_id, get_new_session

"""
```
a = 1
b = a + 2
c = 2
d = 4
e = d + a
f = a * b * c
```

# slice on f

```
a = 1
b = a + 2
c = 2
f = a * b * c
```
"""

# including also a headless integer & variable
code = """a = 1
b = a + 2
c = 2
d = 4
e = d + a
f = a * b * c
10
e
g = e
"""

sliced_code = """a = 1
b = a + 2
c = 2

f = a * b * c
"""

operator_lib = Library(id=get_new_id(), name="operator", version="1", path="")

session = get_new_session(code, libraries=[operator_lib])

a_assign = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    assigned_variable_name="a",
    value=1,
    lineno=1,
    col_offset=0,
    end_lineno=1,
    end_col_offset=5,
)

# NOTE: this doesn't have line/col numbers because it's implicit
operator_module = ImportNode(
    id=get_new_id(), session_id=session.id, library=operator_lib,
)

a_argument_node = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    positional_order=1,
    value_node_id=a_assign.id,
    lineno=2,
    col_offset=4,
    end_lineno=2,
    end_col_offset=5,
)

argument_node_2 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    positional_order=2,
    value_literal=2,
    lineno=2,
    col_offset=8,
    end_lineno=2,
    end_col_offset=9,
)

b_assign = CallNode(
    id=get_new_id(),
    session_id=session.id,
    function_name="add",
    function_module=operator_module.id,  # built in
    assigned_variable_name="b",
    arguments=[a_argument_node.id, argument_node_2.id],
    lineno=2,
    col_offset=0,
    end_lineno=2,
    end_col_offset=9,
)

c_assign = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    assigned_variable_name="c",
    value=2,
    lineno=3,
    col_offset=0,
    end_lineno=3,
    end_col_offset=5,
)

d_assign = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    assigned_variable_name="d",
    value=4,
    lineno=4,
    col_offset=0,
    end_lineno=4,
    end_col_offset=5,
)

a_argument_node_2 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    positional_order=1,
    value_node_id=a_assign.id,
    lineno=5,
    col_offset=8,
    end_lineno=5,
    end_col_offset=9,
)

d_argument_node = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    positional_order=2,
    value_node_id=d_assign.id,
    lineno=5,
    col_offset=4,
    end_lineno=5,
    end_col_offset=5,
)

e_assign = CallNode(
    id=get_new_id(),
    session_id=session.id,
    function_name="add",
    function_module=operator_module.id,  # built in
    assigned_variable_name="e",
    arguments=[a_argument_node_2.id, d_argument_node.id],
    lineno=5,
    col_offset=0,
    end_lineno=5,
    end_col_offset=9,
)

a_argument_node_3 = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    positional_order=1,
    value_node_id=a_assign.id,
    lineno=6,
    col_offset=4,
    end_lineno=6,
    end_col_offset=5,
)

b_argument_node = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    positional_order=2,
    value_node_id=b_assign.id,
    lineno=6,
    col_offset=8,
    end_lineno=6,
    end_col_offset=9,
)

f_assign_1 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    function_name="mul",
    function_module=operator_module.id,  # built in
    assigned_variable_name="f",
    arguments=[a_argument_node_3.id, b_argument_node.id],
    lineno=6,
    col_offset=4,
    end_lineno=6,
    end_col_offset=9,
)

f_argument_node = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    positional_order=1,
    value_node_id=f_assign_1.id,
    lineno=6,
    col_offset=4,
    end_lineno=6,
    end_col_offset=9,
)

c_argument_node = ArgumentNode(
    id=get_new_id(),
    session_id=session.id,
    positional_order=2,
    value_node_id=c_assign.id,
    lineno=6,
    col_offset=12,
    end_lineno=6,
    end_col_offset=13,
)

f_assign = CallNode(
    id=get_new_id(),
    session_id=session.id,
    function_name="mul",
    function_module=operator_module.id,  # built in
    assigned_variable_name="f",
    arguments=[f_argument_node.id, c_argument_node.id],
    lineno=6,
    col_offset=0,
    end_lineno=6,
    end_col_offset=13,
)

headless_literal = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    value=1,
    lineno=7,
    col_offset=0,
    end_lineno=7,
    end_col_offset=2,
)

headless_variable = VariableNode(
    id=get_new_id(),
    session_id=session.id,
    source_variable_id=1,
    lineno=8,
    col_offset=0,
    end_lineno=8,
    end_col_offset=1,
)

variable_alias = VariableNode(
    id=get_new_id(),
    session_id=session.id,
    source_variable_id=e_assign.id,
    assigned_variable_name="g",
    lineno=9,
    col_offset=0,
    end_lineno=9,
    end_col_offset=5,
)

graph_with_messy_nodes = Graph(
    [
        a_assign,
        operator_module,
        a_argument_node,
        argument_node_2,
        b_assign,
        c_assign,
        d_assign,
        a_argument_node_2,
        d_argument_node,
        e_assign,
        a_argument_node_3,
        b_argument_node,
        f_assign_1,
        f_argument_node,
        c_argument_node,
        f_assign,
        headless_literal,
        headless_variable,
        variable_alias,
    ]
)

graph_sliced_by_var_f = Graph(
    [
        a_assign,
        operator_module,
        a_argument_node,
        argument_node_2,
        b_assign,
        c_assign,
        a_argument_node_3,
        b_argument_node,
        f_assign_1,
        f_argument_node,
        c_argument_node,
        f_assign,
    ]
)
