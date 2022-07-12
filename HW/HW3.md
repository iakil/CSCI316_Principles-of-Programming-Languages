## HW 3: Modify PLY calc code

You can access the code for this assignment here, at replit: [link](https://replit.com/@JoshuaWaxman/GoldenLopsidedDifferences#main.py) [(alt)](https://github.com/iakil/CSCI316_Principles-of-Programming-Languages/tree/main/ClassCode/GoldenLopsidedDifferences/main.py)

Modify the code to support the following three bits of functionality.
1) Change the NUMBER token so that it supports floats (with a single decimal point) and not just ints. It should still recognize ints (like 5), so the single decimal point should be optional in your regex portion of the code. 
2) Add a binary operator of == to do comparison. If the two operands are equal, then it should evaluate to 1.0. Otherwise it should evaluate to 0.0.
3) At a ternary elvis operator ?: which works like the question mark - colon in C++. That is, in x ? y : z, if the expression represented by x evaluates to non-zero, then the entire expression evaluates to y. Otherwise, the entire expression evaluates to z. Note that x, y and z need not be individual variables (that is, NAME) but are expressions. Since this is a ternary operator rather than binary, I would recommend copying the entire p_ function for binop, renaming it for ternary, and modifying that.
