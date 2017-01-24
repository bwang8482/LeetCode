"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""


"""Solution:
    1. this problem can be solved by dfs
    2. using dictionary to pair node to its clone
"""

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        # Tip: using __init__ function to initiaize global variables
        self.visited = {}
        
    def cloneGraph(self, node):
        if not node: return
        if node not in self.visited:
            clone = UndirectedGraphNode(node.label)
            self.visited[node] = clone
            for neighbor in node.neighbors:
                # Error 1: remember to clone neighbor (typo)
                clone.neighbors.append(self.cloneGraph(neighbor))
            return clone
        return self.visited[node]





