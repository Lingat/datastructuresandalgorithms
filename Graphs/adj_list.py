MAX = 1000
class Graph:
    def __init__(self):
        self.nodes = [[]]*MAX
    
    def DFSutil(self, v, visited): 
        visited.add(v)
        print(v, end=' ')
        for n in self.nodes[v]:
            if n not in visited:
                self.DFSutil(n, visited)

    def dfs(self, v):
        visited = set()
        self.DFSutil(v, visited)

    def addEdge(self, u, v):
        self.nodes[u].append(v)



# Create a graph given
# in the above diagram
g = Graph()
g.addEdge(1, 0)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print("Following is DFS from (starting from vertex 2)")
g.dfs(2)