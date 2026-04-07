from datetime import datetime
import os
def getFileName() -> str:
    return str(datetime.now().strftime('%Y-%m-%d-%H%M%S%f')[:-3]) + '.yaml'

def MakeDir(outputdir='logs'):
    if not os.path.isdir(outputdir):
        os.makedirs(outputdir)