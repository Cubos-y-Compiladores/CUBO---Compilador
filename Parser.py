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
    p[0]=Program("Program",p[1],p[2])
    print("program")

def p_constB(p):
    '''const_block : const const const const const block'''
    p[0]=ConstB("ConstB",p[1],p[2],p[3],p[4],p[5],p[6])
    print("const_block")

def p_block0(p):
    '''block : procedure block'''
    p[0]=Block0("Block0",p[1],p[2])
    print("block0")

def p_block1(p):
    '''block : global block'''
    p[0]=Block1("Block1",p[1],p[2])
    print("block1")

def p_blockEmp(p):
    '''block : empty'''
    p[0]=Null()
    print("blockEmp")





##########---BLOQUES ALTERNATIVOS---##########
def p_altBlock(p):
    '''alt_block : alt_content alt_block'''
    p[0]= AltBlock("AltBlock",p[1],p[2])
    print("alt_block")

def p_emptyaltBlock(p):
    '''alt_block : empty'''
    p[0]=Null()
    print("emptyaltBlock")

def p_altContent0(p):
    '''alt_content : instruction'''
    p[0]=AltContent0("AltContent0",p[1])
    print("altCont0")

def p_altContent1(p):
    '''alt_content : assignment'''
    p[0]=AltContent1("AltContent1",p[1])
    print("altCont1")





##########---INSTRUCCIONES---##########
def p_instruction0(p):
    ''' instruction : function '''
    p[0]=Instruction0("Instruction0",p[1])
    print("instruction0")

def p_instruction1(p):
    ''' instruction : consult SEMICOLON '''
    p[0]=Instruction1("Instruction1",p[1])
    print("instruction1")

def p_instruction2(p):
    '''instruction : cycle '''
    p[0]=Instruction2("Instruction2",p[1])
    print("instruction2")

def p_instruction3(p):
    '''instruction : statement '''
    p[0]=Instruction3("Instruction3",p[1])
    print("instruction3")





##########---ASIGNACIONES GLOBALES---##########
def p_globalAssignment(p):
    '''global : GLOBAL assignment '''
    p[0]=GlobalAssignment("GlobalAssignment",Global(p[1]),p[2])
    print("globalAssignment")





##########---ASIGNACIONES---##########
def p_simpleAssignment(p):
    '''assignment : identifier ASSIGN a_content SEMICOLON '''
    p[0]=SimpleAssignment("SimpleAssignment",p[1],Assign(p[2]),p[3])
    print("simpleAssignment")

def p_doubleAssignment(p):
    '''assignment : identifier COMMA identifier ASSIGN a_content COMMA a_content SEMICOLON '''
    p[0]=DoubleAssignment("DoubleAssignment",p[1],Comma(p[2]),p[3],Assign(p[4]),p[5],Comma(p[6]),p[7])
    print("doubleAssignment")





##########---FUNCIONES---##########
def p_function0(p):
    '''function : type '''
    p[0]=Function0("Function0",p[1])
    print("function0")

def p_function1(p):
    '''function : insert'''
    p[0]=Function1("Function1",p[1])
    print("function1")

def p_function2(p):
    '''function : del'''
    p[0]=Function2("Function2",p[1])
    print("function2")

def p_function3(p):
    '''function : len'''
    p[0]=Function3("Function3",p[1])
    print("function3")

def p_function4(p):
    '''function : neg'''
    p[0]=Function4("Function4",p[1])
    print("function4")

def p_function5(p):
    '''function : t_f'''
    p[0]=Function5("Function5",p[1])
    print("function5")

def p_function6(p):
    '''function : blink'''
    p[0]=Function6("Function6",p[1])
    print("function6")

def p_function7(p):
    '''function : delay'''
    p[0]=Function7("Function7",p[1])
    print("function7")

def p_function8(p):
    '''function : shape'''
    p[0]=Function8("Function8",p[1])
    print("function8")

