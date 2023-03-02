#Name: Andrew Lee
#OSU 325
#Assignment 8
#Due date: 3/6/2023

import heapq

def nonZeroMin(input, visited):
    '''helper function for nextValidMin. this function looks for the next valid min in the neighbors of just one node
    (input). It makes sure that the next valid min is not already visited. Returns a tuple (next valid min, weight)
    to be used by nextValidMin'''
    minimum_value = (0, float('inf'))                           #tuple (next valid min, weight)
    for x in range(len(input)):                                 #go through all neighbors of input node
        if input[x] != 0 and input[x] < minimum_value[1]:       #check weights
            temp_min = (x, input[x])
            if temp_min[0] not in visited:                      #if not already visited, we have our new min
                minimum_value = temp_min
    return minimum_value

def nextValidMin(G, visited):
    """helper function for Prims that takes graph G and the visited nodes from Prims. uses a helper function nonZeroMin.
    nextValidMin looks for the next valid min in the whole graph.
    """
    next_edge = (0, 0, float('inf'))                            #tuple (source node, destination node, weight)
    for x in visited:                                           #check through every node in visited
        temp_edge = nonZeroMin(G[x], visited)                   #call second helper
        if temp_edge[1] < next_edge[2]:                         #check weights
            next_edge = (x, temp_edge[0], temp_edge[1])
    return next_edge

def Prims(G):
    "brute force implementation of the Prims algorithm that takes a graph G and uses two helper functions, nonZeroMin
    and nextValidMin"
    result = []
    visited = [0]                                               #start with random node, 0
    while len(visited) < len(G):
        min_edge = nextValidMin(G, visited)                     #call nextValidMin to find next valid minimum edge
        result.append(min_edge)
        visited.append(min_edge[1])
    return result