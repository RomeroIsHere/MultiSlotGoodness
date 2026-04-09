from collections.abc import Callable
#MENUUUUUU
def emptyCallable(*args, **kwargs):
    pass

def representsInt(s:str) -> bool:
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True

def intInput(s:str) -> int:
    CandidateNumber=input(s)
    if(representsInt(CandidateNumber)):
        return abs(int(CandidateNumber))
    else:
        return -1
def pause():
    input("Press enter to continue...")

def menu(Title:str='Main Menu',submenu:list[tuple[str,Callable]]=[('EmptyAction',emptyCallable)],separate="""-__-__-__-__-__-__-__-__-__-__-__-__-"""):
    WantsToExit=False
    while not WantsToExit:
        print(Title)
        maxIndex=-1
        for index, tuplere in enumerate(submenu):
            print(f"{index}:{tuplere[0]}")
            maxIndex=index+1
            pass
        print(f'{maxIndex}:Exit.')
        ins=intInput(":")
        print(separate)
        if maxIndex==ins:
            WantsToExit=True
        elif ins>=0:
            try:
                submenu[ins][1]()
            except IndexError:
                print("Please choose between the avaible options")
                pause()
        else:
            print("Unknown Input, Please Use the number of the option you want")
            pause()
#End Menu

if __name__ == "__main__":
    menu()
    pass