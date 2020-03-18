import ply.yacc as yacc
import os, codecs, re

from pip._vendor import colorama
from pip._vendor.distlib.compat import raw_input

from Lexer import tokens
from Lexer import tokenViewer as tv
from sys import stdin

precedence = (
    ('right','ID'),
    ('right','ASSIGN'),
    ('left', 'LT', 'LTE', 'GT', 'GTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MOD', 'DIVENT', 'TIMES', 'DIVIDE'),
    ('left', 'EXP'),
    ('left', 'LPARENT', 'RPARENT'),
)
def p_program(p):
    '''program : statement'''
    print("program")

def p_statement(p):
    ''' statement : simpleAssignment function'''
    print("statement")

def p_simpleAssignment0(p):
    '''simpleAssignment : ID ASSIGN term SEMICOLON statement'''
    print("simpleAssignment0")

def p_simpleAssignmentEmp(p):
    '''simpleAssignment : empty'''
    print("aEmpt")

def p_function0(p):
    '''function : type statement'''
    print("function0")

def p_functionEmp(p):
    '''function : empty'''
    print("fEmpt")
def p_type(p):
    '''type : TYPE LPARENT ID RPARENT SEMICOLON'''
    print("type")

def p_term0(p):
    '''term : FALSE'''
    print("term0")

def p_term1(p):
    '''term : TRUE'''
    print("term1")

def p_term2(p):
    '''term : factor'''
    print("term2")

def p_factor0(p):
    '''factor : ID'''
    print("factor0")

def p_factor1(p):
    """factor : INT"""
    print("factor1")

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
parser = yacc.yacc()
tv(chain)
result = parser.parse(chain)
print(result)
