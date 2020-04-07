import ply.yacc as yacc
import os, codecs, re
from TreeGen import *

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
    p[0]=ProgramNode([p[1],p[2]])
    print("program")

def p_constB(p):
    '''const_block : const const const const const block'''
    p[0]=NonTerminalNode("ConstB",[p[1],p[2],p[3],p[4],p[5],p[6]])
    print("const_block")

def p_block0(p):
    '''block : procedure block'''
    p[0]=NonTerminalNode("Block0",[p[1],p[2]])
    print("block0")

def p_block1(p):
    '''block : global block'''
    p[0]=NonTerminalNode("Block1",[p[1],p[2]])
    print("block1")

def p_blockEmp(p):
    '''block : empty'''
    p[0]=Null()
    print("blockEmp")





##########---BLOQUES ALTERNATIVOS---##########
def p_altBlock(p):
    '''alt_block : alt_content alt_block'''
    p[0]= NonTerminalNode("AltBlock",[p[1],p[2]])
    print("alt_block")

def p_emptyaltBlock(p):
    '''alt_block : empty'''
    p[0]=Null()
    print("emptyaltBlock")

def p_altContent0(p):
    '''alt_content : instruction'''
    p[0]=NonTerminalNode("AltContent0",[p[1]])
    print("altCont0")

def p_altContent1(p):
    '''alt_content : assignment'''
    p[0]=NonTerminalNode("AltContent1",[p[1]])
    print("altCont1")





##########---INSTRUCCIONES---##########
def p_instruction0(p):
    ''' instruction : function '''
    p[0]=NonTerminalNode("Instruction0",[p[1]])
    print("instruction0")

def p_instruction1(p):
    ''' instruction : consult SEMICOLON '''
    p[0]=NonTerminalNode("Instruction1",[p[1]])
    print("instruction1")

def p_instruction2(p):
    '''instruction : cycle '''
    p[0]=NonTerminalNode("Instruction2",[p[1]])
    print("instruction2")

def p_instruction3(p):
    '''instruction : statement '''
    p[0]=NonTerminalNode("Instruction3",[p[1]])
    print("instruction3")





##########---ASIGNACIONES GLOBALES---##########
def p_globalAssignment(p):
    '''global : GLOBAL assignment '''
    p[0]=NonTerminalNode("GlobalAssignment",[TerminalNode("Global","GLOBAL"),p[2]])
    print("globalAssignment")





##########---ASIGNACIONES---##########
def p_simpleAssignment(p):
    '''assignment : identifier ASSIGN a_content SEMICOLON '''
    p[0]=NonTerminalNode("SimpleAssignment",[p[1],TerminalNode("Assign","ASSIGN"),p[3]])
    print("simpleAssignment")

def p_doubleAssignment(p):
    '''assignment : identifier COMMA identifier ASSIGN a_content COMMA a_content SEMICOLON '''
    p[0]=NonTerminalNode("DoubleAssignment",[p[1],TerminalNode("Comma","COMMA"),p[3],TerminalNode("Assign","ASSIGN"),p[5],TerminalNode("Comma","COMMA"),p[7]])
    print("doubleAssignment")





##########---FUNCIONES---##########
def p_function0(p):
    '''function : type '''
    p[0]=NonTerminalNode("Function0",[p[1]])
    print("function0")

def p_function1(p):
    '''function : insert'''
    p[0]=NonTerminalNode("Function1",[p[1]])
    print("function1")

def p_function2(p):
    '''function : del'''
    p[0]=NonTerminalNode("Function2",[p[1]])
    print("function2")

def p_function3(p):
    '''function : len'''
    p[0]=NonTerminalNode("Function3",[p[1]])
    print("function3")

def p_function4(p):
    '''function : neg'''
    p[0]=NonTerminalNode("Function4",[p[1]])
    print("function4")

def p_function5(p):
    '''function : t_f'''
    p[0]=NonTerminalNode("Function5",[p[1]])
    print("function5")

def p_function6(p):
    '''function : blink'''
    p[0]=NonTerminalNode("Function6",[p[1]])
    print("function6")

def p_function7(p):
    '''function : delay'''
    p[0]=NonTerminalNode("Function7",[p[1]])
    print("function7")

