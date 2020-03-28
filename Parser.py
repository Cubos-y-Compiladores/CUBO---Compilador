import ply.yacc as yacc
import os, codecs, re

from pip._vendor import colorama
from pip._vendor.distlib.compat import raw_input

from Lexer import tokens
from Lexer import tokenViewer as tv
from sys import stdin

precedence = (
    ('left','ID','IF','WHILE','TYPE','LEN','BLINK','DELAY','FOR'),
    ('right','ASSIGN'),
    ('left', 'LT', 'LTE', 'GT', 'GTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MOD', 'DIVENT', 'TIMES', 'DIVIDE'),
    ('left', 'EXP'),
    ('left','LPARENT', 'RPARENT'),
)
##########---BLOQUES BASICOS---#########
def p_program(p):
    '''program : const_block main_proc'''
    print("program")

def p_constB(p):
    '''const_block : const const const const const block'''
    print("const_block")

def p_block0(p):
    '''block : procedure block'''
    print("block0")

def p_block1(p):
    '''block : global block'''
    print("block1")

def p_blockEmp(p):
    '''block : empty'''
    print("blockEmp")





##########---BLOQUES ALTERNATIVOS---##########
def p_altBlock(p):
    '''alt_block : alt_content alt_block'''
    print("alt_block")

def p_emptyaltBlock(p):
    '''alt_block : empty'''
    print("emptyaltBlock")

def p_altContent0(p):
    '''alt_content : instruction'''
    print("altCont0")

def p_altContent1(p):
    '''alt_content : assignment'''
    print("altCont1")





##########---INSTRUCCIONES---##########
def p_instruction0(p):
    ''' instruction : function '''
    print("instruction1")

def p_instruction1(p):
    ''' instruction : consult SEMICOLON '''
    print("instruction1")

def p_instruction2(p):
    '''instruction : cycle '''
    print("instruction2")

def p_instruction3(p):
    '''instruction : statement '''
    print("instruction3")





##########---ASIGNACIONES GLOBALES---##########
def p_globalAssignment(p):
    '''global : GLOBAL assignment '''
    print("globalAssignment")





##########---ASIGNACIONES---##########
def p_simpleAssignment(p):
    '''assignment : identifier ASSIGN a_content SEMICOLON '''
    print("simpleAssignment")

def p_doubleAssignment(p):
    '''assignment : identifier COMMA identifier ASSIGN a_content COMMA a_content SEMICOLON '''
    print("doubleAssignment")





##########---FUNCIONES---##########
def p_function0(p):
    '''function : type '''
    print("function0")

def p_function1(p):
    '''function : insert'''
    print("function1")

def p_function2(p):
    '''function : del'''
    print("function2")

def p_function3(p):
    '''function : len'''
    print("function3")

def p_function4(p):
    '''function : neg'''
    print("function4")

def p_function5(p):
    '''function : t_f'''
    print("function5")

def p_function6(p):
    '''function : blink'''
    print("function6")

def p_function7(p):
    '''function : delay'''
    print("function7")

def p_function8(p):
    '''function : shape'''
    print("function8")

def p_function9(p):
    '''function : delete'''
    print("function9")

def p_function10(p):
    '''function : call'''
    print("function10")

def p_type(p):
    '''type : TYPE LPARENT identifier RPARENT SEMICOLON '''
    print("type")

def p_range(p):
    '''a_content : RANGE LPARENT INT COMMA value RPARENT'''
    print("range")

def p_insert(p):
    '''insert : identifier DOT INSERT LPARENT i_content RPARENT SEMICOLON '''
    print("insert")

def p_del(p):
    ''' del : identifier DOT DEL LPARENT INT RPARENT SEMICOLON '''
    print("delete_list")

def p_len(p):
    ''' len : LEN LPARENT ID RPARENT SEMICOLON '''
    print("len")

def p_neg0(p):
    ''' neg :  identifier DOT NEG SEMICOLON '''
    print("neg0")

def p_tf(p):
    '''t_f : identifier DOT tf SEMICOLON '''
    print("tf_function")

def p_blink(p):
    ''' blink : BLINK LPARENT b_content RPARENT SEMICOLON '''
    print("blink")

def p_delay(p):
    '''delay : DELAY LPARENT d_content RPARENT SEMICOLON '''
    print("delay")

def p_shapeArg0(p):
    '''shape_arg : SHAPEF'''
    print("shapeArg0")

def p_shapeArg1(p):
    '''shape_arg : SHAPEC'''
    print("shapeArg1")

def p_shapeArg2(p):
    '''shape_arg : SHAPEA'''
    print("shapeArg2")

