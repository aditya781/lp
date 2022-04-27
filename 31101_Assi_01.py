
from collections import defaultdict

class Graph:

    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):
        # Create a set to store visited vertices
        visited = set()
        self.DFSUtil(v, visited)

    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # Create a queue for BFS
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


# Driver code

g = Graph()

edges=int(input("Please enter no of edges = "))
for i in range(0, edges, 1):
    edge1 = int(input("Please enter 1st(source) vertex = "))
    edge2 = int(input("Please enter 2nd(source) vertex = "))
    g.addEdge(edge1, edge2)
print("Following is DFS from (starting from vertex 0)")
g.DFS(0)
print("\nFollowing is BFS from (starting from vertex 0)")
g.BFS(0)

'''INPUT

    
 example :
    0 - 1 \
    | / |  2
    4 - 3 /
    
    
Please enter no of edges = 7
Please enter 1st(source) vertex = 0
Please enter 2nd(source) vertex = 1
Please enter 1st(source) vertex = 0
Please enter 2nd(source) vertex = 4
Please enter 1st(source) vertex = 1
Please enter 2nd(source) vertex = 3
Please enter 1st(source) vertex = 4
Please enter 2nd(source) vertex = 3
Please enter 1st(source) vertex = 1
Please enter 2nd(source) vertex = 4
Please enter 1st(source) vertex = 1
Please enter 2nd(source) vertex = 2
Please enter 1st(source) vertex = 3
Please enter 2nd(source) vertex = 2
Following is DFS from (starting from vertex 0)
0 1 3 2 4 
Following is BFS from (starting from vertex 0)
0 1 4 3 2 
'''