def p_function8(p):
    '''function : shape'''
    p[0]=NonTerminalNode("Function8",[p[1]])
    print("function8")

def p_function9(p):
    '''function : delete'''
    p[0]=NonTerminalNode("Function9",[p[1]])
    print("function9")

def p_function10(p):
    '''function : call'''
    p[0]=NonTerminalNode("Function10",[p[1]])
    print("function10")

def p_type(p):
    '''type : TYPE LPARENT identifier RPARENT SEMICOLON '''
    p[0]=NonTerminalNode("TypeF",[TerminalNode("Type","TYPE"),TerminalNode("Lparent","LPARENT"),p[3],TerminalNode("Rparent","RPARENT")])
    print("type")

def p_range(p):
    '''a_content : RANGE LPARENT INT COMMA value RPARENT'''
    p[0]=NonTerminalNode("RangeF",[TerminalNode("Range","RANGE"),TerminalNode("Lparent","LPARENT"),TerminalNode("Int",p[3]),TerminalNode("Comma","COMMA"),p[5],TerminalNode("Rparent""RPARENT")])
    print("range")

def p_insert(p):
    '''insert : identifier DOT INSERT LPARENT i_content RPARENT SEMICOLON '''
    p[0]=NonTerminalNode("InsertF",[p[1],TerminalNode("Dot","DOT"),TerminalNode("Insert","INSERT"),TerminalNode("Lparent","LPARENT"),p[5],TerminalNode("Rparent","RPARENT")])
    print("insert")

def p_del(p):
    ''' del : identifier DOT DEL LPARENT INT RPARENT SEMICOLON '''
    p[0]=NonTerminalNode("DelF",[p[1],TerminalNode("Dot","DOT"),TerminalNode("Del","DEL"),TerminalNode("Lparent","LPARENT"),TerminalNode("Int",p[5]),TerminalNode("Rparent","RPARENT")])
    print("delete_list")

def p_len(p):
    ''' len : LEN LPARENT ID RPARENT SEMICOLON '''
    p[0]=NonTerminalNode("LenF",[TerminalNode("Len","LEN"),TerminalNode("Lparent","LPARENT"),TerminalNode("Id",p[3]),TerminalNode("Rparent","RPARENT")])
    print("len")

def p_neg(p):
    ''' neg :  identifier DOT NEG SEMICOLON '''
    p[0]=NonTerminalNode("NegF",[p[1],TerminalNode("Dot","DOT"),TerminalNode("Neg","NEG")])
    print("neg")

def p_tf(p):
    '''t_f : identifier DOT tf SEMICOLON '''
    p[0]=NonTerminalNode("TF",[p[1],TerminalNode("Dot","DOT"),p[3]])
    print("tf_function")

def p_blink(p):
    ''' blink : BLINK LPARENT b_content RPARENT SEMICOLON '''
    p[0]=NonTerminalNode("BlinkF",[TerminalNode("Blink","BLINK"),TerminalNode("Lparent","LPARENT"),p[3],TerminalNode("Rparent","RPARENT")])
    print("blink")

def p_delay(p):
    '''delay : DELAY LPARENT d_content RPARENT SEMICOLON '''
    p[0]=NonTerminalNode("DelayF",[TerminalNode("Delay","DELAY"),TerminalNode("Lparent","LPARENT"),p[3],TerminalNode("Rparent","RPARENT")])
    print("delay")

def p_shapeArg0(p):
    '''shape_arg : SHAPEF'''
    p[0]=NonTerminalNode("ShapeArg0",[TerminalNode("ShapeF","SHAPEF")])
    print("shapeArg0")

def p_shapeArg1(p):
    '''shape_arg : SHAPEC'''
    p[0]=NonTerminalNode("ShapeArg1",[TerminalNode("ShapeC","SHAPEC")])
    print("shapeArg1")

def p_shapeArg2(p):
    '''shape_arg : SHAPEA'''
    p[0]=NonTerminalNode("ShapeArg2",[TerminalNode("ShapeA","SHAPEA")])
    print("shapeArg2")

def p_shape(p):
    '''shape : identifier DOT shape_arg SEMICOLON '''
    p[0]=NonTerminalNode("Shape",[p[1],TerminalNode("Dot","DOT"),p[3]])
    print("shape")

