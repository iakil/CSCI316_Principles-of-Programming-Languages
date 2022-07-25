# Akil Bhuiyan
# Professor Joshua Waxman
# CSCI 316
# HW3 - Modify PLY calc code

# imports
import sys
import ply.lex as lex
import ply.yacc as yacc


sys.path.insert(0, "../..")

tokens = (
    'NAME', 'FLOAT' , 'INTEGER' , 'NAME2'
)

literals = ['=', '+', '-', '*', '/', '(', ')']

# Tokens
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NAME2 = r'\d+==\d+'



def t_FLOAT(t):
    r'\d+\.\d+'
    '[-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)'        
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_eof(t):
    more = input('... ')
    if more:
        t.lexer.input(more + '\n')
        return t.lexer.token()
    else:
        return None


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules

precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
)

# dictionary of names
names = {}
names2 = {}

def p_statement_assign(p):
    'statement : NAME2 "==" expression'
    names2[p[4]] = p[3]

def p_statement_assign(p):
    'statement : NAME "=" expression'
    names[p[1]] = p[3]



def p_statement_expr(p):
    'statement : expression'
    print(p[1])

def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression
                  '''
    
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[3] == '=':
        if p[1] == p[4]:
            p[0] = 1.0
        else: 
            p[0] = 0.0
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = -p[2]

def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]

def p_expression_integer(p):
    'expression : INTEGER'
    p[0] = p[1]

def p_expression_float(p):
    'expression : FLOAT'
    p[0] = p[1]

def p_expression_name(p):
    "expression : NAME"
    try:
        p[0] = names[p[1]]

    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s + '\n')
