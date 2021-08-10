from uuid import UUID
from datetime import datetime
from enum import Enum
from typing import Any, Tuple, Optional, List

from pydantic import BaseModel

# aliasing the ID type in case we chnage it later
LineaID = UUID

# TODO: not sure if this is the most intuitive name.
class StateScope:
    """
    TODO
    This captures the scope
    """

    pass


class SessionType(Enum):
    JUPYTER = 1
    SCRIPT = 2


class HardwareSpec(BaseModel):
    # TODO: information about the machine the code is run on.
    pass


class Library(BaseModel):
    name: str
    version: str
    path: str


class SessionContext(BaseModel):
    uuid: LineaID  # populated on creation by uuid.uuid4()
    environment_type: SessionType
    creation_time: datetime
    file_name: str  # making file name required since every thing runs from some file
    session_name: Optional[
        str
    ]  # obtained from name in with tracking(session_name=...):
    user_name: Optional[str] = None
    hardware_spec: Optional[HardwareSpec] = None
    libraries: Optional[List[Library]] = None


class NodeContext(BaseModel):
    lines: Tuple[int, int]
    columns: Tuple[int, int]
    execution_time: datetime
    cell_id: Optional[str] = None  # only applicable to Jupyter sessions


# NodeValue = TypeVar("NodeValue")
# NodeValue = NewType('NodeValue', Optional[Any])
NodeValue = Any
# Yifan note: something weird here about optional and NewType... https://github.com/python/mypy/issues/4580; tried to use TypeVar but also kinda weird. Seems hairy https://stackoverflow.com/questions/59360567/define-a-custom-type-that-behaves-like-typing-any


class NodeType(Enum):
    Node = 1
    ArgumentNode = 2
    CallNode = 3
    LiteralAssignNode = 4
    FunctionNode = 5
    ConditionNode = 6
    LoopNode = 7
    WithNode = 8
    ImportNode = 9


class Node(BaseModel):
    id: LineaID  # populated on creation by uuid.uuid4()
    session_id: LineaID  # refers to SessionContext.uuid
    node_type: NodeType = NodeType.Node
    code: str
    context: Optional[NodeContext] = None


class ImportNode(Node):
    node_type: NodeType = NodeType.ImportNode
    library: Library
    alias: Optional[str] = None


class ArgumentNode(Node):
    node_type: NodeType = NodeType.ArgumentNode
    keyword: Optional[str]
    positional_order: Optional[int]
    value_node_id: Optional[LineaID]
    value_literal: Optional[Any]
    value_pickled: Optional[str]


class CallNode(Node):
    node_type: NodeType = NodeType.CallNode
    arguments: List[ArgumentNode]
    function_name: str
    function_module: Optional[str]
    assigned_variable_name: Optional[str]
    value: Optional[NodeValue] = None  # value of the result


class LiteralAssignNode(Node):
    node_type: NodeType = NodeType.LiteralAssignNode
    assigned_variable_name: str
    value: Optional[NodeValue]  # gets filled at run time


class FunctionDefinitionNode(Node):
    node_type: NodeType = NodeType.FunctionNode
    function_name: str
    # TODO: should we track if its an recursive function?


class ConditionNode(Node):
    node_type: NodeType = NodeType.ConditionNode
    # TODO


class StateChangeNode(Node):
    """
    This type of node is to capture the state changes caused by "black boxes" such as loops.
    Later code need to reference the NEW id now modified.
    """

    variable_name: str
    pass


class LoopEnterNode(Node):
    """
    We do not care about the intermeidate states, but rather just what state has changed. It's conceptually similar to representing loops in a more functional way (such as map and reduce).  We do this by treating the LoopNode as a node similar to "CallNode".
    """

    node_type: NodeType = NodeType.LoopNode
    code: str
    # keeping a list of state_change_nodes that we probably have to re-construct from the sql db.
    state_change_nodes: List[StateChangeNode]
    # TODO


# Not sure if we need the exit node, commenting out for now
# class LoopExitNode(Node):
#     node_type: NodeType = NodeType.LoopNode
#     pass


class WithNode(Node):
    node_type: NodeType = NodeType.WithNode
    # TODO


class DirectedEdge(BaseModel):
    """
    When we have `a = foo(), b = bar(a)`, should the edge be between bar and foo, with foo being the source, and bar being the sink.
    Yifan note: @dorx please review if this is what you had in mind
    """

    source_node_id: LineaID  # refers to Node.uuid
    sink_node_id: LineaID  # refers to Node.uuid
