import random
class World:
    '''A World, Storing the Information of Players that Can Play them

    A Player may only Appear once per World, or must be submitted under a different Slot name
    '''
    def __init__(self,world_name):
        # Given World Name
        self.name=world_name
        # Players that Can play this World
        # Currently random For Dev Purposes
        self.players=set()
        #TODO add a way to initialize this from a File or Something
    def __str__(self) -> str:
        return self.name + ': ' + repr(self.players)
    def __repr__(self) -> str:
        return self.__str__()
    def printPlayers(self):
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
        # has a Chance to pick the same twice, but since it turns into set it does not duplicate the players name
        WorldList.append(currentWorld)
    for world in WorldList:
        world.printPlayers()
