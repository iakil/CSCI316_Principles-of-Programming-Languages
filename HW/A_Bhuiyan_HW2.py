# Akil Bhuiyan
# Professor Joshua Waxman
# CSCI 316
# HW2 - Add exponent to CFG

# imports
from nltk import CFG
from nltk import ChartParser

# Exponent added to the CFG
grammar = CFG.fromstring("""
S -> Expression
Expression -> Expression PlusMinus Term1 | Term1
Term1 -> Term2 | Term1 TimesDivide Term2
Term2 -> Factor | Term2 Exponent Factor
Factor -> 'W' | 'X' | 'Y' | 'Z'                              
PlusMinus -> '+' | '-'
Exponent -> '^'
TimesDivide -> '*' | '/'                  
""")

print('The productions are:', grammar.productions()) # Print the productions

parser = ChartParser(grammar)
sentence = 'W ^ X + Y * Z'.split() # Sentence
print('The statement is', sentence) # Print the statement
for tree in parser.parse(sentence):
    print(tree)
    tree.draw()