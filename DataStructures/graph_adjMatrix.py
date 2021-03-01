class UndirectedGraph:
    def __init__(self, total_vertices: int):
        self.n_vertices = total_vertices
        self.graph_mat = [[0 for i in range(self.n_vertices)]
                          for j in range(self.n_vertices)]
        self.node_val_map = {}
        for

    def add_vertex(self):
        self.n_vertices += 1


    def add_edge(self, vertex1, vertex2):
        self.graph_mat[vertex1][vertex2] = 1
        self.graph_mat[vertex2][vertex1] = 1

    def dfs(self):
        pass

    def find_connected_components(self):
        pass
