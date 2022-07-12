## HW 2: Add exponent to CFG

Here is a [link](https://replit.com/@JoshuaWaxman/DroopyAggressiveCharactermapping#main.py) [(alt)](https://github.com/iakil/CSCI316_Principles-of-Programming-Languages/tree/main/ClassCode/DroopyAggressiveCharactermapping/main.py) to my REPL:

```python
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
```

Create your own public REPL, or use the same one as before. (Just don't lose previous content. Perhaps rename your old one as hw1.py instead of main. Start recording using Chrome DevTools Recorder tool. Copy the above code into the REPL.
Modify the code so it has your own name in a comment. Also, change the context free grammar (in the multiline string) so that it will also support an exponentiation operator. Recall that exponent has greater precedence than multiplication and division. Also, modify the sentence (in the line sentence = ...) so that it also involves your exponentiation operator.
To submit:

1) The Python file (ending in .py)
2) The link to your own REPL (as a comment, perhaps on the assignment if this is possible).
3) The exported JSON for your recording. (I'll be able to lightly edit it and then replay the recording myself.)
