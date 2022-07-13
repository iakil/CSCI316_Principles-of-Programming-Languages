# Principles of Programming Languages

Principles and implementation of programming languages. Topics include: the procedural, object-oriented, functional, and logic programming paradigms, syntax (BNF, expression grammars, operator precedence and associativity), variables (scope, storage bindings, and lifetime), data types, control structures, function call and return (activation records and parameter passing), formal semantics. Programming assignments. 

<br>

<Details>
<summary>

## ClassCode:

</summary>
<pre>

### [DifferentEcstaticOrigin](https://github.com/iakil/CSCI316_Principles-of-Programming-Languages/tree/main/ClassCode/DifferentEcstaticOrigin)

### [DroopyAggressiveCharactermapping](https://github.com/iakil/CSCI316_Principles-of-Programming-Languages/tree/main/ClassCode/DroopyAggressiveCharactermapping)

### [GoldenLopsidedDifferences](https://github.com/iakil/CSCI316_Principles-of-Programming-Languages/tree/main/ClassCode/GoldenLopsidedDifferences)
</pre>
</details>


<details> 
<summary>

## HW:

</summary>
<pre>

[HW1](https://github.com/iakil/CSCI316_Principles-of-Programming-Languages/blob/main/HW/A_Bhuiyan_HW1.py) [HW2](https://github.com/iakil/CSCI316_Principles-of-Programming-Languages/blob/main/HW/A_Bhuiyan_HW2.py) [HW3](https://github.com/iakil/CSCI316_Principles-of-Programming-Languages/blob/main/HW/A_Bhuiyan_HW3.py) [HW4](https://github.com/iakil/CSCI316_Principles-of-Programming-Languages/blob/main/HW/A_Bhuiyan_HW4.py) [HW5](https://github.com/iakil/CSCI316_Principles-of-Programming-Languages/blob/main/HW/A_Bhuiyan_HW5.py)
</pre>
<details>
<summary> 
 HW1    
</summary>
<pre>

## HW 1: Find the area of a circle in Python

Here is a [alt](https://replit.com/@JoshuaWaxman/DifferentEcstaticOrigin#main.py) [(link)](https://github.com/iakil/CSCI316_Principles-of-Programming-Languages/tree/main/ClassCode/DifferentEcstaticOrigin) to my REPL:

There, you will find the following code (towards the bottom):

```python
def compute_area_circle():
    # put your name in a comment here
  
    # make definitions here
    radius:int = 0
 
    # get the radius using a function
 
    # processing using a function
    # output the area here by calling a function
 
    pass
compute_area_circle()

```

Create your own public REPL. (If you want, name the file hw1.py or something like that.) 
Start recording using Chrome DevTools Recorder tool. Copy the above code into the REPL.
Modify the code so it has your own name in the first comment. Also, after each of the subsequent comments, call a function. That function can either be a nested function (in which case you will likely have to use the nonlocal keyword to access radius and PI), or a function outside of compute_area_circle() (in which case you will likely have to use the global keyword to access radius and / or PI).

 To submit:
1) The Python file (ending in .py)
2) The link to your own REPL (as a comment, perhaps on the assignment if this is possible).
3) The exported JSON for your recording. (I'll be able to lightly edit it and then replay the recording myself.)
</pre>
</details>
<details>
<summary> 
 HW2    
</summary>
<pre>

## HW 2: Add exponent to CFG

Here is a [alt](https://replit.com/@JoshuaWaxman/DroopyAggressiveCharactermapping#main.py) [(link)](https://github.com/iakil/CSCI316_Principles-of-Programming-Languages/tree/main/ClassCode/DroopyAggressiveCharactermapping/main.py) to my REPL:

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
</pre>
</details>
<details>
<summary> 
 HW3   
</summary>
<pre>

## HW 3: Modify PLY calc code

You can access the code for this assignment here, at replit: [alt](https://replit.com/@JoshuaWaxman/GoldenLopsidedDifferences#main.py) [(link)](https://github.com/iakil/CSCI316_Principles-of-Programming-Languages/tree/main/ClassCode/GoldenLopsidedDifferences/main.py)

Modify the code to support the following three bits of functionality.
1) Change the NUMBER token so that it supports floats (with a single decimal point) and not just ints. It should still recognize ints (like 5), so the single decimal point should be optional in your regex portion of the code. 
2) Add a binary operator of == to do comparison. If the two operands are equal, then it should evaluate to 1.0. Otherwise it should evaluate to 0.0.
3) At a ternary elvis operator ?: which works like the question mark - colon in C++. That is, in x ? y : z, if the expression represented by x evaluates to non-zero, then the entire expression evaluates to y. Otherwise, the entire expression evaluates to z. Note that x, y and z need not be individual variables (that is, NAME) but are expressions. Since this is a ternary operator rather than binary, I would recommend copying the entire p_ function for binop, renaming it for ternary, and modifying that.
</pre>
</details>
</details>