def p_delete(p):
    '''delete : identifier DOT DELETE LPARENT indice COMMA INT RPARENT SEMICOLON '''
    p[0]=NonTerminalNode("DeleteF",[p[1],TerminalNode("Dot","DOT"),TerminalNode("Delete","DELETE"),TerminalNode("Lparent","LPARENT"),p[5],TerminalNode("Comma","COMMA"),TerminalNode("Int",p[7]),TerminalNode("Rparent","RPARENT")])
    print("delete_mat")

def p_call(p):
    '''call : CALL proc_dec SEMICOLON'''
    p[0]=NonTerminalNode("CallF",[TerminalNode("Call","CALL"),p[2]])
    print("call")





##########---CICLOS---##########
def p_cycle(p):
    '''cycle : for'''
    p[0]=NonTerminalNode("Cycle",[p[1]])
    print("cycle0")

def p_for(p):
    '''for : FOR ID IN iterable step LCORCH alt_block RCORCH SEMICOLON '''
    p[0]=NonTerminalNode("ForC",[TerminalNode("For","FOR"),TerminalNode("Id",p[2]),TerminalNode("In","IN"),p[4],p[5],TerminalNode("Lcorch","LCORCH"),p[7],TerminalNode("Rcorch","RCORCH")])
    print("for")

def p_step(p):
    '''step : STEP INT'''
    p[0]=NonTerminalNode("StepF",[TerminalNode("Step","STEP"),TerminalNode("Int",p[2])])
    print("step0")

def p_stepEmp(p):
    '''step : empty'''
    p[0]=Null()
    print("stepEmpt")





##########---BIFURCACIONES---##########
def p_statement(p):
    '''statement : IF LPARENT iterable relation bif_value RPARENT LCORCH alt_block RCORCH SEMICOLON opt_statement '''
    p[0]=NonTerminalNode("Statement",[TerminalNode("If","IF"),TerminalNode("Lparent","LPARENT"),p[3],p[4],p[5],TerminalNode("Rparent","RPARENT"),TerminalNode("Lcorch","LCORCH"),p[8],TerminalNode("Rcorch","RCORCH"),p[11]])
    print("statement")

def p_optStatment(p):
    '''opt_statement : ELSE LCORCH alt_block RCORCH SEMICOLON '''
    p[0]=NonTerminalNode("OptStatement",[TerminalNode("Else","ELSE"),TerminalNode("Lcorch","LCORCH"),p[3],TerminalNode("Rcorch","RCORCH")])
    print("optStatement")

def p_EmptyOptStatment(p):
    '''opt_statement : empty '''
    p[0]=Null()
    print("EmptyOptStatement")





##########---PROCEDIMIENTOS---##########
def p_procedure(p):
    '''procedure : PROCEDURE proc_dec LCORCH body RCORCH SEMICOLON '''
    p[0]=NonTerminalNode("ProcedureP",[TerminalNode("Procedure","PROCEDURE"),p[2],TerminalNode("Lcorch","LCORCH"),p[4],TerminalNode("Rcorch","RCORCH")])
    print("procedure")
def p_procDec(p):
    '''proc_dec : proc_name LPARENT parameter RPARENT'''
    p[0]=NonTerminalNode("ProcDec",[p[1],TerminalNode("Lparent","LPARENT"),p[3],TerminalNode("Rparent","RPARENT")])
    print("proc_dec")

def p_procName(p):
    '''proc_name : ID'''
    p[0]=NonTerminalNode("ProcName",[TerminalNode("Id",p[1])])
    print("proc_name")

def p_parameter0(p):
    '''parameter : proc_param'''
    p[0]=NonTerminalNode("Parameter0",[p[1]])
    print("parameter0")

def p_parameter1(p):
    '''parameter : proc_param COMMA parameter'''
    p[0]=NonTerminalNode("Parameter1",[p[1],TerminalNode("Comma","COMMA"),p[3]])
    print("parameter1")

def p_emptyParameter(p):
    '''parameter : empty'''
    p[0]=Null()
    print("emptyParameter")