def p_function9(p):
    '''function : delete'''
    p[0]=Function9("Function9",p[1])
    print("function9")

def p_function10(p):
    '''function : call'''
    p[0]=Function10("Function10",p[1])
    print("function10")

def p_type(p):
    '''type : TYPE LPARENT identifier RPARENT SEMICOLON '''
    p[0]=TypeF("TypeF",Type(p[1]),Lparent(p[2]),p[3],Rparent(p[4]))
    print("type")

def p_range(p):
    '''a_content : RANGE LPARENT INT COMMA value RPARENT'''
    p[0]=RangeF("RangeF",Range(p[1]),Lparent(p[2]),Int(p[3]),Comma(p[4]),p[5],Rparent(p[6]))
    print("range")

def p_insert(p):
    '''insert : identifier DOT INSERT LPARENT i_content RPARENT SEMICOLON '''
    p[0]=InsertF("InsertF",p[1],Dot(p[2]),Insert(p[3]),Lparent(p[4]),p[5],Rparent(p[6]))
    print("insert")

def p_del(p):
    ''' del : identifier DOT DEL LPARENT INT RPARENT SEMICOLON '''
    p[0]=DelF("DelF",p[1],Dot(p[2]),Del(p[3]),Lparent(p[4]),Int(p[5]),Rparent(p[6]))
    print("delete_list")

def p_len(p):
    ''' len : LEN LPARENT ID RPARENT SEMICOLON '''
    p[0]=LenF("LenF",Len(p[1]),Lparent(p[2]),Id(p[3]),Rparent(p[4]))
    print("len")

def p_neg(p):
    ''' neg :  identifier DOT NEG SEMICOLON '''
    p[0]=NegF("NegF",p[1],Dot(p[2]),Neg(p[3]))
    print("neg")

def p_tf(p):
    '''t_f : identifier DOT tf SEMICOLON '''
    p[0]=TF("TF",p[1],Dot(p[2]),p[3])
    print("tf_function")

def p_blink(p):
    ''' blink : BLINK LPARENT b_content RPARENT SEMICOLON '''
    p[0]=BlinkF("BlinkF",Blink(p[1]),Lparent(p[2]),p[3],Rparent(p[4]))
    print("blink")

def p_delay(p):
    '''delay : DELAY LPARENT d_content RPARENT SEMICOLON '''
    p[0]=DelayF("DelayF",Delay(p[1]),Lparent(p[2]),p[3],Rparent(p[4]))
    print("delay")

def p_shapeArg0(p):
    '''shape_arg : SHAPEF'''
    p[0]=ShapeArg0("ShapeArg0",ShapeF(p[1]))
    print("shapeArg0")

def p_shapeArg1(p):
    '''shape_arg : SHAPEC'''
    p[0]=ShapeArg1("ShapeArg1",ShapeC(p[1]))
    print("shapeArg1")

def p_shapeArg2(p):
    '''shape_arg : SHAPEA'''
    p[0]=ShapeArg2("ShapeArg2",ShapeA(p[1]))
    print("shapeArg2")

def p_shape(p):
    '''shape : identifier DOT shape_arg SEMICOLON '''
    p[0]=Shape("Shape",p[1],Dot(p[2]),p[3])
    print("shape")

def p_delete(p):
    '''delete : identifier DOT DELETE LPARENT indice COMMA INT RPARENT SEMICOLON '''
    p[0]=DeleteF("DeleteF",p[1],Dot(p[2]),Delete(p[3]),Lparent(p[4]),p[5],Comma(p[6]),Int(p[7]),Rparent(p[8]))
    print("delete_mat")

def p_call(p):
    '''call : CALL proc_dec SEMICOLON'''
    p[0]=CallF("CallF",Call(p[1]),p[2])
    print("call")





##########---CICLOS---##########
def p_cycle(p):
    '''cycle : for'''
    p[0]=Cycle("Cycle",p[1])
    print("cycle0")

