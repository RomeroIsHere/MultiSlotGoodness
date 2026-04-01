from __future__ import annotations
import random
GLOBAL_GAME_VARIETY_COUNT=1
class Player:
    '''An Archipelago Player, representing a Singular Slot in the Archipelago

    To have more than 1 Single-Slot, submit player twice

    keep in mind, for every player, there will be 2 slots created
    '''
    def __init__(self,player_name, index):
        # Given Slot Name of the Player
        self.name=player_name
        self.id=index
        # Worlds that they Can play
        # Currently random For Dev Purposes
        self.acceptable_worlds=set()
        # Once Done Parsing, needs to track which Players it's compatible with
        self.CompatiblePlayers=set()
        self.CompatiblePlayersScoreKeeper=dict()
        self.HasBeenVisited=False
        self.DegreeOf=-1
    def __str__(self) -> str:
        return self.name
    def __repr__(self) -> str:
        return self.__str__()
    def printWorlds(self):
        print(self.name,self.id,self.acceptable_worlds)
    def printCompatible(self):
        print(self.name,self.id,self.CompatiblePlayers)
        
    def AddIfCompatible(self, Other:Player):
        if(len(list(Other.acceptable_worlds&self.acceptable_worlds))>0):
            self.CompatiblePlayers.add(Other.name)
            return True
        else:
            return False
    def AddToCompatible(self, Other:Player):
        if Other.name in self.CompatiblePlayersScoreKeeper:
            self.CompatiblePlayersScoreKeeper[Other.name]+=1
        else:
            self.CompatiblePlayersScoreKeeper[Other.name]=1
        if self.CompatiblePlayersScoreKeeper[Other.name] >= GLOBAL_GAME_VARIETY_COUNT:
            self.CompatiblePlayers.add(Other.name)
    def RemoveCompatible(self, Other:Player):
        self.CompatiblePlayers.discard(Other.name)
    def is_adjacent(self, Other:Player):
        return Other in self.CompatiblePlayers
def UpdateGlobalVarietyCount(VarietyScore= 0):
    global GLOBAL_GAME_VARIETY_COUNT
    GLOBAL_GAME_VARIETY_COUNT = VarietyScore
    pass
if __name__ == "__main__":
    testing_var_global_world=['alpha','beta','charlie','delta']
    testing_names=['alice','bob','cassandra','daryl','esther','frank']
    playerList=[]
    for id, slot in enumerate(testing_names):
        currentPlayer=Player(slot,id)
        # for x in range(random.randrange(len(testing_var_global_world))):
        currentPlayer.acceptable_worlds=set(random.choices(testing_var_global_world,k=3)) 
        # has a Chance to pick the same twice, but since it turns into set it does not  duplicate the World name
        playerList.append(currentPlayer)
    for player in playerList:
        player.printWorlds()
        print(player)
