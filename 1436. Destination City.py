from typing import List

# ===== Problem Statement =====
# You are given the array paths, where paths[i] = [cityAi, cityBi]
# means there exists a direct path going from cityAi to cityBi. Return
# the destination city, that is, the city without any path outgoing to
# another city. It is guaranteed that the graph of paths forms a line
# without any loop, therefore, there will be exactly one destination city.

class Solution:
    # . Goal: Look for the node with no outgoing edges
    # . Note that the keys of graph are source nodes
    #   and the values are destination nodes. If a
    #   destination node is not also a source node,
    #   then that is your destination city

    # Runtime: 52 ms
    # Memory: 14.1 MB
    def approach1(self, paths: List[List[str]]) -> str:
        # Set approach
        graph = {}
        for e in paths: graph[e[0]] = e[1]
        return list(set(graph.values()).difference(graph.keys()))[0]


    # Runtime: 52 ms
    # Memory: 13.6 MB
    def approach2(self, paths: List[List[str]]) -> str:
        # list comp approach:
        graph = {}
        for e in paths: graph[e[0]] = e[1]
        return [n for n in graph.values() if n not in graph.keys()][0]


    # Runtime: 52 ms
    # Memory: 13.9 MB
    def approach3(self, paths: List[List[str]]) -> str:
        # . This is a pretty good one because it takes advantage
        #   of the guarantee given by the problem (see NOTE below)
        #   and because we can potentially return early. Morever,
        #   we don't have to build a dict and call methods on that dict...
        # . Again, don't always go for list comprehensions because you
        #   might miss out on opportunities to bail out early...
        # . Hmm, despite how optimized this version looks, it still
        #   has similar runtime and memory use to the previous approaches...
        s = set(p[0] for p in paths)
        for p in paths:
            if p[1] not in s:
                return p[1]


    #destCity = approach1
    #destCity = approach2
    destCity = approach3



# NOTE:
# Guaranteed to have only one destination city,
# which means that the resulting container that
# you make in the methods up there^ will always
# have a single element that you can index
# return [n[0] for n in graph if not n[1]][0]
if __name__ == "__main__":
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    sol = Solution()
    print(sol.destCity(paths))