def p_for(p):
    '''for : FOR ID IN iterable step LCORCH alt_block RCORCH SEMICOLON '''
    p[0]=ForC("ForC",For(p[1]),Id(p[2]),In(p[3]),p[4],p[5],Lcorch(p[6]),p[7],Rcorch(p[8]))
    print("for")

def p_step(p):
    '''step : STEP INT'''
    p[0]=StepF("StepF",Step(p[1]),Int(p[2]))
    print("step0")

def p_stepEmp(p):
    '''step : empty'''
    p[0]=Null()
    print("stepEmpt")





##########---BIFURCACIONES---##########
def p_statement(p):
    '''statement : IF LPARENT iterable relation bif_value RPARENT LCORCH alt_block RCORCH SEMICOLON opt_statement '''
    p[0]=Statement("Statement",If(p[1]),Lparent(p[2]),p[3],p[4],p[5],Rparent(p[6]),Lcorch(p[7]),p[8],Rcorch(p[9]),p[11])
    print("statement")

def p_optStatment(p):
    '''opt_statement : ELSE LCORCH alt_block RCORCH SEMICOLON '''
    p[0]=OptStatement("OptStatement",Else(p[1]),Lcorch(p[2]),p[3],Rcorch(p[4]))
    print("optStatement")

def p_EmptyOptStatment(p):
    '''opt_statement : empty '''
    p[0]=Null()
    print("EmptyOptStatement")





##########---PROCEDIMIENTOS---##########
def p_procedure(p):
    '''procedure : PROCEDURE proc_dec LCORCH body RCORCH SEMICOLON '''
    p[0]=ProcedureP("ProcedureP",Procedure(p[1]),p[2],Lcorch(p[3]),p[4],Rcorch(p[5]))
    print("procedure")
def p_procDec(p):
    '''proc_dec : proc_name LPARENT parameter RPARENT'''
    p[0]=ProcDec("ProcDec",p[1],Lparent(p[2]),p[3],Rparent(p[4]))
    print("proc_dec")

def p_procName(p):
    '''proc_name : ID'''
    p[0]=ProcName("ProcName",Id(p[1]))
    print("proc_name")

def p_parameter0(p):
    '''parameter : proc_param'''
    p[0]=Parameter0("Parameter0",p[1])
    print("parameter0")

def p_parameter1(p):
    '''parameter : proc_param COMMA parameter'''
    p[0]=Parameter1("Parameter1",p[1],Comma(p[2]),p[3])
    print("parameter1")

def p_emptyParameter(p):
    '''parameter : empty'''
    p[0]=Null()
    print("emptyParameter")

def p_procParam(p):
    '''proc_param : ID'''
    p[0]=ProcParam("ProcParam",Id(p[1]))
    print("proc_param")

def p_body(p):
    '''body : BEGIN alt_block END SEMICOLON '''
    p[0]=Body("Body",Begin(p[1]),p[2],End(p[3]))
    print("proc_body")

def p_mainProcedure(p):
    '''main_proc : MAIN LPARENT RPARENT LCORCH main_body RCORCH SEMICOLON block'''
    p[0]=MainProc("MainProc",Main(p[1]),Lparent(p[2]),Rparent(p[3]),Lcorch(p[4]),p[5],Rcorch(p[6]),p[8])
    print("mainProcedure")

def p_mainBody(p):
    '''main_body : BEGIN main_block END SEMICOLON'''
    p[0]=MainBody("MainBody",Begin(p[1]),p[2],End(p[3]))
    print("main_body")

def p_mainBlock(p):
    '''main_block : instruction main_block'''
    p[0]=MainBlock("MainBlock",p[1],p[2])
    print("main_block")


def p_EmptyMainblok(p):
    '''main_block : empty'''
    p[0]=Null()
    print("EmptyMainblok")





##########---OPERACIONES ARITMETICAS---##########
def p_arithmetic0(p):
    ''' arithmetic : term'''
    p[0]=Arithmetic0("Arithmetic0",p[1])
    print("arithmetic0")
