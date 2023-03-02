
import heapq

def solve_puzzle(Board, Source, Destination):
    distance = {}                                                            #dictionary to store paths to each coord
    for x in range(len(Board)):                                 #adding every coord to the dict
        for y in range(len(Board[0])):
            distance[x,y] = []

    distance[Source] = [Source]                                   #necessary to build paths in later code
    pq = [Source]                                               #our queue to do BFS.
    visited = []                                                #keep track of coords we visited

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
            if Board[neighbor[0]][neighbor[1]] == '#':
                continue
            visited.append(current_node)
            path = distance[current_node].copy()                            #copy of the current node's path
            path.append(neighbor)                                           #add neighbor to the path
            if len(distance[neighbor]) == 0:
                distance[neighbor] = path

            elif len(path) < len(distance[neighbor]):
                distance[neighbor] = path

            heapq.heappush(pq, (neighbor))
    return distance[Destination]

Puzzle = [
 ['-', '-', '-', '-', '-'],
 ['-', '-', '#', '-', '-'],
 ['-', '-', '-', '-', '-'],
 ['#', '-', '#', '#', '-'],
 ['-', '#', '-', '-', '-']
]

print(solve_puzzle(Puzzle, (0,2), (2,2)))
print(solve_puzzle(Puzzle, (0,0), (4,4)))