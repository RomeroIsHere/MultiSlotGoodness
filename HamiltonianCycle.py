class Graph(): 
    def __init__(self, vertices:int): 
        # Makes an Epty Adjacency Matrix of the Correct Size
        self.adjacency_matrix = [[0 for column in range(vertices)]
                                    for row in range(vertices)] 
        self.vertices_count = vertices 

    def is_safe_to_add(self, v, pos, path): 
        if self.adjacency_matrix[path[pos-1]][v] == 0: 
            return False

        for vertex in path: 
            if vertex == v: 
                return False

        return True

    def hamiltonian_cycle_util(self, path, pos): 
        if pos == self.vertices_count: 
            if self.adjacency_matrix[path[pos-1]][path[0]] == 1: 
                return True
            else: 
                return False

        for v in range(1, self.vertices_count): 
            if self.is_safe_to_add(v, pos, path): 
                path[pos] = v 

                if self.hamiltonian_cycle_util(path, pos+1): 
                    return True

                path[pos] = -1

        return False

    def find_hamiltonian_cycle(self):
        # Makes a List representing the path (Exactly the Size of the Number of Vertices)
        path = [-1] * self.vertices_count 
        # Arbitraly Start it at 0 (The cycle can Start Anywhere because it is a Cycle, so the Starting Point is Irrelevant in the Cycle case)
        path[0] = 0

        if not self.hamiltonian_cycle_util(path, 1): 
            print ("No\n")
            return False

        self.print_solution(path) 
        return True

    def print_solution(self, path): 
        print ("Yes\n")
        for vertex in path: 
            print (vertex )

# Example Graphs
g1 = Graph(5) 
g1.adjacency_matrix = [ [0, 1, 0, 1, 0], 
                        [1, 0, 1, 1, 1], 
                        [0, 1, 0, 0, 1],
                        [1, 1, 0, 0, 1], 
                        [0, 1, 1, 1, 0]]

g1.find_hamiltonian_cycle()