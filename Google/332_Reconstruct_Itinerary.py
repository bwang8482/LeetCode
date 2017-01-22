"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
"""

"""Solution:
    1. this problem can be solved by recursion.
    2. for each airport, travers its neigbors with alphabetical order
    3. add each termination node to route.
"""


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.flights = collections.defaultdict(list)
        self.route = []
        for departure, arrival in sorted(tickets):
            # Error 3: using list to contain all target airports
            self.flights[departure].append(arrival)
        self.dfs('JFK')
        # Error 2: reverse the route from start to end
        return self.route[::-1]

    def dfs(self, airport):
        while self.flights[airport]:
            target = self.flights[airport].pop(0)
            self.dfs(target)
        # Error 1: if the airport has no target, add itself to route as termination
        self.route.append(airport)

"""Summary:
    This problem can be solved by recursion. The key idea is that the node we stucked
is the termination airport which is the last arrivaled airport so far. In this case,
we append every airport we stucked to route.
"""












