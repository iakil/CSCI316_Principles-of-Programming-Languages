# Akil Bhuiyan
# Professor Joshua Waxman
# CSCI 316
# HW2 - Add exponent to CFG

from nltk import CFG
from nltk import ChartParser

grammar = CFG.fromstring("""
S -> Expression
Expression -> Expression PlusMinus SecondTerm | SecondTerm
SecondTerm -> Term | SecondTerm TimesDivide Term
Term -> Factor | Term Exponent Factor
Factor -> 'A' | 'X' | 'Y' | 'Z'                              
PlusMinus -> '+' | '-'
TimesDivide -> '*' | '/'  
Exponent -> '^'                              
""")

print('\n\n\nThe productions are:', grammar.productions(), "\n\n\t\tDefault sentence is: A ^ X + Y * Z \n\t\t(Note: Make sure to put spaces)") 

parser = ChartParser(grammar)
#sentence = 'A ^ X + Y * Z'.split()
sentence = input("Sentence: ").split()
print('The statement is', sentence)


try:
    for tree in parser.parse(sentence):
        #print(tree)
        tree.pretty_print()
        tree.draw()
except ValueError:
    print("No parse tree possible.")