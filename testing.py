class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.adj_list:
            self.adj_list[vertex_id] = []

    def add_edge(self, from_id, to_id):
        if from_id in self.adj_list and to_id in self.adj_list:
            if to_id not in self.adj_list[from_id]:
                self.adj_list[from_id].append(to_id)

    def list_outgoing(self, user_id):
        return self.adj_list.get(user_id, [])

    def list_followers(self, target_id):
        return [uid for uid, following in self.adj_list.items() if target_id in following]

    class Graph:
        def __init__(self):
            self.adj_list = {}

        def add_vertex(self, vertex_id):
            if vertex_id not in self.adj_list:
                self.adj_list[vertex_id] = []

        def add_edge(self, from_id, to_id):
            if from_id in self.adj_list and to_id in self.adj_list:
                if to_id not in self.adj_list[from_id]:
                    self.adj_list[from_id].append(to_id)

        def list_outgoing(self, user_id):
            return self.adj_list.get(user_id, [])

        def list_followers(self, target_id):
            return [uid for uid, following in self.adj_list.items() if target_id in following]



