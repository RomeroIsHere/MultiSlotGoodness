import logging
import YamlReader
from Players import Player
import random
from typing import Any, Iterable
import os
import time

logger=logging.getLogger(__name__)

class Graph(): 
    def __init__(self, PlayerDict:dict[str,list[str]]): 
        # Makes an Epty Adjacency Matrix of the Correct Size
        self.PlayerDict=PlayerDict
        templist=list(self.PlayerDict)
        random.shuffle(templist)
        # includes all the Vertex By Name
        self.random_order_vertex_list = templist
        self.vertices_count=len(self.random_order_vertex_list)
        self.finishedPath=list()


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
        
        if self.random_order_vertex_list[vertexB] in self.PlayerDict[self.random_order_vertex_list[vertexA]]: 
            return True
        else: 
            return False

    def hamiltonian_cycle_util(self, path:list[int], recurse_depth): 
        '''Recursive function to check Hamiltonian cycle
        Recursion stops when Recursion Depth (recurse_depth) is Equal to the number of Vertices in the Graph, then:
            Returns True if the Final vertex is adjacent to first
        '''
        # Check if You've traversed all nodes by checking Depth to the Total Number of Vertices
        if recurse_depth == self.vertices_count:
            return self.is_adjacent(path[recurse_depth-1], path[0])

        for v,name in enumerate(self.random_order_vertex_list): 
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
            logger.error("No Appropiate Path found")
            return False
        
        logger.info("Appropiate Path Found")
        self.finishedPath=path
        
        return True
def getFileName() -> str:
    return str(time.strftime("%Y%m%d-%H%M%S")) + '.yaml'
def WriteFile(HamiltonTraveler:Graph, outputdir='output'):
    if not os.path.isdir(outputdir):
        os.makedirs(outputdir)
    with open(os.path.join(outputdir,getFileName()), "a") as stream:
        stream.writelines("Generated Cycle\n")
        avgCompatibilityLenght=0
        for cur, nxt in zip (HamiltonTraveler.finishedPath, HamiltonTraveler.finishedPath [1:] + [ HamiltonTraveler.finishedPath[0]] ):
            stream.write(f"{HamiltonTraveler.random_order_vertex_list[cur]} ->  {HamiltonTraveler.random_order_vertex_list[nxt]} \n")
            ListOfCompatibility = PlayerDict[HamiltonTraveler.random_order_vertex_list[cur]].acceptable_worlds & PlayerDict[HamiltonTraveler.random_order_vertex_list[nxt]].acceptable_worlds
            stream.write(f"{str(ListOfCompatibility)}\n\n")
            avgCompatibilityLenght+=len(ListOfCompatibility)
        avgCompatibilityLenght/=len(HamiltonTraveler.finishedPath)
        logger.info(f"The Average Compatibility of This Generation is {avgCompatibilityLenght}")
        pass
if __name__ == "__main__":
    logging.basicConfig(filename='logs/main.log', encoding='utf-8', level=logging.INFO, format='[%(asctime)s]%(name)s:%(levelname)s %(message)s',  datefmt='%I:%M:%S')
    logger.info("Starting Application")
    SlotNamesAdjacencyDict=dict()
    PlayerDict=YamlReader.ParseDSGYaml()
    logger.info("Succesfully got PlayerDict")
    logger.debug("Turning PlayerDict into and Adjacency Dict")

    for Slot in PlayerDict.keys():
        SlotNamesAdjacencyDict[Slot]=PlayerDict[Slot].CompatiblePlayers
    HamiltonTraveler=Graph(SlotNamesAdjacencyDict)
    logger.info("Finding Cycle")
    if HamiltonTraveler.find_hamiltonian_cycle():
        logger.info("Found Hamiltonian Cycle")
        logger.info("Writing to file")
        WriteFile(HamiltonTraveler)