def p_procParam(p):
    '''proc_param : ID'''
    p[0]=NonTerminalNode("ProcParam",[TerminalNode("Id",p[1])])
    print("proc_param")

def p_body(p):
    '''body : BEGIN alt_block END SEMICOLON '''
    p[0]=NonTerminalNode("Body",[TerminalNode("Begin","BEGIN"),p[2],TerminalNode("End","END")])
    print("proc_body")

def p_mainProcedure(p):
    '''main_proc : MAIN LPARENT RPARENT LCORCH main_body RCORCH SEMICOLON block'''
    p[0]=NonTerminalNode("MainProc",[TerminalNode("Main","MAIN"),TerminalNode("Lparent","LPARENT"),TerminalNode("Rparent","RPARENT"),TerminalNode("Lcorch","LCORCH"),p[5],TerminalNode("Rcorch","RCORCH"),p[8]])
    print("mainProcedure")

def p_mainBody(p):
    '''main_body : BEGIN main_block END SEMICOLON'''
    p[0]=NonTerminalNode("MainBody",[TerminalNode("Begin","BEGIN"),p[2],TerminalNode("End","END")])
    print("main_body")

def p_mainBlock(p):
    '''main_block : instruction main_block'''
    p[0]=NonTerminalNode("MainBlock",[p[1],p[2]])
    print("main_block")


def p_EmptyMainblok(p):
    '''main_block : empty'''
    p[0]=Null()
    print("EmptyMainblok")





##########---OPERACIONES ARITMETICAS---##########
def p_arithmetic0(p):
    ''' arithmetic : term'''
    p[0]=NonTerminalNode("Arithmetic0",[p[1]])
    print("arithmetic0")
def p_arithmetic1(p):
    '''arithmetic : adding_operator term '''
    p[0]=NonTerminalNode("Arithmetic1",[p[1],p[2]])
    print("arithmetic1")

def p_arithmetic2(p):
    '''arithmetic : arithmetic adding_operator term'''
    p[0]=NonTerminalNode("Arithmetic2",[p[1],p[2],p[3]])
    print("arithmetic2")





##########---TERMINOS---##########
def p_term0(p):
    '''term : factor'''
    p[0]=NonTerminalNode("Term0",[p[1]])
    print("term0")

def p_term1(p):
    '''term : term multiplying_operator factor'''
    p[0]=NonTerminalNode("Term1",[p[1],p[2],p[3]])
    print("term1")





##########---FACTORES---##########
def p_factor0(p):
    '''factor : INT'''
    p[0]=NonTerminalNode("Factor0",[TerminalNode("Int",p[1])])
    print("factor0")

def p_factor1(p):
    '''factor : ID'''
    p[0]=NonTerminalNode("Factor1",[TerminalNode("Id",p[1])])
    print("factor1")

def p_factor2(p):
    '''factor : LPARENT arithmetic RPARENT'''
    p[0]=NonTerminalNode("Factor2",[TerminalNode("Lparent","LPARENT"),p[2],TerminalNode("Rparent","RPARENT")])
    print("factor2")





##########---CONSTANTES DE CONFIGURACION---##########
def p_const0(p):
    '''const : TIMER ASSIGN INT SEMICOLON'''
    p[0]=NonTerminalNode("Const0",[TerminalNode("Timer","TIMER"),TerminalNode("Assign","ASSIGN"),TerminalNode("Int",p[3])])
    print("timer_const")

def p_const1(p):
    '''const : RANGOTIMER ASSIGN time_mes SEMICOLON'''
    p[0]=NonTerminalNode("Const1",[TerminalNode("RangoTimer","RANGOTIMER"),TerminalNode("Assign","ASSIGN"),p[3]])
    print("rng_const")

def p_const2(p):
    '''const : dimension ASSIGN INT SEMICOLON'''
    p[0]=NonTerminalNode("Const2",[p[1],TerminalNode("Assign","ASSIGN"),TerminalNode("Int",p[3])])
    print("dim_const")

def p_const3(p):
    '''const : CUBO ASSIGN INT SEMICOLON'''
    p[0]=NonTerminalNode("Const3",[TerminalNode("Cubo","CUBE"),TerminalNode("Assign","ASSIGN"),TerminalNode("Int",p[3])])
    print("cube_const")





