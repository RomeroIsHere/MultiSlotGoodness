import logging
from DSGFileHandler import InputHandler, OutputHandler, Utility
logger=logging.getLogger(__name__)

def RenameYamls():
    renamedict: dict[str,str|int]=InputHandler.ParseRenameYaml()
    EveryNameSet=set()
    RepeatedSender=set()
    RepeatedReceiver=set()
    for Sender, Receiver in renamedict.items():
        if Sender in EveryNameSet:
            RepeatedSender.add(Sender)
        EveryNameSet.add(Sender)
        if Receiver in EveryNameSet:
            RepeatedReceiver.add(Receiver)
        EveryNameSet.add(Receiver)
    if len(RepeatedReceiver) or len(RepeatedSender):
        logger.error(f"Names Repeat Within the Duplications")
        for Element in sorted(RepeatedReceiver):
            print(Element)
            logger.warning(f'Receiving Player "{Element}" is already present in the set')
        for Element in sorted(RepeatedSender):
            print(Element)
            logger.warning(f'Sending Player "{Element}" is already present in the set')
    OutputHandler.RenameAndCopyYAML(renamedict)

def StripPlando():
    OutputHandler.RenameAndStripYAML()

if __name__ == "__main__":
    Utility.MakeDir("logs")
    logging.basicConfig(filename='logs/renaming.log', encoding='utf-8', level=logging.INFO, format='[%(asctime)s]%(name)s:%(levelname)s %(message)s',  datefmt='%I:%M:%S')
    StripPlando()