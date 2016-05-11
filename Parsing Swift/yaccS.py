import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lexS import tokens

DEBUG = False

# Namespace & built-in functions

name = {}

#  Evaluation functions

def lisp_eval(simb, items):
    if simb in name:
        return call(name[simb], eval_lists(items))
    else:
        return [simb] + items

def call(f, l):
    try:
        return f(eval_lists(l))
    except TypeError:
        return f

def eval_lists(l):
    r = []
    for i in l:
        if is_list(i):
            if i:
                r.append(lisp_eval(i[0], i[1:]))
            else:
                r.append(i)
        else:
            r.append(i)
    return r

# Utilities functions

def is_list(l):
    return type(l) == type([])

def lisp_str(l):
    if type(l) == type([]):
        if not l:
            return "()"
        r = "("
        for i in l[:-1]:
            r += lisp_str(i) + " "
        r += lisp_str(l[-1]) + ")"
        return r
    elif l is True:
        return "#t"
    elif l is False:
        return "#f"
    elif l is None:
        return 'nil'
    else:
        return str(l)

# BNF

def p_exp_atom(p):
    'exp : atom'
    p[0] = p[1]

def p_exp_wrap(p):
    'exp : BSLASH LPAREN exp RPAREN'
    print "Saw " + p[3]
    p[0] = p[3]

def p_exp(p):
    'exp : atom PLUS atom'
    print "Addition: " + p[1:]
    p[0] = p[1:]

def p_exp_string(p):
    'exp : QUOTE exp QUOTE'
    print "Producing string equivalent: " + p[2]
    p[0] = ["Producing string equivalent: "] + p[2]

def p_exp_let(p):
    'exp : LET atom SIMB exp'
    print "Calling let on " + p[2]
    p[0] = ["Calling let on "] + [p[2]]

def p_atom_simbol(p):
    'atom : SIMB'
    p[0] = p[1]

def p_atom_num(p):
    'atom : NUM'
    p[0] = p[1]

def p_atom_word(p):
    'atom : TEXT'
    p[0] = p[1]

def p_atom_empty(p):
    'atom :'
    pass

# Error rule for syntax errors
def p_error(p):
    print "Syntax error!! ",p

# Build the parser
# Use this if you want to build the parser using SLR instead of LALR
# yacc.yacc(method="SLR")
yacc.yacc()
with open('SStest.txt', 'r') as content_file:
    content = content_file.read()
    yacc.parse(content)
