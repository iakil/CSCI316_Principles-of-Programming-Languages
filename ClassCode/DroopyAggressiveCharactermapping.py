# from nltk import bigrams
# from typing import List
# sentence: List[str] = "I went to the store".split()
# for b in bigrams(sentence):
#   print(b)

# REPL = read eval print loop

# from nltk import CFG

# grammar = CFG.fromstring("""
# Sentence -> Subject Predicate
# Subject -> NounPhrase
# Predicate -> Verb NounPhrase
# NounPhrase -> Article Noun
# Noun -> 'dog' | 'cat' | 'car'
# Verb -> 'chased' | 'ate'
# Article -> 'the' | 'a'
# """)

# print('The productions are:', grammar.productions())

# from nltk import ChartParser
# parser = ChartParser(grammar)
# sentence = 'the dog chased the cat'.split()
# print('The sentence is', sentence)
# for tree in parser.parse(sentence):
#     print(tree)
#     tree.draw()


# from nltk import CFG
# import nltk

# grammar = nltk.CFG.fromstring("""
# S -> NP VP
# PP -> P NP
# NP -> Det N | Det N PP | 'I'
# VP -> V NP | VP PP
# Det -> 'an' | 'my'
# N -> 'elephant' | 'pajamas'
# V -> 'shot'
# P -> 'in'
# """)

# print('The productions are:', grammar.productions())

# from nltk import ChartParser
# parser = ChartParser(grammar)
# sentence = 'I shot an elephant in my pajamas'.split()
# print('The sentence is', sentence)
# for tree in parser.parse(sentence):
#     print(tree)
#     tree.draw()


# from nltk import CFG
# import nltk

# grammar = nltk.CFG.fromstring("""
# S -> Expression
# Expression -> Expression PlusMinus Expression | Term
# Term -> 'X' | 'Y' | 'Z'
# PlusMinus -> '+' | '-'
# """)

# print('The productions are:', grammar.productions())

# from nltk import ChartParser
# parser = ChartParser(grammar)
# sentence = 'X - Y + Z'.split()
# print('The statement is', sentence)
# for tree in parser.parse(sentence):
#     print(tree)
#     tree.draw()


from nltk import CFG
import nltk

grammar = nltk.CFG.fromstring("""
S -> Expression
Expression -> Expression PlusMinus Term | Term
Term -> Factor | Term TimesDivide Factor
Factor -> 'X' | 'Y' | 'Z'                              
PlusMinus -> '+' | '-'
TimesDivide -> '*' | '/'                  
""")

print('The productions are:', grammar.productions())

from nltk import ChartParser
parser = ChartParser(grammar)
sentence = 'X + Y * Z'.split()
print('The statement is', sentence)
for tree in parser.parse(sentence):
    print(tree)
    tree.draw()
