import logging
from DSGFileHandler import OutputHandler, Utility
logger=logging.getLogger(__name__)

def StripPlando():
    OutputHandler.RenameAndStripYAML()



if __name__ == "__main__":
    Utility.MakeDir("logs")
    logging.basicConfig(filename='logs/plandostripping.log', encoding='utf-8', level=logging.INFO, format='[%(asctime)s]%(name)s:%(levelname)s %(message)s',  datefmt='%I:%M:%S')
    StripPlando()