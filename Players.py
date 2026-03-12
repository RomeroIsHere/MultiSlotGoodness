import random
class Player:
    '''An Archipelago Player, representing a Singular Slot in the Archipelago

    To have more than 1 Single-Slot, submit player twice

    keep in mind, for every player, there will be 2 slots created
    '''
    def __init__(self,player_name):
        # Given Slot Name of the Player
        self.name=player_name
        # Worlds that they Can play
        # Currently random For Dev Purposes
        self.acceptable_worlds={""}
        #TODO add a way to initialize this from a File or Something
    def printWorlds(self):
        print(self.name,self.acceptable_worlds)


if __name__ == "__main__":
    testing_var_global_world=['alpha','beta','charlie','delta']
    testing_names=['alice','bob','cassandra','daryl','esther','frank']
    playerList=[]
    for slot in testing_names:
        currentPlayer=Player(slot)
        # for x in range(random.randrange(len(testing_var_global_world))):
        currentPlayer.acceptable_worlds=set(random.choices(testing_var_global_world,k=3)) 
        # has a Chance to pick the same twice, but since it turns into set it does not  duplicate the World name
        playerList.append(currentPlayer)
    for player in playerList:
        player.printWorlds()
