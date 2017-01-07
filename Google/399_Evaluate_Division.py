"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0. 
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""

"""Solution:
    1. this question calculates the division with chain rule. e.g. a/c = a/b * b/c
    2. therefore, we can consider this question as graph.
    3. each value is a vertex and division is the weight of edge
    4. a/b = 2 means from vertex a to vertex b with edge a->b has weight 2.
    5. a/d = a/b * b/c * c/d => pick b, a/c = a/b * b/c; pick c, a/d = a/c * c/d
    6. every pair of two nodes will be traversed
"""

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # Tip: declare dictionary with dictionary as elements
        graph = collections.defaultdict(dict)
        for (start, end), weight in zip(equations, values):
            graph[start][start] = graph[end][end] = 1.0
            graph[start][end] = weight
            graph[end][start] = 1.0/weight
        # Tip: using middle vertex as outerloop
        for mid in graph:
            for start in graph[mid]:
                for end in graph[mid]:
                    graph[start][end] = graph[start][mid] * graph[mid][end]
        # for each (start, end) pair in queries, get weight in graph[start][end]
        # if start isn't connected to end, return -1
        return [graph[start].get(end,-1.0) for (start, end) in queries]