##########---CONTENIDO DE ASIGNACIONES---##########
def p_Acont0(p):
    '''a_content : value'''
    p[0]=NonTerminalNode("Acont0",[p[1]])
    print("a_content0")

def p_Acont1(p):
    '''a_content : arithmetic'''
    p[0]=NonTerminalNode("Acont1",[p[1]])
    print("a_content1")

def p_Acont2(p):
    '''a_content : list'''
    p[0]=NonTerminalNode("Acont2",[p[1]])
    print("a_content2")

def p_Acont3(p):
    '''a_content : mat'''
    p[0]=NonTerminalNode("Acont3",[p[1]])
    print("a_content3")

def p_Acont4(p):
    '''a_content : 3dmat'''
    p[0]=NonTerminalNode("Acont4",[p[1]])
    print("a_content4")

def p_Acont5(p):
    '''a_content : consult'''
    p[0]=NonTerminalNode("Acont5",[p[1]])
    print("a_content5")




##########---CONTENIDO DE FUNCIONES---##########
def p_Fcont0(p):
    '''b_content : list_consult COMMA INT COMMA time_mes COMMA value'''
    p[0]=NonTerminalNode("Fcont0",[p[1],TerminalNode("Comma","COMMA"),TerminalNode("Int",p[3]),TerminalNode("Comma","COMMA"),p[5],TerminalNode("Comma","COMMA"),p[7]])
    print("blink_content0")

def p_Fcont1(p):
    '''b_content : list_consult COMMA value'''
    p[0]=NonTerminalNode("Fcont1",[p[1],TerminalNode("Comma","COMMA"),p[3]])
    print("blink_content1")

def p_Fcont2(p):
    '''d_content : empty'''
    p[0]=Null()
    print("delayEmp")

def p_Fcont3(p):
    '''d_content : INT COMMA time_mes'''
    p[0]=NonTerminalNode("Fcont3",[TerminalNode("Int",p[1]),TerminalNode("Comma","COMMA"),p[3]])
    print("delay_content0")

def p_Fcont4(p):
    '''tf : T'''
    p[0]=NonTerminalNode("Fcont4",[TerminalNode("T","T")])
    print("t_content")

def p_Fcont5(p):
    '''tf : F'''
    p[0]=NonTerminalNode("Fcont5",[TerminalNode("F","F")])
    print("f_content")

def p_Fcont6(p):
    '''i_content : INT COMMA value'''
    p[0]=NonTerminalNode("Fcont6",[TerminalNode("Int",p[1]),TerminalNode("Comma","COMMA"),p[3]])
    print("i_content0")

def p_Fcont7(p):
    '''i_content : list COMMA INT i_ind'''
    p[0]=NonTerminalNode("Fcont7",[p[1],TerminalNode("Comma","COMMA"),TerminalNode("Int",p[3]),p[4]])
    print("i_content1")





##########---LISTAS Y MATRICES---##########
def p_list(p):
    '''list : PARENTCL list_term PARENTCR'''
    p[0]=NonTerminalNode("List",[TerminalNode("Parentcl","PARENTCL"),p[2],TerminalNode("Parentcr","PARENTCR")])
    print("list")

def p_EmptyList(p):
    '''list : PARENTCL empty PARENTCR'''
    p[0]=NonTerminalNode("EmptyList",[TerminalNode("Parentcl","PARENTCL"),Null(),TerminalNode("Parentcr","PARENTCR")])
    print("lEmpt")

def p_listT0(p):
    '''list_term : list_value COMMA list_term'''
    p[0]=NonTerminalNode("ListT0",[p[1],TerminalNode("Comma","COMMA"),p[3]])
    print("list_term0")

def p_listT1(p):
    '''list_term : list_value'''
    p[0]=NonTerminalNode("ListT1",[p[1]])
    print("list_term1")

def p_listV(p):
    '''list_value : value'''
    p[0]=NonTerminalNode("ListV",[p[1]])
    print("list_value")

def p_mat(p):
    '''mat : PARENTCL mat_term PARENTCR'''
    p[0]=NonTerminalNode("Mat",[TerminalNode("Parentcl","PARENTCL"),p[2],TerminalNode("Parentcr","PARENTCR")])
    print("mat")