def p_arithmetic1(p):
    '''arithmetic : adding_operator term '''
    p[0]=Arithmetic1("Arithmetic1",p[1],p[2])
    print("arithmetic1")

def p_arithmetic2(p):
    '''arithmetic : arithmetic adding_operator term'''
    p[0]=Arithmetic2("Arithmetic2",p[1],p[2],p[3])
    print("arithmetic2")





##########---TERMINOS---##########
def p_term0(p):
    '''term : factor'''
    p[0]=Term0("Term0",p[1])
    print("term0")

def p_term1(p):
    '''term : term multiplying_operator factor'''
    p[0]=Term1("Term1",p[1],p[2],p[3])
    print("term1")





##########---FACTORES---##########
def p_factor0(p):
    '''factor : INT'''
    p[0]=Factor0("Factor0",Int(p[1]))
    print("factor0")

def p_factor1(p):
    '''factor : ID'''
    p[0]=Factor1("Factor0",Id(p[1]))
    print("factor1")

def p_factor2(p):
    '''factor : LPARENT arithmetic RPARENT'''
    p[0]=Factor2("Factor2",Lparent(p[1]),p[2],Rparent(p[3]))
    print("factor2")





##########---CONSTANTES DE CONFIGURACION---##########
def p_const0(p):
    '''const : TIMER ASSIGN INT SEMICOLON'''
    p[0]=Const0("Const0",Timer(p[1]),Assign(p[2]),Int(p[3]))
    print("timer_const")

def p_const1(p):
    '''const : RANGOTIMER ASSIGN time_mes SEMICOLON'''
    p[0]=Const1("Const1",RangoTimer(p[1]),Assign(p[2]),p[3])
    print("rng_const")

def p_const2(p):
    '''const : dimension ASSIGN INT SEMICOLON'''
    p[0]=Const2("Const2",p[1],Assign(p[2]),Int(p[3]))
    print("dim_const")

def p_const3(p):
    '''const : CUBO ASSIGN INT SEMICOLON'''
    p[0]=Const3("Const3",Cubo(p[1]),Assign(p[2]),Int(p[3]))
    print("cube_const")





##########---CONTENIDO DE ASIGNACIONES---##########
def p_Acont0(p):
    '''a_content : value'''
    p[0]=Acont0("Acont0",p[1])
    print("a_content0")

def p_Acont1(p):
    '''a_content : arithmetic'''
    p[0]=Acont1("Acont1",p[1])
    print("a_content1")

def p_Acont2(p):
    '''a_content : list'''
    p[0]=Acont2("Acont2",p[1])
    print("a_content2")

def p_Acont3(p):
    '''a_content : mat'''
    p[0]=Acont3("Acont3",p[1])
    print("a_content3")

def p_Acont4(p):
    '''a_content : 3dmat'''
    p[0]=Acont4("Acont4",p[1])
    print("a_content4")

def p_Acont5(p):
    '''a_content : consult'''
    p[0]=Acont5("Acont5",p[1])
    print("a_content5")




##########---CONTENIDO DE FUNCIONES---##########
def p_Fcont0(p):
    '''b_content : list_consult COMMA INT COMMA time_mes COMMA value'''
    p[0]=Fcont0("Fcont0",p[1],Comma(p[2]),Int(p[3]),Comma(p[4]),p[5],Comma(p[6]),p[7])
    print("blink_content0")

def p_Fcont1(p):
    '''b_content : list_consult COMMA value'''
    p[0]=Fcont1("Fcont1",p[1],Comma(p[2]),p[3])
    print("blink_content1")

def p_Fcont2(p):
    '''d_content : empty'''
    p[0]=Null()
    print("delayEmp")

def p_Fcont3(p):
    '''d_content : INT COMMA time_mes'''
    p[0]=Fcont3("Fcont3",Int(p[1]),Comma(p[2]),p[3])
    print("delay_content0")

