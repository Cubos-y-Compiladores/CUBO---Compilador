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
##########---BLOQUES BASICOS---#########
def p_program(p):
    '''program : const_block'''
    print("program")

def p_constB(p):
    '''const_block : const const const const const block'''
    print("const_block")

def p_block0(p):
    ''' block : assignment'''
    print("block0")


def p_block1(p):
    ''' block : function'''
    print("block1")


def p_block2(p):
    ''' block : consult'''
    print("block2")


##########---ASIGNACIONES---##########
def p_simpleAssignment0(p):
    '''assignment :  complex_id ASSIGN content SEMICOLON block'''
    print("simpleAssignment0")

def p_simpleAssignment1(p):
    '''assignment :  GLOBAL ID ASSIGN content SEMICOLON block'''
    print("simpleAssignment1")

def p_doubleAssignment(p):
    '''assignment : ID COMMA ID ASSIGN value COMMA value SEMICOLON block'''
    print("doubleAssignment")

def p_assignmentEmp(p):
    '''assignment : empty'''
    print("aEmpt")





##########---FUNCIONES---##########
def p_function(p):
    '''function : type '''
    print("function")

def p_type(p):
    '''type : TYPE LPARENT ID RPARENT SEMICOLON block'''
    print("type")

def p_range(p):
    '''content : RANGE LPARENT INT COMMA value RPARENT'''
    print("range")





##########---OPERACIONES ARITMETICAS---##########
def p_arithmetic0(p):
    ''' arithmetic : term'''
    print("arithmetic0")
def p_arithmetic1(p):
    '''arithmetic : adding_operator term '''
    print("arithmetic1")

def p_arithmetic2(p):
    '''arithmetic : arithmetic adding_operator term'''
    print("arithmetic2")





##########---TERMINOS---##########
def p_term0(p):
    '''term : factor'''
    print("term0")

def p_term1(p):
    '''term : term multiplying_operator factor'''
    print("term1")





##########---FACTORES---##########
def p_factor0(p):
    '''factor : INT'''
    print("factor0")

def p_factor1(p):
    '''factor : ID'''
    print("factor1")

def p_factor2(p):
    '''factor : LPARENT arithmetic RPARENT'''
    print("factor2")





##########---CONSTANTES DE CONFIGURACION---##########
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





##########---CONTENIDO DE ASIGNACIONES---##########
def p_cont0(p):
    '''content : value'''
    print("content0")

def p_cont1(p):
    '''content : arithmetic'''
    print("content1")

def p_cont2(p):
    '''content : PARENTCL list_term PARENTCR'''
    print("content2")



##########---LISTAS---##########
def p_listT0(p):
    '''list_term : value COMMA list_term'''
    print("list_term0")

def p_listT1(p):
    '''list_term : value'''
    print("list_term1")

def p_listTEmp(p):
    '''list_term : '''
    print("lEmpt")


def p_consult0(p):
    '''consult : ID PARENTCL INT PARENTCR SEMICOLON block'''
    print("simple_conslt")

def p_consult1(p):
    '''consult : ID PARENTCL INT TP INT PARENTCR SEMICOLON block '''
    print("rng_conslt")



##########---DIMENSIONES---##########
def p_dim0(p):
    '''dimension : DIMFILAS'''
    print("dim_filas")

def p_dim1(p):
    '''dimension : DIMCOLUMNAS'''
    print("dim_columnas")





##########---MEDIDAS DE TIEMPO---##########
def p_timeM0(p):
    '''time_mes : MIL'''
    print("timeM0")

def p_timeM1(p):
    '''time_mes : MIN'''
    print("timeM1")

def p_timeM2(p):
    '''time_mes : SEG'''
    print("timeM2")





##########---OPERADORES---##########
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





##########---VALORES---##########
def p_value0(p):
    '''value : FALSE'''
    print("value0")

def p_value1(p):
    '''value : TRUE'''
    print("value1")





##########---RELACIONES---##########
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





##########---VARIOS---##########
def p_cmplxId0(p):
    '''complex_id : ID'''
    print("cmplxId0")

def p_cmplxId1(p):
    '''complex_id : ID PARENTCL INT PARENTCR'''
    print("cmplxId1")

def p_empty(p):
    'empty : '
    pass





##########---ERRORES---##########
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
