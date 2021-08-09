from typing import List

from lineapy.data.types import Node, NodeType, DirectedEdge, LineaID

import networkx as nx

class Graph(object):
    """
    TODO:
    - implement the getters by wrapping around networkx (see https://github.com/LineaLabs/backend-take-home/blob/main/dag.py for simple reference)
    """

    def __init__(self, nodes: List[Node], edges: List[DirectedEdge] = []):
        """
        Note:
        - edges could be none for very simple programs
        """
        self._nodes: List[Node] = nodes
        self._ids = dict((n.id, n) for n in nodes)
        self._edges: List[DirectedEdge] = edges
        self._call_tree = nx.DiGraph()
        self._call_tree.add_nodes_from([node.id for node in nodes if node.node_type != NodeType.ArgumentNode])
        self._call_tree.add_edges_from([(edge.source_node_id, edge.sink_node_id) for edge in edges])
        
    def get_parents(self, node: Node) -> List[Node]:
        return list(self._call_tree.predecessors(node))

    def get_ancestors(self, node: Node) -> List[Node]:
        return list(nx.ancestors(self._call_tree, node))

    def get_children(self, node: Node) -> List[Node]:
        return list(self._call_tree.successors(node))

    def get_descendants(self, node: Node) -> List[Node]:
        return list(nx.descendants(self._call_tree, node))

    def get_node(self, id: LineaID) -> Node:
        return self._ids[id]

    def top_sort(self) -> List[Node]:
        return list(nx.topological_sort(self._call_tree))

    def print(self):
        # TODO: improve printing (cc @dhruv)
        for n in self._nodes:
            print(n)
        for e in self._edges:
            print(e)

    def __str__(self):
        self.print()

    def __repr__(self):
        self.print()