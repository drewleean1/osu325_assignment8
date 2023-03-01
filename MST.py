#Name: Andrew Lee
#OSU 325
#Assignment 8
#Due date: 3/6/2023

import heapq

def nonZeroMin(input, visited):
    minimum_value = (0, float('inf'))
    for x in range(len(input)):
        if input[x] != 0 and input[x] < minimum_value[1]:
            temp_min = (x, input[x])
            if temp_min[0] not in visited:
                minimum_value = temp_min
    return minimum_value

def nextValidMin(G, visited):
    next_edge = (0, 0, float('inf'))
    for x in visited:
        temp_edge = nonZeroMin(G[x], visited)
        if temp_edge[1] < next_edge[2]:
            next_edge = (x, temp_edge[0], temp_edge[1])
    return next_edge

def Prims(G):
    result = []
    visited = [0]
    while len(visited) < len(G):
        min_edge = nextValidMin(G, visited)
        result.append(min_edge)
        visited.append(min_edge[1])
    return result




input = [
 [0, 8, 5, 0, 0, 0, 0],
 [8, 0, 10, 2, 18, 0, 0],
 [5, 10, 0, 3, 0, 16, 0],
 [0, 2, 3, 0, 12, 30, 14],
 [0, 18, 0, 12, 0, 0, 4],
 [0, 0, 16, 30, 0, 0, 26],
 [0, 0, 0, 14, 4, 26, 0]
]

#print(Prims(input))