def p_Fcont4(p):
    '''tf : T'''
    p[0]=Fcont4("Fcont4",T(p[1]))
    print("t_content")

def p_Fcont5(p):
    '''tf : F'''
    p[0]=Fcont5("Fcont5",F(p[1]))
    print("f_content")

def p_Fcont6(p):
    '''i_content : INT COMMA value'''
    p[0]=Fcont6("Fcont6",Int(p[1]),Comma(p[2]),p[3])
    print("i_content0")

def p_Fcont7(p):
    '''i_content : list COMMA INT i_ind'''
    p[0]=Fcont7("Fcont7",p[1],Comma(p[2]),Int(p[3]),p[4])
    print("i_content1")





##########---LISTAS Y MATRICES---##########
def p_list(p):
    '''list : PARENTCL list_term PARENTCR'''
    p[0]=List("List",Parentcl(p[1]),p[2],Parentcr(p[3]))
    print("list")

def p_EmptyList(p):
    '''list : PARENTCL empty PARENTCR'''
    p[0]=EmptyList("EmptyList",Parentcl(p[1]),Null(),Parentcr(p[3]))
    print("lEmpt")

def p_listT0(p):
    '''list_term : list_value COMMA list_term'''
    p[0]=ListT0("ListT0",p[1],Comma(p[2]),p[3])
    print("list_term0")

def p_listT1(p):
    '''list_term : list_value'''
    p[0]=ListT1("ListT1",p[1])
    print("list_term1")

def p_listV(p):
    '''list_value : value'''
    p[0]=ListV("ListV",p[1])
    print("list_value")

def p_mat(p):
    '''mat : PARENTCL mat_term PARENTCR'''
    p[0]=Mat("Mat",Parentcl(p[1]),p[2],Parentcr(p[3]))
    print("mat")

def p_matT0(p):
    '''mat_term : mat_value COMMA mat_term'''
    p[0]=MatT0("MatT0",p[1],Comma(p[2]),p[3])
    print("mat_term0")

def p_matT1(p):
    '''mat_term : mat_value'''
    p[0]=MatT1("MatT1",p[1])
    print("mat_term1")

def p_matV(p):
    '''mat_value : list'''
    p[0]=MatV("MatV",p[1])
    print("mat_value")

def p_3dmat(p):
    '''3dmat : PARENTCL 3dmat_term PARENTCR'''
    p[0]=ThreeDMat("3dMat",Parentcl(p[1]),p[2],Parentcr(p[3]))
    print("3dmat")

def p_3dmatT0(p):
    '''3dmat_term : 3dmat_value COMMA 3dmat_term'''
    p[0]=ThreeDMatT0("ThreeDMatT0",p[1],Comma(p[2]),p[3])
    print("3dmat_term0")

def p_3dmatT1(p):
    '''3dmat_term : 3dmat_value'''
    p[0]=ThreeDMatT1("ThreeDMatT1",p[1])
    print("3dmat_term1")

def p_3dmatV(p):
    '''3dmat_value : mat'''
    p[0]=ThreeDMatV("ThreeDMatV",p[1])
    print("3dmat_value")

def p_consult0(p):
    '''consult : list_consult '''
    p[0]=Consult0("Consult0",p[1])
    print("consult0")

def p_consult1(p):
    '''consult : mat_consult '''
    p[0]=Consult1("Consult1",p[1])
    print("consult1")

def p_consult2(p):
    '''consult : 3dmat_consult'''
    p[0]=Consult2("Consult2",p[1])
    print("consult2")

def p_Listconsult(p):
    '''list_consult : ID list_consultT '''
    p[0]=ListConsult("ListConsult",Id(p[1]),p[2])
    print("listConslt0")

def p_ListconsultT0(p):
    '''list_consultT : PARENTCL indice PARENTCR'''
    p[0]=ListConsultT0("ListConsultT0",Parentcl(p[1]),p[2],Parentcr(p[3]))
    print("LstConsltT0")