def p_matT0(p):
    '''mat_term : mat_value COMMA mat_term'''
    p[0]=NonTerminalNode("MatT0",[p[1],TerminalNode("Comma","COMMA"),p[3]])
    print("mat_term0")

def p_matT1(p):
    '''mat_term : mat_value'''
    p[0]=NonTerminalNode("MatT1",[p[1]])
    print("mat_term1")

def p_matV(p):
    '''mat_value : list'''
    p[0]=NonTerminalNode("MatV",[p[1]])
    print("mat_value")

def p_3dmat(p):
    '''3dmat : PARENTCL 3dmat_term PARENTCR'''
    p[0]=NonTerminalNode("3dMat",[TerminalNode("Parentcl","PARENTCL"),p[2],TerminalNode("Parentcr","PARENTCR")])
    print("3dmat")

def p_3dmatT0(p):
    '''3dmat_term : 3dmat_value COMMA 3dmat_term'''
    p[0]=NonTerminalNode("ThreeDMatT0",[p[1],TerminalNode("Comma","COMMA"),p[3]])
    print("3dmat_term0")

def p_3dmatT1(p):
    '''3dmat_term : 3dmat_value'''
    p[0]=NonTerminalNode("ThreeDMatT1",[p[1]])
    print("3dmat_term1")

def p_3dmatV(p):
    '''3dmat_value : mat'''
    p[0]=NonTerminalNode("ThreeDMatV",[p[1]])
    print("3dmat_value")

def p_consult0(p):
    '''consult : list_consult '''
    p[0]=NonTerminalNode("Consult0",[p[1]])
    print("consult0")

def p_consult1(p):
    '''consult : mat_consult '''
    p[0]=NonTerminalNode("Consult1",[p[1]])
    print("consult1")

def p_consult2(p):
    '''consult : 3dmat_consult'''
    p[0]=NonTerminalNode("Consult2",[p[1]])
    print("consult2")

def p_Listconsult(p):
    '''list_consult : ID list_consultT '''
    p[0]=NonTerminalNode("ListConsult",[TerminalNode("Id",p[1]),p[2]])
    print("listConslt0")

def p_ListconsultT0(p):
    '''list_consultT : PARENTCL indice PARENTCR'''
    p[0]=NonTerminalNode("ListConsultT0",[TerminalNode("Parentcl","PARENTCL"),p[2],TerminalNode("Parentcr","PARENTCR")])
    print("LstConsltT0")

def p_LstconsultT1(p):
    '''list_consultT : PARENTCL indice TP indice PARENTCR '''
    p[0]=NonTerminalNode("ListConsultT1",[TerminalNode("Parentcl","PARENTCL"),p[2],TerminalNode("Tp","TP"),p[4],TerminalNode("Parentcr","PARENTCR")])
    print("LstConsltT1")

def p_Matconsult(p):
    '''mat_consult : ID mat_consultT '''
    p[0]=NonTerminalNode("MatConsult",[TerminalNode("Id",p[1]),p[2]])
    print("matConslt0")

def p_MatconsultT0(p):
    '''mat_consultT : PARENTCL indice COMMA indice PARENTCR'''
    p[0]=NonTerminalNode("MatConsultT0",[TerminalNode("Parentcl","PARENTCL"),p[2],TerminalNode("Comma","COMMA"),p[4],TerminalNode("Parentcr","PARENTCR")])
    print("matConsltT0")

def p_MatconsultT1(p):
    '''mat_consultT : PARENTCL TP COMMA indice PARENTCR '''
    p[0]=NonTerminalNode("MatConsultT1",[TerminalNode("Parentcl","PARENTCL"),TerminalNode("Tp","TP"),TerminalNode("Comma","COMMA"),p[4],TerminalNode("Parentcr","PARENTCR")])
    print("matConsltT1")

def p_MatconsultT2(p):
    '''mat_consultT : PARENTCL TP PARENTCR list_consultT '''
    p[0]=NonTerminalNode("MatConsultT2",[TerminalNode("Parentcl","PARENTCL"),TerminalNode("Tp","TP"),TerminalNode("Parentcr","PARENTCR"),p[4]])
    print("matConsltT2")

