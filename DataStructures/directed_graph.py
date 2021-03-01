import collections


class DirectedGraph:
    def __init__(self):
        self.graph = {}
        self.n_nodes = 0

    def add_edge(self, source, destination):
        if source not in self.graph:
            self.add_vertex(source)
        self.graph[source].append(destination)

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

    def bfs(self, start_node) -> list:
        queue = collections.deque()
        queue.append(start_node)
        visited = [False] * self.n_nodes
        parents = [-1] * self.n_nodes

        visited[start_node] = True
        while queue:
            node = queue.popleft()
            for children in self.graph[node]:
                if not visited[children]:
                    queue.append(children)
                    visited[children] = True
                    parents[children] = node

        return parents

    def reconctruct_path(self, start_node, end_node, parent_list) -> list:
        path = []
        index = end_node
        while index != -1:
            path.append(parent_list[index])
            index = path[-1]

        path.reverse()
        #check if there is a cycle
        if path[0] == start_node:
            return path
        return []

    def find_shortest_path(self, start_node: int, end_node: int) -> list:
        parents_in_path = self.bfs(start_node)
        return self.reconstruct_path(start_node, end_node, parents_in_path)


if __name__ == '__main__':
    graph1 = DirectedGraph()
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