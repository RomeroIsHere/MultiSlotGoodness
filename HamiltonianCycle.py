# Imports
from typing import Any, Iterable
# because i want Type hints
import random
# So that i's not Always the same
class Graph(): 
    def __init__(self, vertices:int): 
        # Makes an Epty Adjacency Matrix of the Correct Size
        self.adjacency_matrix = [[0 for column in range(vertices)]
                                    for row in range(vertices)] 
        self.vertices_count = vertices
        templist=list(range(1, self.vertices_count))
        random.shuffle(templist)
        self.random_vertex = templist


    def is_safe_to_add(self, path, pos, candidateVertex): 
        '''Check if the Candidate Vertex is a valid Vertex to add to the path
        
        a) The candidate vertex is adjacent to the latest path vertex
        
        and 

        b) The candidate Vertex is not included in the Path Taken to get here
        '''
        if not self.is_adjacent(path[pos-1], candidateVertex):
            return False

        for vertex in path: 
            if vertex == candidateVertex: 
                return False

        return True
    
    def is_adjacent(self, vertexA:int, vertexB:int):
        '''Checks if 2 Nodes are Adjacent, using the Adjacency Matrix
        
        This check is Directional, Meaning that It returns true so long as Vertex A can go to Vertex B, but the Reverse is not Necessarily true
        '''
        if self.adjacency_matrix[vertexA][vertexB] == 1: 
            return True
        else: 
            return False

    def hamiltonian_cycle_util(self, path, recurse_depth): 
        '''Recursive function to check Hamiltonian cycle
        Recursion stops when Recursion Depth (recurse_depth) is Equal to the number of Vertices in the Graph, then:
            Returns True if the Final vertex is adjacent to first
        '''
        # Check if You've traversed all nodes by checking Depth to the Total Number of Vertices
        if recurse_depth == self.vertices_count:
            return self.is_adjacent(path[recurse_depth-1], path[0])

        for v in self.random_vertex: 
            if self.is_safe_to_add(path, recurse_depth, v): 

                path[recurse_depth] = v 

                if self.hamiltonian_cycle_util(path, recurse_depth+1): 
                    # if this path found a valid Cycle, shortcircuit and don't check any more configurations
                    return True
                # if it did not, means that the path we have so far is Wrong, and we must go back to a Previous step to continue Searching

                # Reset the Vertex added at this step
                path[recurse_depth] = -1
        # if the search never Short circuits, then there must be no Path that Satisfies the 
        return False

    def find_hamiltonian_cycle(self):
        '''Brute Forces a Hamiltonian Cycle of the Graph using Backtracking'''
        # Makes a List representing the path (Exactly the Size of the Number of Vertices)
        path = [-1] * self.vertices_count 
        # Arbitraly Start it at 0 (The cycle can Start Anywhere because it is a Cycle, so the Starting Point is Irrelevant in the Cycle case)
        path[0] = 0
        
        if not self.hamiltonian_cycle_util(path, 1): 
            print ("No\n")
            return False
        
        print ("Yes\n")
        self.print_solution(path) 
        return True

    def print_solution(self, path:Iterable[Any]):
        '''Arbitrarily prints the elements of an iterable(list, set, tuple, etc...)'''
        for vertex in path: 
            print (vertex )

# Example Graphs
g1 = Graph(5) 
g1.adjacency_matrix = [ [0, 1, 1, 1, 1], 
                        [1, 0, 1, 1, 1], 
                        [1, 1, 0, 1, 1],
                        [1, 1, 1, 0, 1],
                        [1, 1, 1, 1, 0]]

g1.find_hamiltonian_cycle()