def p_LstconsultT1(p):
    '''list_consultT : PARENTCL indice TP indice PARENTCR '''
    p[0]=ListConsultT1("ListConsultT1",Parentcl(p[1]),p[2],Tp(p[3]),p[4],Parentcr(p[5]))
    print("LstConsltT1")

def p_Matconsult(p):
    '''mat_consult : ID mat_consultT '''
    p[0]=MatConsult("MatConsult",Id(p[1]),p[2])
    print("matConslt0")

def p_MatconsultT0(p):
    '''mat_consultT : PARENTCL indice COMMA indice PARENTCR'''
    p[0]=MatConsultT0("MatConsultT0",Parentcl(p[1]),p[2],Comma(p[3]),p[4],Parentcr(p[5]))
    print("matConsltT0")

def p_MatconsultT1(p):
    '''mat_consultT : PARENTCL TP COMMA indice PARENTCR '''
    p[0]=MatConsultT1("MatConsultT1",Parentcl(p[1]),Tp(p[2]),Comma(p[3]),p[4],Parentcr(p[5]))
    print("matConsltT1")

def p_MatconsultT2(p):
    '''mat_consultT : PARENTCL TP PARENTCR list_consultT '''
    p[0]=MatConsultT2("MatConsultT2",Parentcl(p[1]),Tp(p[2]),Parentcr(p[3]),p[4])
    print("matConsltT2")

def p_MatconsultT3(p):
    '''mat_consultT : PARENTCL indice PARENTCR list_consultT'''
    p[0]=MatConsultT3("MatConsultT3",Parentcl(p[1]),p[2],Parentcr(p[3]),p[4])
    print("matConsltT3")

def p_3dMatconsult(p):
    '''3dmat_consult : ID 3dmat_consultT'''
    p[0]=ThreeDMatConsult("ThreeDMatConsult",Id(p[1]),p[2])
    print("3dmatConslt")

def p_3dMatconsultT0(p):
    '''3dmat_consultT : PARENTCL indice COMMA indice COMMA indice PARENTCR'''
    p[0]=ThreeDMatConsultT0("ThreeDMatConsultT0",Parentcl(p[1]),p[2],Comma(p[3]),p[4],Comma(p[5]),p[6],Parentcr(p[7]))
    print("3dmatConsltT0")

def p_3dMatconsultT1(p):
    '''3dmat_consultT : PARENTCL indice PARENTCR mat_consultT'''
    p[0]=ThreeDMatConsultT1("ThreeDMatConsultT1",Parentcl(p[1]),p[2],Parentcr(p[3]),p[4])
    print("3dmatConsltT1")



##########---INDICES---##########
def p_indice0(p):
    '''indice : INT'''
    p[0]=Indice0("Indice0",Int(p[1]))
    print("indice0")

def p_indice1(p):
    '''indice : ID'''
    p[0]=Indice1("Indice1",Id(p[1]))
    print("indice1")

def p_Insind0(p):
    '''i_ind : COMMA INT'''
    p[0]=Insind0("Insind0",Comma(p[1]),Int(p[2]))
    print("insInd0")

def p_InsindEmp(p):
    '''i_ind : empty'''
    p[0]=Null()
    print("insIndEmp")



##########---DIMENSIONES---##########
def p_dim0(p):
    '''dimension : DIMFILAS'''
    p[0]=Dim0("Dim0",Dimfilas(p[1]))
    print("dim_filas")

def p_dim1(p):
    '''dimension : DIMCOLUMNAS'''
    p[0]=Dim1("Dim1",Dimcolumnas(p[1]))
    print("dim_columnas")





##########---MEDIDAS DE TIEMPO---##########
def p_timeM0(p):
    '''time_mes : QUOTES MIL QUOTES'''
    p[0]=TimeM0("TimeM0",Mil(p[2]))
    print("timeM0")

def p_timeM1(p):
    '''time_mes : QUOTES MIN QUOTES'''
    p[0]=TimeM1("TimeM1",Min(p[2]))
    print("timeM1")

