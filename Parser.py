import ply.yacc as yacc
import os, codecs, re

from pip._vendor import colorama
from pip._vendor.distlib.compat import raw_input

from Lexer import tokens
from Lexer import tokenViewer as tv
from sys import stdin

precedence = (
    ('right','ID','IF','WHILE','TYPE'),
    ('right','ASSIGN'),
    ('left', 'LT', 'LTE', 'GT', 'GTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MOD', 'DIVENT', 'TIMES', 'DIVIDE'),
    ('left', 'EXP'),
    ('left','LPARENT', 'RPARENT'),
)
def p_program(p):
    '''program : const_block'''
    print("program")

def p_constB(p):
    '''const_block : const const const const const block'''
    print("const_block")

def p_block(p):
    ''' block : assignment function'''
    print("block")

def p_simpleAssignment0(p):
    '''assignment : ID ASSIGN value SEMICOLON block'''
    print("simpleAssignment0")

def p_simpleAssignment1(p):
    '''assignment : ID ASSIGN arithmetic SEMICOLON block'''
    print("simpleAssignment1")

def p_doubleAssignment(p):
    '''assignment : ID COMMA ID ASSIGN value COMMA value SEMICOLON block'''
    print("doubleAssignment")

def p_assignmentEmp(p):
    '''assignment : empty'''
    print("aEmpt")

def p_function(p):
    '''function : type'''
    print("function")

def p_functionEmp(p):
    '''function : empty'''
    print("fEmpt")

def p_type(p):
    '''type : TYPE LPARENT ID RPARENT SEMICOLON block'''
    print("type")

def p_arithmetic0(p):
    ''' arithmetic : term'''
    print("arithmetic0")
def p_arithmetic1(p):
    '''arithmetic : adding_operator term '''
    print("arithmetic1")

def p_arithmetic2(p):
    '''arithmetic : arithmetic adding_operator term'''
    print("arithmetic2")

def p_term0(p):
    '''term : factor'''
    print("term0")

def p_term1(p):
    '''term : term multiplying_operator factor'''
    print("term1")

def p_factor0(p):
    '''factor : INT'''
    print("factor0")

def p_factor1(p):
    '''factor : ID'''
    print("factor1")

def p_factor2(p):
    '''factor : LPARENT arithmetic RPARENT'''
    print("factor2")

def p_const0(p):
    '''const : TIMER ASSIGN INT SEMICOLON'''
    print("timer_const")

def p_const1(p):
    '''const : RANGOTIMER ASSIGN QUOTES time_mes QUOTES SEMICOLON'''
    print("rng_const")

def p_const2(p):
    '''const : dimension ASSIGN INT SEMICOLON'''
    print("dim_const")

def p_const3(p):
    '''const : CUBO ASSIGN INT SEMICOLON'''
    print("cube_const")




def p_dim0(p):
    '''dimension : DIMFILAS'''
    print("dim_filas")

def p_dim1(p):
    '''dimension : DIMCOLUMNAS'''
    print("dim_columnas")

def p_timeM0(p):
    '''time_mes : MIL'''
    print("timeM0")

def p_timeM1(p):
    '''time_mes : MIN'''
    print("timeM1")

def p_timeM2(p):
    '''time_mes : SEG'''
    print("timeM2")

def p_addingOp0(p):
    '''adding_operator : PLUS'''
    print("Plus")

def p_addingOp1(p):
    '''adding_operator : MINUS'''
    print("Minus")

def p_multiplyingOp0(p):
    '''multiplying_operator : TIMES'''
    print("Times")
def p_multiplyingOp1(p):
    '''multiplying_operator : EXP'''
    print("Exponencial")

def p_multiplyingOp2(p):
    '''multiplying_operator : DIVIDE'''
    print("Divide")

def p_multiplyingOp3(p):
    '''multiplying_operator : DIVENT'''
    print("Divent")

def p_multiplyingOp4(p):
    '''multiplying_operator : MOD'''
    print("Module")

def p_value0(p):
    '''value : FALSE'''
    print("value0")

def p_value1(p):
    '''value : TRUE'''
    print("value1")

def p_value2(p):
    '''value : ID'''
    print("value2")

def p_value3(p):
    '''value : INT'''
    print("value3")
    
def p_relation0(p):
	'''relation : ASSIGN'''
	print ("relation 0")

def p_relation1(p):
	'''relation : NE'''
	print ("relation 1")

def p_relation2(p):
	'''relation : LT'''
	print ("relation 2")

def p_relation3(p):
	'''relation : GT'''
	print ("relation 3")

def p_relation4(p):
	'''relation : LTE'''
	print ("relation 4")

def p_relation5(p):
	'''relation : GTE'''
	print ("relation 5")
    
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
