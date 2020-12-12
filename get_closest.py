from nltk.tokenize import word_tokenize
from difflib import get_close_matches
from difflib import SequenceMatcher
import sqlServer


lis = sqlServer.databaseWriter()
lists=lis.myvalues()
# print(lists)


def correct_content(word) :
    # if word in lists:
    #     return  word
    for w in lists:
         s = SequenceMatcher(None, word, w).ratio()
         if s > 0.9:
             return get_close_matches(word.lower(),lists)[0]

    return word


