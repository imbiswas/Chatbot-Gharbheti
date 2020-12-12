from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
class tokenization(object):
    def __init__(self,value):
        self.value=value
        self.token()

    def token(self):
        try:
            self.value=self.value.lower()
            #remove special symbols
            removeSpecialSymbol=re.sub('[^a-z0-9 ]+', '', self.value)
            # print(removeSpecialSymbol)


            stop_words = set(stopwords.words('english'))
            word_tokens = word_tokenize(removeSpecialSymbol)
            filtered_sentence = [w for w in word_tokens if not w in stop_words]
            # print(word_tokens)
            # print(filtered_sentence)
            return (filtered_sentence)
        except Exception:
            print("Error from tokenization")

