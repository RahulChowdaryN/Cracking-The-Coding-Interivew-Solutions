def search_route(self, start, end):
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