def p_timeM2(p):
    '''time_mes : QUOTES SEG QUOTES'''
    p[0]=TimeM2("TimeM2",Seg(p[2]))
    print("timeM2")





##########---OPERADORES---##########
def p_addingOp0(p):
    '''adding_operator : PLUS'''
    p[0]=AddingOp0("AddingOp0",Plus(p[1]))
    print("Plus")

def p_addingOp1(p):
    '''adding_operator : MINUS'''
    p[0]=AddingOp1("AddingOp1",Minus(p[1]))
    print("Minus")

def p_multiplyingOp0(p):
    '''multiplying_operator : TIMES'''
    p[0]=MultiplyingOp0("MultiplyingOp0",Times(p[1]))
    print("Times")
def p_multiplyingOp1(p):
    '''multiplying_operator : EXP'''
    p[0]=MultiplyingOp1("MultiplyingOp1",Exp(p[1]))
    print("Exponencial")

def p_multiplyingOp2(p):
    '''multiplying_operator : DIVIDE'''
    p[0]=MultiplyingOp2("MultiplyingOp2",Divide(p[1]))
    print("Divide")

def p_multiplyingOp3(p):
    '''multiplying_operator : DIVENT'''
    p[0]=MultiplyingOp3("MultiplyingOp3",Divent(p[1]))
    print("Divent")

def p_multiplyingOp4(p):
    '''multiplying_operator : MOD'''
    p[0]=MultiplyingOp4("MultiplyingOp4",Mod(p[1]))
    print("Module")





##########---VALORES---##########
def p_value0(p):
    '''value : FALSE'''
    p[0]=Value0("Value0",FalseV(p[1]))
    print("value0")

def p_value1(p):
    '''value : TRUE'''
    p[0]=Value1("Value1",TrueV(p[1]))
    print("value1")

def p_Bifvalue0(p):
    '''bif_value : value'''
    p[0]=BifValue0("BifValue0",p[1])
    print("bif_Value0")

def p_Bifvalue1(p):
    '''bif_value : arithmetic'''
    p[0]=BifValue1("BifValue1",p[1])
    print("bif_Value1")





##########---RELACIONES---##########
def p_relation0(p):
    '''relation : ASSIGN'''
    p[0]=Relation0("Relation0",Assign(p[1]))
    print ("relation 0")

def p_relation1(p):
    '''relation : NE'''
    p[0]=Relation1("Relation1",Ne(p[1]))
    print ("relation 1")

def p_relation2(p):
    '''relation : LT'''
    p[0]=Relation2("Relation2",Lt(p[1]))
    print ("relation 2")

def p_relation3(p):
    '''relation : GT'''
    p[0]=Relation3("Relation3",Gt(p[1]))
    print ("relation 3")

def p_relation4(p):
    '''relation : LTE'''
    p[0]=Relation0("Relation0",Assign(p[1]))
    print ("relation 4")

def p_relation5(p):
    '''relation : GTE'''
    p[0]=Relation5("Relation5",Gte(p[1]))
    print ("relation 5")

def p_relation6(p):
    '''relation : COMPARE'''
    p[0]=Relation0("Relation6",Compare(p[1]))
    print ("relation 6")



##########---IDENTIFICADORES---##########
def p_identifier0(p):
    '''identifier : ID'''
    p[0]=Identifier0("Identifier0",Id(p[1]))
    print("identifier0")

def p_identifier1(p):
    '''identifier : consult'''
    p[0]=Identifier1("Identifier1",p[1])
    print("identifier1")





##########---ITERABLES---##########
def p_iterable0(p):
    '''iterable : identifier'''
    p[0]=Iterable0("Iterable0",p[1])
    print("iterable0")

def p_iterable1(p):
    '''iterable : INT'''
    p[0]=Iterable1("Iterable1",Int(p[1]))
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
#tv(chain)
result = parser.parse(chain)
result.printer(" ")
translate(result)