def p_MatconsultT3(p):
    '''mat_consultT : PARENTCL indice PARENTCR list_consultT'''
    p[0]=NonTerminalNode("MatConsultT3",[TerminalNode("Parentcl","PARENTCL"),p[2],TerminalNode("Parentcr","PARENTCR"),p[4]])
    print("matConsltT3")

def p_3dMatconsult(p):
    '''3dmat_consult : ID 3dmat_consultT'''
    p[0]=NonTerminalNode("ThreeDMatConsult",[TerminalNode("Id",p[1]),p[2]])
    print("3dmatConslt")

def p_3dMatconsultT0(p):
    '''3dmat_consultT : PARENTCL indice COMMA indice COMMA indice PARENTCR'''
    p[0]=NonTerminalNode("ThreeDMatConsultT0",[TerminalNode("Parentcl","PARENTCL"),p[2],TerminalNode("Comma","COMMA"),p[4],TerminalNode("Comma","COMMA"),p[6],TerminalNode("Parentcr","PARENTCR")])
    print("3dmatConsltT0")

def p_3dMatconsultT1(p):
    '''3dmat_consultT : PARENTCL indice PARENTCR mat_consultT'''
    p[0]=NonTerminalNode("ThreeDMatConsultT1",[TerminalNode("Parentcl","PARENTCL"),p[2],TerminalNode("Parentcr","PARENTCR"),p[4]])
    print("3dmatConsltT1")



##########---INDICES---##########
def p_indice0(p):
    '''indice : INT'''
    p[0]=NonTerminalNode("Indice0",[TerminalNode("Int",p[1])])
    print("indice0")

def p_indice1(p):
    '''indice : ID'''
    p[0]=NonTerminalNode("Indice1",[TerminalNode("Id",p[1])])
    print("indice1")

def p_Insind0(p):
    '''i_ind : COMMA INT'''
    p[0]=NonTerminalNode("Insind0",[TerminalNode("Comma","COMMA"),TerminalNode("Int",p[1])])
    print("insInd0")

def p_InsindEmp(p):
    '''i_ind : empty'''
    p[0]=Null()
    print("insIndEmp")



##########---DIMENSIONES---##########
def p_dim0(p):
    '''dimension : DIMFILAS'''
    p[0]=NonTerminalNode("Dim0",[TerminalNode("Dimfilas","DIMFILAS")])
    print("dim_filas")

def p_dim1(p):
    '''dimension : DIMCOLUMNAS'''
    p[0]=NonTerminalNode("Dim1",[TerminalNode("Dimcolumnas","DIMCOLUMNAS")])
    print("dim_columnas")





##########---MEDIDAS DE TIEMPO---##########
def p_timeM0(p):
    '''time_mes : QUOTES MIL QUOTES'''
    p[0]=NonTerminalNode("TimeM0",[TerminalNode("Mil","MIL")])
    print("timeM0")

def p_timeM1(p):
    '''time_mes : QUOTES MIN QUOTES'''
    p[0]=NonTerminalNode("TimeM1",[TerminalNode("Min","MIN")])
    print("timeM1")

def p_timeM2(p):
    '''time_mes : QUOTES SEG QUOTES'''
    p[0]=NonTerminalNode("TimeM2",[TerminalNode("Seg","SEG")])
    print("timeM2")





##########---OPERADORES---##########
def p_addingOp0(p):
    '''adding_operator : PLUS'''
    p[0]=NonTerminalNode("AddingOp0",[TerminalNode("Plus","PLUS")])
    print("Plus")

def p_addingOp1(p):
    '''adding_operator : MINUS'''
    p[0]=NonTerminalNode("AddingOp1",[TerminalNode("Minus","MINUS")])
    print("Minus")

def p_multiplyingOp0(p):
    '''multiplying_operator : TIMES'''
    p[0]=NonTerminalNode("MultiplyingOp0",[TerminalNode("Times","TIMES")])
    print("Times")
def p_multiplyingOp1(p):
    '''multiplying_operator : EXP'''
    p[0]=NonTerminalNode("MultiplyingOp1",[TerminalNode("Exp","EXP")])
    print("Exponencial")