def p_shape(p):
    '''shape : identifier DOT shape_arg SEMICOLON '''
    print("shape")

def p_delete(p):
    '''delete : identifier DOT DELETE LPARENT indice COMMA INT RPARENT SEMICOLON '''
    print("delete_mat")

def p_call(p):
    '''call : CALL proc_dec SEMICOLON'''
    print("call")





##########---CICLOS---##########
def p_cycle0(p):
    '''cycle : for'''
    print("cycle0")

def p_for(p):
    '''for : FOR ID IN iterable step LCORCH alt_block RCORCH SEMICOLON '''
    print("for")

def p_step0(p):
    '''step : STEP INT'''
    print("step0")

def p_stepEmp(p):
    '''step : empty'''
    print("stepEmpt")





##########---BIFURCACIONES---##########
def p_statement(p):
    '''statement : IF LPARENT iterable relation bif_value RPARENT LCORCH alt_block RCORCH SEMICOLON opt_statement '''
    print("statement")

def p_optStatment0(p):
    '''opt_statement : ELSE LCORCH alt_block RCORCH SEMICOLON '''
    print("optStatement0")

def p_optStatment1(p):
    '''opt_statement : empty '''
    print("optStatementEmp")





##########---PROCEDIMIENTOS---##########
def p_procedure(p):
    '''procedure : PROCEDURE proc_dec LCORCH body RCORCH SEMICOLON '''
    print("procedure")
def p_procDec(p):
    '''proc_dec : proc_name LPARENT parameter RPARENT'''
    print("proc_dec")

def p_procName(p):
    '''proc_name : ID'''
    print("proc_name")

def p_parameter0(p):
    '''parameter : proc_param'''
    print("parameter0")

def p_parameter1(p):
    '''parameter : proc_param COMMA parameter'''
    print("parameter1")

def p_emptyParameter(p):
    '''parameter : empty'''
    print("emptyParameter")

def p_procParam0(p):
    '''proc_param : ID'''
    print("proc_param0")

def p_body(p):
    '''body : BEGIN alt_block END SEMICOLON '''
    print("proc_body")

def p_mainProcedure(p):
    '''main_proc : MAIN LPARENT RPARENT LCORCH main_body RCORCH SEMICOLON block'''
    print("mainProcedure")

def p_mainBody(p):
    '''main_body : BEGIN main_block END SEMICOLON'''
    print("main_body")

def p_mainBlock0(p):
    '''main_block : instruction main_block'''
    print("main_block0")


def p_emptyMainblk(p):
    '''main_block : empty'''
    print("emptyMainblk")





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
    '''const : RANGOTIMER ASSIGN time_mes SEMICOLON'''
    print("rng_const")

def p_const2(p):
    '''const : dimension ASSIGN INT SEMICOLON'''
    print("dim_const")

def p_const3(p):
    '''const : CUBO ASSIGN INT SEMICOLON'''
    print("cube_const")





##########---CONTENIDO DE ASIGNACIONES---##########
def p_Acont0(p):
    '''a_content : value'''
    print("a_content0")

def p_Acont1(p):
    '''a_content : arithmetic'''
    print("a_content1")

def p_Acont2(p):
    '''a_content : list'''
    print("a_content2")

def p_Acont3(p):
    '''a_content : mat'''
    print("a_content3")

def p_Acont4(p):
    '''a_content : 3dmat'''
    print("a_content4")

def p_Acont5(p):
    '''a_content : consult'''
    print("a_content5")




##########---CONTENIDO DE FUNCIONES---##########
def p_Fcont0(p):
    '''b_content : list_consult COMMA INT COMMA time_mes COMMA value'''
    print("blink_content0")

def p_Fcont1(p):
    '''b_content : list_consult COMMA value'''
    print("blink_content1")

def p_Fcont2(p):
    '''d_content : empty'''
    print("delayEmp")

def p_Fcont3(p):
    '''d_content : INT COMMA time_mes'''
    print("delay_content0")

def p_Fcont4(p):
    '''tf : T'''
    print("t_content")

def p_Fcont5(p):
    '''tf : F'''
    print("f_content")

def p_Fcont6(p):
    '''i_content : INT COMMA value'''
    print("i_content0")

def p_Fcont7(p):
    '''i_content : list COMMA INT i_ind'''
    print("i_content1")



##########---LISTAS Y MATRICES---##########
def p_list(p):
    '''list : PARENTCL list_term PARENTCR'''
    print("list")

def p_listEmp(p):
    '''list : PARENTCL empty PARENTCR'''
    print("lEmpt")

