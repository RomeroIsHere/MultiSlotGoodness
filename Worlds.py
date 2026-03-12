import random
class World:
    '''A World, Storing the Information

    To have more than 1 Single-Slot, submit player twice

    keep in mind, for every player, there will be 2 slots created
    '''
    def __init__(self,player_name):
        # Given Slot Name of the Player
        self.name=player_name
        # Worlds that they Can play
        # Currently random For Dev Purposes
        self.players={""}
        #TODO add a way to initialize this from a File or Something
    def printWorlds(self):
        print(self.name,self.players)

# test Gen for Random Players inside each world
if __name__ == "__main__":
    testing_var_global_world=['alpha','beta','charlie','delta']
    testing_names=['alice','bob','cassandra','daryl','esther','frank']
    WorldList=[]
    for world in testing_var_global_world:
        currentWorld=World(world)
        # for x in range(random.randrange(len(testing_names))):
        currentWorld.players=set(random.choices(testing_names,k=3)) 
        # has a Chance to pick the same twice, but since it turns into set it does not  duplicate the World name
        WorldList.append(currentWorld)
    for world in WorldList:
        world.printWorlds()
