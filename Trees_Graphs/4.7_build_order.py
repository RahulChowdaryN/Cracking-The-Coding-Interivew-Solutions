class GraphNode:
    def __init__(self,data):
        self.edges = []
        self.data = data
        self.dependencies_left = 0

    def add_edge(self,node):
        self.edges.append(node)
        node.dependencies_left +=1


class Queue:

    def __init__(self):
        self.array = []

    def add(self,item):
        self.array.append(item)

    def remove(self):
        self.array.pop(0)

    def is_empty(self):
        return len(self.array) == 0

def buildorder(projects, dependencies):

    nodes = {}

    for project in projects:
        nodes[project] = GraphNode(project)

    for dependent in dependencies:
        nodes[dependent[0]].add_edge(dependent[1])


    queue = Queue()
    for project in projects:
        node = nodes[project]

        if not node.dependencies_left:
            queue.add(node)

    build_order = []

    while queue:
        node = queue.remove()
        build_order.append(node)

        for dependent in node.edges:
            dependent.dependencies_left -= 1

            if not dependent.dependencies_left:
                queue.add(dependent)

    if len(build_order) != len(projects):
        Exception("cycle detected")

    return build_order







