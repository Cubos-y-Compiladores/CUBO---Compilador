import ply.yacc as yacc
import os, codecs, re

from pip._vendor import colorama
from pip._vendor.distlib.compat import raw_input

from Lexer import tokens
from Lexer import tokenViewer as tv
from sys import stdin

precedence = (
    ('right','ID'),
    ('right', 'ASSIGN'),
    ('left', 'LT', 'LTE', 'GT', 'GTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MOD', 'DIVENT', 'TIMES', 'DIVIDE'),
    ('left', 'EXP'),
    ('left', 'LPARENT', 'RPARENT'),
)
def p_program(p):
    '''program : block'''
    print("program")
def p_block(p):
    '''block : assignmentList function'''
    #print("block")

def p_assignmentList(p):
    '''assignmentList : ID ASSIGN term SEMICOLON block
    | empty'''
    print("Assignment")
def p_function(p):
    '''function : type
                | empty'''

def p_term(p):
    '''term : factor
            | TRUE
            | FALSE
            | empty'''
    print(p[1])
def p_factor(p):
    """factor : INT
              | ID"""
def p_type(p):
    '''type : TYPE LPARENT ID RPARENT SEMICOLON'''
    print("Caso TYPE")

def p_empty(p):
    'empty : '
    pass

def p_error(p):
    if (p):
        print(colorama.Fore.RED + "SYNTACTIC ERROR: line:", p.lexer.lineno, "position:", p.lexpos, "Syntax error:", p.value, colorama.Fore.RESET)
    else:
        print(colorama.Fore.RED + "SYNTACTIC ERROR: Unknown syntax error" + colorama.Fore.RESET)


test = '/home/dcamachog1501/Induced_Desktop/Test'
fp = codecs.open(test, "r", "utf-8")
chain = fp.read()
parser = yacc.yacc('SLR')
tv(chain)
result = parser.parse(chain)
print(result)