def p_multiplyingOp2(p):
    '''multiplying_operator : DIVIDE'''
    p[0]=NonTerminalNode("MultiplyingOp2",[TerminalNode("Divide","DIVIDE")])
    print("Divide")

def p_multiplyingOp3(p):
    '''multiplying_operator : DIVENT'''
    p[0]=NonTerminalNode("MultiplyingOp3",[TerminalNode("Divent","DIVENT")])
    print("Divent")

def p_multiplyingOp4(p):
    '''multiplying_operator : MOD'''
    p[0]=NonTerminalNode("MultiplyingOp4",[TerminalNode("Mod","MOD")])
    print("Module")





##########---VALORES---##########
def p_value0(p):
    '''value : FALSE'''
    p[0]=NonTerminalNode("Value0",[TerminalNode("FalseV","FALSE")])
    print("value0")

def p_value1(p):
    '''value : TRUE'''
    p[0]=NonTerminalNode("Value1",[TerminalNode("TrueV","TRUE")])
    print("value1")

def p_Bifvalue0(p):
    '''bif_value : value'''
    p[0]=NonTerminalNode("BifValue0",[p[1]])
    print("bif_Value0")

def p_Bifvalue1(p):
    '''bif_value : arithmetic'''
    p[0]=NonTerminalNode("BifValue1",[p[1]])
    print("bif_Value1")





##########---RELACIONES---##########
def p_relation0(p):
    '''relation : ASSIGN'''
    p[0]=NonTerminalNode("Relation0",[TerminalNode("Assign","ASSIGN")])
    print ("relation 0")

def p_relation1(p):
    '''relation : NE'''
    p[0]=NonTerminalNode("Relation1",[TerminalNode("Ne","NE")])
    print ("relation 1")

def p_relation2(p):
    '''relation : LT'''
    p[0]=NonTerminalNode("Relation2",[TerminalNode("Lt","LT")])
    print ("relation 2")

def p_relation3(p):
    '''relation : GT'''
    p[0]=NonTerminalNode("Relation3",[TerminalNode("Gt","GT")])
    print ("relation 3")

def p_relation4(p):
    '''relation : LTE'''
    p[0]=NonTerminalNode("Relation0",[TerminalNode("Lte","LTE")])
    print ("relation 4")

def p_relation5(p):
    '''relation : GTE'''
    p[0]=NonTerminalNode("Relation5",[TerminalNode("Gte","GTE")])
    print("relation 5")

def p_relation6(p):
    '''relation : COMPARE'''
    p[0]=NonTerminalNode("Relation6",[TerminalNode("Compare","COMPARE")])
    print ("relation 6")



##########---IDENTIFICADORES---##########
def p_identifier0(p):
    '''identifier : ID'''
    p[0]=NonTerminalNode("Identifier0",[TerminalNode("Id",p[1])])
    print("identifier0")

def p_identifier1(p):
    '''identifier : consult'''
    p[0]=NonTerminalNode("Identifier1",[p[1]])
    print("identifier1")





##########---ITERABLES---##########
def p_iterable0(p):
    '''iterable : identifier'''
    p[0]=NonTerminalNode("Iterable0",[p[1]])
    print("iterable0")

def p_iterable1(p):
    '''iterable : INT'''
    p[0]=NonTerminalNode("Iterable1",TerminalNode("Int",p[1]))
    print("iterable1")





##########---VARIOS---##########
def p_empty(p):
    'empty : '
    pass

def translate(result):
	graphFile = open('graphviztree.vz','w')
	graphFile.write(result.translate())
	graphFile.close()




##########---ERRORES---##########
def p_error(p):
    if (p):
        print(colorama.Fore.RED + "SYNTACTIC ERROR: line:", p.lexer.lineno, "position:", p.lexpos, "Syntax error:", p.value, colorama.Fore.RESET)
    else:
        print(colorama.Fore.RED + "SYNTACTIC ERROR: Unknown syntax error" + colorama.Fore.RESET)


test = 'C:/Users/dcama/Desktop/Compilador/Test'
fp = codecs.open(test, "r", "utf-8")
chain = fp.read()
parser = yacc.yacc()
tv(chain)
result = parser.parse(chain)
translate(result)
