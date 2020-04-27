class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbors(self,nbr,weight):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def getId(self):
        return self.id

    def __str__(self):
        return str(self.id) + 'connectedTo: ' + str([x.id for x in self.connectedTo])


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        new_vertex = Vertex(key)
        self.numVertices += 1
        self.vertList[key] = new_vertex

        return new_vertex

    def addEdge(self,fr,to,weight = 0):
        if fr not in self.vertList:
            new_vertex_fr = Vertex(fr)
            self.vertList[fr] = new_vertex_fr
        if to not in self.vertList:
            new_vertex_to = Vertex(to)
            self.vertList[to] = new_vertex_to

        self.vertList[fr].addNeighbors(self.vertList[to],weight)

    def getVertices(self):
        return self.vertList.keys()

    def getVertex(self,key):
        if key in self.vertList:
            return self.vertList[key]
        return None

    def getGraph(self):
        graph = {}
        for vert in self.vertList:
            graph[vert] = [x.getId() for x in self.vertList[vert].getConnections()]
        return graph

    def __contains__(self, item):
        return item in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())


    def search_route(self,start,end):

        visited = [start]
        explored = []
        graph = self.getGraph()

        while visited:
            node = visited.pop(0)
            if node not in explored:
                if node == end:
                    return True
                visited += graph[node]
                explored += [node]

        return False

    def find_all_paths(self,start):

        pass

    def shortest_path(self,start,end):

        pass

    def bfs(self,start):

        visited = [start]
        explored = []
        graph = self.getGraph()

        while visited:
            node = visited.pop(0)
            if node not in explored:
                visited += graph[node]
                explored += [node]

        return explored

    def bfs_iter(self,start):

        visited = [start]
        explored = []
        graph = self.getGraph()

        while visited:
            node = visited.pop(0)
            for nbr in graph[node]:
                if nbr not in explored:
                    visited.append(nbr)
            explored.append(node)

        return explored




    def dfs(self,start):
        visited = [start]

        explored = []
        graph = self.getGraph()

        while visited:
            node = visited.pop()
            if node not in explored:
                visited += graph[node]
                explored += [node]

        return explored

    def dfs_recursive(self,start,visited = []):
        graph = self.getGraph()

        visited += [start]

        for node in graph[start]:
            if not node in visited:
                visited = self.dfs_recursive(node,visited)
                
        return visited

    def dfs_iter(self,start,explored=[]):
        visited = [start]
        graph = self.getGraph()
        while visited:
            node = visited.pop()
            if node not in explored:
                explored += [node]
                visited += graph[node]
        return explored

    def getShortestPath(self,src):

        graph = self.getGraph()
        parent = {src:None}
        distance = {src:0}
        visited = [src]
        explored =[src]

        while visited:
            current = visited.pop(0)

            for dest in graph[current]:
                if dest not in explored:
                    explored += [dest]
                    visited += [dest]
                    parent[dest] = current
                    distance[dest] = distance[current] + 1
        return (parent,distance)

    def  all_paths_dfs(self,start,end,visited = [],path = [],full_path=[]):

        graph = self.getGraph()
        visited += [start]
        path += [start]

        if start == end:
            full_path.append({"path": list(path)})

        for node in graph[start]:

            if not node in visited:
                self.all_paths_dfs(node, end, visited, path, full_path)

        path.pop()
        visited.pop()

        if not path:
            return full_path












    #

g = Graph()

for i in range(6):
    g.addVertex(i)

#print(g.vertList)

g.addEdge(0, 1, 5)
g.addEdge(0, 5, 2)
g.addEdge(1, 2, 4)
g.addEdge(2, 3, 9)
g.addEdge(3, 4, 7)
g.addEdge(3, 5, 3)
g.addEdge(4, 0, 8)
g.addEdge(5, 4, 8)
g.addEdge(5, 2, 1)
g.addEdge(3,6,3)
g.addEdge(6,5,9)

print("graph",g.getGraph())
for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))


print("dfs recursive")
print(g.dfs_recursive(1))
print("dfs")
print(g.dfs(1))
print("bfs")
print(g.search_route(0,0))
print(g.dfs_iter(1))
print(g.bfs_iter(1))
# dfs - iter and recursive

# bfs - iter

#shortest path, all paths using dfs and bfs

print("graph",g.getGraph())
parent, distance =g.getShortestPath(0)
print(parent)
print(distance)
for i in parent:
    print("distance from {} to {} is {}".format(0,i,distance[i]), end = " ")
    print("path",end = " ")
    while parent[i] is not None:
        print(i, end = ' ')
        i= parent[i]
    print(0)


print(g.all_paths_dfs(0,5))