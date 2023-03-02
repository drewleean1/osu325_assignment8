#Name: Andrew Lee
#OSU 325
#Assignment 8
#Due date: 3/6/2023

import heapq

def solve_puzzle(Board, Source, Destination):
    '''function that takes a given board with barriers and returns the minimum path from source to destination. Uses
    similar logic to Djikstra's algorithm, storing the paths in the dictionary instance of a distance.'''
    distance = {}                                                   #dictionary to store paths to each coord
    for x in range(len(Board)):                                     #adding every coord to the dict
        for y in range(len(Board[0])):
            distance[x,y] = []

    distance[Source] = [Source]                                     #necessary to build paths in later code
    pq = [Source]                                                   #our queue to do BFS.
    visited = []                                                    #keep track of coords we visited

    while len (pq) > 0:
        current_node = heapq.heappop(pq)
        if current_node in visited:
            continue
        visited.append(current_node)
        m = current_node[0]
        n = current_node[1]
        for neighbor in [(m-1, n), (m+1, n), (m, n+1), (m, n-1)]:           #check every neighbor
            if neighbor not in distance:
                continue
            if neighbor in visited:
                continue
            if Board[neighbor[0]][neighbor[1]] == '#':                      #check for barriers
                continue
            path = distance[current_node].copy()                            #copy of the current node's path
            path.append(neighbor)                                           #add neighbor to the path
            if len(distance[neighbor]) == 0:                                #case when we first reach a node/neighbor
                distance[neighbor] = path

            elif len(path) < len(distance[neighbor]):                       #if better path to node, update
                distance[neighbor] = path

            heapq.heappush(pq, (neighbor))
    if distance[Destination] == []:                                 #check for if we can't reach destination
        return None
    return distance[Destination]