def p_listT0(p):
    '''list_term : list_value COMMA list_term'''
    print("list_term0")

def p_listT1(p):
    '''list_term : list_value'''
    print("list_term1")

def p_listV0(p):
    '''list_value : value'''
    print("list_value0")

def p_mat(p):
    '''mat : PARENTCL mat_term PARENTCR'''
    print("mat")

def p_matT0(p):
    '''mat_term : mat_value COMMA mat_term'''
    print("mat_term0")

def p_matT1(p):
    '''mat_term : mat_value'''
    print("mat_term1")

def p_matV0(p):
    '''mat_value : list'''
    print("mat_value0")

def p_3dmat(p):
    '''3dmat : PARENTCL 3dmat_term PARENTCR'''
    print("3dmat")

def p_3dmatT0(p):
    '''3dmat_term : 3dmat_value COMMA 3dmat_term'''
    print("3dmat_term0")

def p_3dmatT1(p):
    '''3dmat_term : 3dmat_value'''
    print("3dmat_term1")

def p_3dmatV0(p):
    '''3dmat_value : mat'''
    print("3dmat_value0")

def p_consult0(p):
    '''consult : list_consult '''
    print("consult0")

def p_consult1(p):
    '''consult : mat_consult '''
    print("consult1")

def p_consult2(p):
    '''consult : 3dmat_consult'''
    print("consult2")

def p_Lstconsult(p):
    '''list_consult : ID lst_consultT '''
    print("listConslt0")

def p_LstconsultT0(p):
    '''lst_consultT : PARENTCL indice PARENTCR'''
    print("LstConsltT0")

def p_LstconsultT1(p):
    '''lst_consultT : PARENTCL indice TP indice PARENTCR '''
    print("LstConsltT1")

def p_Matconsult(p):
    '''mat_consult : ID mat_consultT '''
    print("matConslt0")

def p_MatconsultT0(p):
    '''mat_consultT : PARENTCL indice COMMA indice PARENTCR'''
    print("matConsltT0")

def p_MatconsultT1(p):
    '''mat_consultT : PARENTCL TP COMMA indice PARENTCR '''
    print("matConsltT1")

def p_MatconsultT2(p):
    '''mat_consultT : PARENTCL TP PARENTCR lst_consultT '''
    print("matConsltT2")

def p_MatconsultT3(p):
    '''mat_consultT : PARENTCL indice PARENTCR lst_consultT'''
    print("matConsltT3")

def p_3dMatconsult(p):
    '''3dmat_consult : ID 3dmat_consultT'''
    print("3dmatConslt")

def p_3dMatconsultT0(p):
    '''3dmat_consultT : PARENTCL indice COMMA indice COMMA indice PARENTCR'''
    print("3dmatConsltT0")

def p_3dMatconsultT1(p):
    '''3dmat_consultT : PARENTCL indice PARENTCR mat_consultT'''
    print("3dmatConsltT1")



##########---INDICES---##########
def p_indice0(p):
    '''indice : INT'''
    print("indice0")

def p_indice1(p):
    '''indice : ID'''
    print("indice1")

def p_Insind0(p):
    '''i_ind : COMMA INT'''
    print("insInd0")

def p_InsindEmp(p):
    '''i_ind : empty'''
    print("insIndEmp")



##########---DIMENSIONES---##########
def p_dim0(p):
    '''dimension : DIMFILAS'''
    print("dim_filas")

def p_dim1(p):
    '''dimension : DIMCOLUMNAS'''
    print("dim_columnas")





##########---MEDIDAS DE TIEMPO---##########
def p_timeM0(p):
    '''time_mes : QUOTES MIL QUOTES'''
    print("timeM0")

def p_timeM1(p):
    '''time_mes : QUOTES MIN QUOTES'''
    print("timeM1")

def p_timeM2(p):
    '''time_mes : QUOTES SEG QUOTES'''
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

def p_Bifvalue0(p):
    '''bif_value : value'''
    print("bif_Value0")

def p_Bifvalue1(p):
    '''bif_value : arithmetic'''
    print("bif_Value1")

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

def p_relation6(p):
	'''relation : COMPARE'''
	print ("relation 6")



##########---IDENTIFICADORES---##########
def p_identifier0(p):
    '''identifier : ID'''
    print("identifier0")

def p_identifier1(p):
    '''identifier : consult'''
    print("identifier1")





##########---ITERABLES---##########
def p_iterable0(p):
    '''iterable : identifier'''
    print("iterable0")

def p_iterable1(p):
    '''iterable : INT'''
    print("iterable1")





##########---VARIOS---##########
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
