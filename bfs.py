import collections

def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)
    
    while queue:
    
         # Dequeue a vertex from queue
         vertex = queue.popleft()
         print(str(vertex) + " ", end=" ")
         
         # If not visited, mark it as visited, and enqueue it
         for neighbour in graph[vertex]:
               if neighbour not in visited:
                      visited.add(neighbour)
                      queue.append(neighbour)
                    
if __name__ == '__main__':
    graph = {0: [2, 3 ,4], 1: [1, 3], 2: [1, 2, 4, 5, ], 3:[1, 3 ,5], 4:[3, 4, ], 5:[3, 5]}
    print("Following is Breadth First Traversal : ")
    bfs(graph, 0)
    
    
