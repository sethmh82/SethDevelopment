# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 13:58:27 2020

@author: SethHarden
"""



"""
n = number of nodes
g = adjacency list of the unweighted graph




Function bfs(start_node, end_node)
prev = solve(start_node)
return reconstructPath(start_n, end_n, run)
"""
def reconstructPath(s, e, prev):
    # setup an empty array
    path = []
    
    # loop backwards from the end node until we get to the start
    for (at = e; at != null; at = prev[at]):
        path.add(at)
    
    #since we started at the end we need to reverse the nodes
    path.reverse()
    
    # check that they are connected if s and e are connected return the path
    # this checks that the start arrived at the root index 
    if path[0] == s:
        return path
    return []


def bfs(s, e):
    prev = solve(s)
    
    return reconstructPath(s, e, prev)


def solve(s):
    q.enqueue(s)
    
    visited = [false, ..., false] #size n
    visited[s] = true
    
    prev = [null, ..., null] #size n
    while !q.isEmpty():
        node = q.dequeue()
        neighbors = g.get(node)
        
        for(next : neighbors):
            if !visited[next]:
                q.enqueue(next)
                visited[next] = true
                prev[next] = node
    return prev



print(solve(s))