from Main import Graph
import YamlReader
def mainTest():
    SlotNamesAdjacencyDict=dict()
    PlayerDict=YamlReader.ParseDSGYaml()
    for Slot in PlayerDict.keys():
        SlotNamesAdjacencyDict[Slot]=PlayerDict[Slot].CompatiblePlayers
    AvgCumulativeCompatibility=0
    iterationsCount=30
    for iteration in range(iterationsCount):
        HamiltonTraveler=Graph(SlotNamesAdjacencyDict)
        HamiltonTraveler.find_hamiltonian_cycle()
        CumulativeCompatibilityForIteration=0
        for cur, nxt in zip (HamiltonTraveler.finishedPath, HamiltonTraveler.finishedPath [1:] + [ HamiltonTraveler.finishedPath[0]] ):
            ListOfCompatibility = PlayerDict[HamiltonTraveler.random_order_vertex_list[cur]].acceptable_worlds & PlayerDict[HamiltonTraveler.random_order_vertex_list[nxt]].acceptable_worlds
            CumulativeCompatibilityForIteration+=len(ListOfCompatibility)
        AvgCumulativeCompatibility+=CumulativeCompatibilityForIteration/len(HamiltonTraveler.finishedPath)
        print(f"Average Compatibility for iteration #{iteration}:{CumulativeCompatibilityForIteration/len(HamiltonTraveler.finishedPath)}")
    print(f"Average of {iterationsCount} Generations:{AvgCumulativeCompatibility/iterationsCount}")



if __name__ == "__main__":
    SlotNamesAdjacencyDict=dict()
    PlayerDict=YamlReader.ParseDSGYaml()
    for Slot in PlayerDict.keys():
        SlotNamesAdjacencyDict[Slot]=PlayerDict[Slot].CompatiblePlayers
    AvgCumulativeCompatibility=0
    iterationsCount=0
    try:
        while True:
            HamiltonTraveler=Graph(SlotNamesAdjacencyDict)
            HamiltonTraveler.find_hamiltonian_cycle()
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