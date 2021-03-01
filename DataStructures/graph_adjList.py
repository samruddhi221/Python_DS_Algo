class UndirectedGraph:
    def __init__(self):
        self.graph = {}
        self.n_nodes = 0

    def add_vertex(self, value: int) -> None:
        self.graph[value] = []
        self.n_nodes += 1

    def add_edge(self, source, destination):
        if source not in self.graph:
            self.add_vertex(source)
        if destination not in self.graph:
            self.add_vertex(destination)
        self.graph[source].append(destination)
        self.graph[destination].append(source)

    def dfs(self, vertex: int, visited: set(), temp_list: list) -> list:
        if vertex in visited:
            return temp_list

        visited.add(vertex)
        temp_list.append(vertex)
        neighbor_list = self.graph[vertex]
        for neighbor in neighbor_list:
            temp_list = self.dfs(neighbor, visited, temp_list)
        return temp_list

    def find_connected_components(self) -> int:
        connected_components = []
        visited = set()

        for i in self.graph.keys():
            if i not in visited:
                connected_components.append(self.dfs(i, visited, []))
        return connected_components



if __name__ == '__main__':
    graph1 = UndirectedGraph()
    graph1.add_vertex(10)
    graph1.add_vertex(11)
    graph1.add_vertex(12)
    graph1.add_vertex(13)
    graph1.add_vertex(15)
    graph1.add_vertex(16)
    graph1.add_vertex(17)
    graph1.add_edge(10, 11)
    graph1.add_edge(12, 11)
    graph1.add_edge(13, 12)
    graph1.add_edge(10, 14)
    graph1.add_edge(15, 17)
    graph1.add_edge(16, 15)
    graph1.add_edge(16, 18)
    graph1.add_edge(15, 18)
    connected_nodes = graph1.find_connected_components()
    print(connected_nodes)