#pip install nltk
from nltk import bigrams
x = bigrams("akil")
for b in  x:
    print(b)

print ("----------------")

from typing import List
sentence: List[str] = "I am Akil Bhuiyan".split() # List[str] -> This sentence is a List of string
for b in bigrams(sentence):
    print(b)
