from datetime import datetime
from difflib import SequenceMatcher
import os
def getFileName() -> str:
    return str(datetime.now().strftime('%Y-%m-%d-%H%M%S%f')[:-3]) + '.yaml'

def MakeDir(outputdir='logs'):
    if not os.path.isdir(outputdir):
        os.makedirs(outputdir)
def similar_strings(to_compare:str, to_match:str) -> float:
    """Takes in two strings and returns a float of the percentage they are similar to each other

    Parameters
    ----------
    to_compare : str
        The string you want to compare
    to_match : str
        The string you want to compare against

    Returns
    -------
    float
        The ratio of the similarity between to strings
    """
    # Remove excess whitespace
    to_compare = to_compare.strip()
    to_match = to_match.strip()
    return SequenceMatcher(None, to_compare, to_match).ratio()

def suggest_word(input_word:str, word_list:list[str]) -> tuple[str,float]:
    """Takes in a string and a list of words and returns the most likely word

    Parameters
    ----------
    input_word : str
        The word you want to check for similarity

    word_list : list[str]
        The list of words to test input_word against for similarity

    Returns
    -------
    str
        The most similar word, can also be empty string if none had more than %10 similarity
    """
    similarities = {}
    for current_word in word_list:
        similarities[current_word] = similar_strings(input_word, current_word)
    similarities = dict(sorted(similarities.items(),key=lambda x:x[1], reverse=True))
    for word in similarities:
        return (word,similarities[word])     # Return first word in dictionary
    return ("",0)