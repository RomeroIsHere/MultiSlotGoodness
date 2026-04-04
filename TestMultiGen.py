from Models import Graph
from DSGFileHandler import YamlFilesHandling
def mainTest(iterationMax=1000):
    SlotNamesAdjacencyDict=dict()
    PlayerDict=YamlFilesHandling.ParseDSGYaml()
    for Slot in PlayerDict.keys():
        SlotNamesAdjacencyDict[Slot]=PlayerDict[Slot].CompatiblePlayers
    AvgCumulativeCompatibility=0
    iterationsCount=0
    try:
        while iterationsCount<iterationMax:
            HamiltonTraveler=Graph(SlotNamesAdjacencyDict)
            if(HamiltonTraveler.find_hamiltonian_cycle()):
                CumulativeCompatibilityForIteration=0
                for cur, nxt in zip (HamiltonTraveler.finishedPath, HamiltonTraveler.finishedPath [1:] + [ HamiltonTraveler.finishedPath[0]] ):
                    ListOfCompatibility = PlayerDict[HamiltonTraveler.random_order_vertex_list[cur]].acceptable_worlds & PlayerDict[HamiltonTraveler.random_order_vertex_list[nxt]].acceptable_worlds
                    CumulativeCompatibilityForIteration+=len(ListOfCompatibility)
                AvgCumulativeCompatibility+=CumulativeCompatibilityForIteration/len(HamiltonTraveler.finishedPath)
                print(f"Average Compatibility for iteration #{iterationsCount}:{CumulativeCompatibilityForIteration/len(HamiltonTraveler.finishedPath)}")
                iterationsCount+=1
            pass
            
    except KeyboardInterrupt:
        pass
    if iterationsCount:
        print(f"Average of {iterationsCount} Generations:{AvgCumulativeCompatibility/iterationsCount}")
    else:
        print("Found Nothing")



if __name__ == "__main__":
    mainTest()