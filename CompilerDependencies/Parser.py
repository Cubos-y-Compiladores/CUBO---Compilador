import ply.yacc as yacc
import codecs,sys
from CompilerDependencies.Lexer import *
from CompilerDependencies.TreeGen import *
from CompilerDependencies.Semantics import *

from pip._vendor import colorama
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
    print(colorama.Fore.GREEN + "Successful compilation! Generating code...")


def p_constB(p):
    '''const_block : const const const const const block'''
    constBSem(p)
    semantics(p[6])
    p[0]=NonTerminalNode("ConstB",[p[1],p[2],p[3],p[4],p[5],p[6]])
    
def p_block0(p):
    '''block : procedure block'''
    p[0]=NonTerminalNode("Block0",[p[1],p[2]])
    

def p_block1(p):
    '''block : global block'''
    p[0]=NonTerminalNode("Block1",[p[1],p[2]])
    

def p_blockEmp(p):
    '''block : empty'''
    p[0]=Null()
   





##########---BLOQUES ALTERNATIVOS---##########
def p_altBlock(p):
    '''alt_block : alt_content alt_block'''
    p[0]= NonTerminalNode("AltBlock",[p[1],p[2]])
    

def p_emptyaltBlock(p):
    '''alt_block : empty'''
    p[0]=Null()
    

def p_altContent0(p):
    '''alt_content : instruction'''
    p[0]=NonTerminalNode("AltContent0",[p[1]])
    

def p_altContent1(p):
    '''alt_content : assignment'''
    p[0]=NonTerminalNode("AltContent1",[p[1]])
    





##########---INSTRUCCIONES---##########
def p_instruction0(p):
    ''' instruction : function '''
    p[0]=NonTerminalNode("Instruction0",[p[1]])
    

def p_instruction1(p):
    ''' instruction : consult SEMICOLON '''
    p[0]=NonTerminalNode("Instruction1",[p[1]])
    

def p_instruction2(p):
    '''instruction : cycle '''
    p[0]=NonTerminalNode("Instruction2",[p[1]])
    

def p_instruction3(p):
    '''instruction : statement '''
    p[0]=NonTerminalNode("Instruction3",[p[1]])
   





##########---ASIGNACIONES GLOBALES---##########
def p_globalAssignment(p):
    '''global : assignment '''
    p[0]=NonTerminalNode("GlobalAssignment",[p[1]])
    

def p_globalCall(p):
    '''global_call : GLOBAL global_term SEMICOLON global_call'''
    p[0]=NonTerminalNode("GlobalCall",[TerminalNode("Global","GLOBAL"),p[2],p[4]])
    

def p_EmptyGlobalCall(p):
    '''global_call : empty'''
    p[0]=Null()
  

def p_globalTerm0(p):
    '''global_term : ID COMMA global_term'''
    p[0]=NonTerminalNode("GlobalTerm0",[TerminalNode("Id",p[1]),TerminalNode("Coma","COMMA"),p[3]])
    

def p_globalTerm1(p):
    '''global_term : ID'''
    p[0]=NonTerminalNode("GlobalTerm1",[TerminalNode("Id",p[1])])
    





##########---ASIGNACIONES---##########
def p_simpleAssignment(p):
    '''assignment : identifier ASSIGN a_content SEMICOLON '''
    p[0]=NonTerminalNode("SimpleAssignment",[p[1],TerminalNode("Assign","ASSIGN"),p[3]])
    

def p_doubleAssignment(p):
    '''assignment : identifier COMMA identifier ASSIGN a_content COMMA a_content SEMICOLON '''
    p[0]=NonTerminalNode("DoubleAssignment",[p[1],TerminalNode("Comma","COMMA"),p[3],TerminalNode("Assign","ASSIGN"),p[5],TerminalNode("Comma","COMMA"),p[7]])
    




##########---FUNCIONES---##########
def p_function0(p):
    '''function : type '''
    p[0]=NonTerminalNode("Function0",[p[1]])
    

def p_function1(p):
    '''function : insert'''
    p[0]=NonTerminalNode("Function1",[p[1]])
    

def p_function2(p):
    '''function : del'''
    p[0]=NonTerminalNode("Function2",[p[1]])
   

def p_function3(p):
    '''function : len'''
    p[0]=NonTerminalNode("Function3",[p[1]])
    

def p_function4(p):
    '''function : neg'''
    p[0]=NonTerminalNode("Function4",[p[1]])
    

def p_function5(p):
    '''function : t_f'''
    p[0]=NonTerminalNode("Function5",[p[1]])
   

def p_function6(p):
    '''function : blink'''
    p[0]=NonTerminalNode("Function6",[p[1]])
   

def p_function7(p):
    '''function : delay'''
    p[0]=NonTerminalNode("Function7",[p[1]])
    

def p_function8(p):
    '''function : shape'''
    p[0]=NonTerminalNode("Function8",[p[1]])
    
def p_function9(p):
    '''function : delete'''
    p[0]=NonTerminalNode("Function9",[p[1]])
    

def p_function10(p):
    '''function : call'''
    p[0]=NonTerminalNode("Function10",[p[1]])
    
def p_type(p):
    '''type : TYPE LPARENT identifier RPARENT SEMICOLON '''
    p[0]=NonTerminalNode("TypeF",[TerminalNode("Type","TYPE"),TerminalNode("Lparent","LPARENT"),p[3],TerminalNode("Rparent","RPARENT")])
    

def p_range(p):
    '''a_content : RANGE LPARENT iterable COMMA value RPARENT'''
    p[0]=NonTerminalNode("RangeF",[TerminalNode("Range","RANGE"),TerminalNode("Lparent","LPARENT"),p[3],TerminalNode("Comma","COMMA"),p[5],TerminalNode("Rparent","RPARENT")])


def p_insert(p):
    '''insert : identifier DOT INSERT LPARENT i_content RPARENT SEMICOLON '''
    p[0]=NonTerminalNode("InsertF",[p[1],TerminalNode("Dot","DOT"),TerminalNode("Insert","INSERT"),TerminalNode("Lparent","LPARENT"),p[5],TerminalNode("Rparent","RPARENT")])
    

def p_del(p):
    ''' del : identifier DOT DEL LPARENT iterable RPARENT SEMICOLON '''
    p[0]=NonTerminalNode("DelF",[p[1],TerminalNode("Dot","DOT"),TerminalNode("Del","DEL"),TerminalNode("Lparent","LPARENT"),p[5],TerminalNode("Rparent","RPARENT")])
    

def p_len(p):
    ''' len : LEN LPARENT identifier RPARENT SEMICOLON '''
    p[0]=NonTerminalNode("LenF",[TerminalNode("Len","LEN"),TerminalNode("Lparent","LPARENT"),p[3],TerminalNode("Rparent","RPARENT")])
    

def p_neg(p):
    ''' neg :  identifier DOT NEG SEMICOLON '''
    p[0]=NonTerminalNode("NegF",[p[1],TerminalNode("Dot","DOT"),TerminalNode("Neg","NEG")])
   

def p_tf(p):
    '''t_f : identifier DOT tf SEMICOLON '''
    p[0]=NonTerminalNode("TF",[p[1],TerminalNode("Dot","DOT"),p[3]])
    

def p_blink(p):
    ''' blink : BLINK LPARENT b_content RPARENT SEMICOLON '''
    p[0]=NonTerminalNode("BlinkF",[TerminalNode("Blink","BLINK"),TerminalNode("Lparent","LPARENT"),p[3],TerminalNode("Rparent","RPARENT")])
    

def p_delay(p):
    '''delay : DELAY LPARENT d_content RPARENT SEMICOLON '''
    p[0]=NonTerminalNode("DelayF",[TerminalNode("Delay","DELAY"),TerminalNode("Lparent","LPARENT"),p[3],TerminalNode("Rparent","RPARENT")])
    

def p_shapeArg0(p):
    '''shape_arg : SHAPEF'''
    p[0]=NonTerminalNode("ShapeArg0",[TerminalNode("ShapeF","SHAPEF")])
   

def p_shapeArg1(p):
    '''shape_arg : SHAPEC'''
    p[0]=NonTerminalNode("ShapeArg1",[TerminalNode("ShapeC","SHAPEC")])
    

def p_shapeArg2(p):
    '''shape_arg : SHAPEA'''
    p[0]=NonTerminalNode("ShapeArg2",[TerminalNode("ShapeA","SHAPEA")])
    

def p_shape(p):
    '''shape : identifier DOT shape_arg SEMICOLON '''
    p[0]=NonTerminalNode("Shape",[p[1],TerminalNode("Dot","DOT"),p[3]])
    

def p_delete(p):
    '''delete : identifier DOT DELETE LPARENT indice COMMA INT RPARENT SEMICOLON '''
    p[0]=NonTerminalNode("DeleteF",[p[1],TerminalNode("Dot","DOT"),TerminalNode("Delete","DELETE"),TerminalNode("Lparent","LPARENT"),p[5],TerminalNode("Comma","COMMA"),TerminalNode("Int",p[7]),TerminalNode("Rparent","RPARENT")])
    

def p_call(p):
    '''call : CALL proc_call SEMICOLON'''
    p[0]=NonTerminalNode("CallF",[TerminalNode("Call","CALL"),p[2]])
    





##########---CICLOS---##########
def p_cycle(p):
    '''cycle : for'''
    p[0]=NonTerminalNode("Cycle",[p[1]])
    

def p_for(p):
    '''for : FOR ID IN iterable step LCORCH alt_block RCORCH SEMICOLON '''
    p[0]=NonTerminalNode("ForC",[TerminalNode("For","FOR"),TerminalNode("Id",p[2]),TerminalNode("In","IN"),p[4],p[5],TerminalNode("Lcorch","LCORCH"),p[7],TerminalNode("Rcorch","RCORCH")])
    

def p_step(p):
    '''step : STEP INT'''
    p[0]=NonTerminalNode("StepF",[TerminalNode("Step","STEP"),TerminalNode("Int",p[2])])
    

def p_stepEmp(p):
    '''step : empty'''
    p[0]=Null()
    





##########---BIFURCACIONES---##########
def p_statement(p):
    '''statement : IF LPARENT iterable relation bif_value RPARENT LCORCH alt_block RCORCH SEMICOLON opt_statement '''
    p[0]=NonTerminalNode("Statement",[TerminalNode("If","IF"),TerminalNode("Lparent","LPARENT"),p[3],p[4],p[5],TerminalNode("Rparent","RPARENT"),TerminalNode("Lcorch","LCORCH"),p[8],TerminalNode("Rcorch","RCORCH"),p[11]])
    

def p_optStatment(p):
    '''opt_statement : ELSE LCORCH alt_block RCORCH SEMICOLON '''
    p[0]=NonTerminalNode("OptStatement",[TerminalNode("Else","ELSE"),TerminalNode("Lcorch","LCORCH"),p[3],TerminalNode("Rcorch","RCORCH")])
    

def p_EmptyOptStatment(p):
    '''opt_statement : empty '''
    p[0]=Null()
    





##########---PROCEDIMIENTOS---##########
def p_procedure(p):
    '''procedure : PROCEDURE proc_dec LCORCH body RCORCH SEMICOLON '''
    p[0]=NonTerminalNode("ProcedureP",[TerminalNode("Procedure","PROCEDURE"),p[2],TerminalNode("Lcorch","LCORCH"),p[4],TerminalNode("Rcorch","RCORCH")])
    
def p_procDec(p):
    '''proc_dec : proc_name LPARENT parameter RPARENT'''
    p[0]=NonTerminalNode("ProcDec",[p[1],TerminalNode("Lparent","LPARENT"),p[3],TerminalNode("Rparent","RPARENT")])
   
def p_procCall(p):
    '''proc_call : proc_name LPARENT param RPARENT'''
    p[0]=NonTerminalNode("ProcCall",[p[1],TerminalNode("Lparent","LPARENT"),p[3],TerminalNode("Rparent","RPARENT")])

def p_procName(p):
    '''proc_name : ID'''
    p[0]=NonTerminalNode("ProcName",[TerminalNode("Id",p[1])])
   

def p_parameter0(p):
    '''parameter : proc_param'''
    p[0]=NonTerminalNode("Parameter0",[p[1]])
    

def p_parameter1(p):
    '''parameter : proc_param COMMA parameter'''
    p[0]=NonTerminalNode("Parameter1",[p[1],TerminalNode("Comma","COMMA"),p[3]])
    

def p_emptyParameter(p):
    '''parameter : empty'''
    p[0]=Null()
    

def p_procParam(p):
    '''proc_param : ID'''
    p[0]=NonTerminalNode("ProcParam",[TerminalNode("Id",p[1])])
    

def p_param0(p):
    '''param : call_param'''
    p[0]=NonTerminalNode("Param0",[p[1]])
    

def p_param1(p):
    '''param : call_param COMMA param'''
    p[0]=NonTerminalNode("Param1",[p[1],TerminalNode("Comma","COMMA"),p[3]])
    

def p_emptyParam(p):
    '''param : empty'''
    p[0]=Null()
    

def p_callParam(p):
    '''call_param : iterable'''
    p[0]=NonTerminalNode("CallParam",[p[1]])

def p_body(p):
    '''body : global_call BEGIN alt_block END SEMICOLON '''
    p[0]=NonTerminalNode("Body",[p[1],TerminalNode("Begin","BEGIN"),p[3],TerminalNode("End","END")])
    

def p_mainProcedure(p):
    '''main_proc : MAIN LPARENT RPARENT LCORCH main_body RCORCH SEMICOLON block'''
    line = len(p.stack)
    p[0]=NonTerminalNode("MainProc",[TerminalNode("Main","MAIN"),TerminalNode("Lparent","LPARENT"),TerminalNode("Rparent","RPARENT"),TerminalNode("Lcorch","LCORCH"),p[5],TerminalNode("Rcorch","RCORCH"),p[8]])
    

def p_mainBody(p):
    '''main_body : BEGIN main_block END SEMICOLON'''
    p[0]=NonTerminalNode("MainBody",[TerminalNode("Begin","BEGIN"),p[2],TerminalNode("End","END")])
    

def p_mainBlock(p):
    '''main_block : instruction main_block'''
    p[0]=NonTerminalNode("MainBlock",[p[1],p[2]])
    


def p_EmptyMainblok(p):
    '''main_block : empty'''
    p[0]=Null()
    





##########---OPERACIONES ARITMETICAS---##########
def p_arithmetic0(p):
    ''' arithmetic : term'''
    p[0]=NonTerminalNode("Arithmetic0",[p[1]])
    
def p_arithmetic1(p):
    '''arithmetic : adding_operator term '''
    p[0]=NonTerminalNode("Arithmetic1",[p[1],p[2]])
    

def p_arithmetic2(p):
    '''arithmetic : arithmetic adding_operator term'''
    p[0]=NonTerminalNode("Arithmetic2",[p[1],p[2],p[3]])
   





##########---TERMINOS---##########
def p_term0(p):
    '''term : factor'''
    p[0]=NonTerminalNode("Term0",[p[1]])
    

def p_term1(p):
    '''term : term multiplying_operator factor'''
    p[0]=NonTerminalNode("Term1",[p[1],p[2],p[3]])
    





##########---FACTORES---##########
def p_factor0(p):
    '''factor : INT'''
    p[0]=NonTerminalNode("Factor0",[TerminalNode("Int",p[1])])
    

def p_factor1(p):
    '''factor : ID'''
    p[0]=NonTerminalNode("Factor1",[TerminalNode("Id",p[1])])
    

def p_factor2(p):
    '''factor : LPARENT arithmetic RPARENT'''
    p[0]=NonTerminalNode("Factor2",[TerminalNode("Lparent","LPARENT"),p[2],TerminalNode("Rparent","RPARENT")])
    





##########---CONSTANTES DE CONFIGURACION---##########
def p_const0(p):
    '''const : TIMER ASSIGN INT SEMICOLON'''
    p[0]=NonTerminalNode("Const0",[TerminalNode("Timer","TIMER"),TerminalNode("Assign","ASSIGN"),TerminalNode("Int",p[3])])
    

def p_const1(p):
    '''const : RANGOTIMER ASSIGN time_mes SEMICOLON'''
    p[0]=NonTerminalNode("Const1",[TerminalNode("RangoTimer","RANGOTIMER"),TerminalNode("Assign","ASSIGN"),p[3]])
    

def p_const2(p):
    '''const : dimension ASSIGN INT SEMICOLON'''
    p[0]=NonTerminalNode("Const2",[p[1],TerminalNode("Assign","ASSIGN"),TerminalNode("Int",p[3])])
    

def p_const3(p):
    '''const : CUBO ASSIGN INT SEMICOLON'''
    p[0]=NonTerminalNode("Const3",[TerminalNode("Cubo","CUBE"),TerminalNode("Assign","ASSIGN"),TerminalNode("Int",p[3])])
    





##########---CONTENIDO DE ASIGNACIONES---##########
def p_Acont0(p):
    '''a_content : value'''
    p[0]=NonTerminalNode("Acont0",[p[1]])
    

def p_Acont1(p):
    '''a_content : arithmetic'''
    p[0]=NonTerminalNode("Acont1",[p[1]])
    

def p_Acont2(p):
    '''a_content : list'''
    p[0]=NonTerminalNode("Acont2",[p[1]])
    

def p_Acont3(p):
    '''a_content : mat'''
    p[0]=NonTerminalNode("Acont3",[p[1]])
    

def p_Acont4(p):
    '''a_content : 3dmat'''
    p[0]=NonTerminalNode("Acont4",[p[1]])
    

def p_Acont5(p):
    '''a_content : consult'''
    p[0]=NonTerminalNode("Acont5",[p[1]])
    




##########---CONTENIDO DE FUNCIONES---##########
def p_Fcont0(p):
    '''b_content : identifier COMMA INT COMMA time_mes COMMA value'''
    p[0]=NonTerminalNode("Fcont0",[p[1],TerminalNode("Comma","COMMA"),TerminalNode("Int",p[3]),TerminalNode("Comma","COMMA"),p[5],TerminalNode("Comma","COMMA"),p[7]])
    

def p_Fcont1(p):
    '''b_content : identifier COMMA value'''
    p[0]=NonTerminalNode("Fcont1",[p[1],TerminalNode("Comma","COMMA"),p[3]])
    

def p_Fcont2(p):
    '''d_content : empty'''
    p[0]=Null()
    

def p_Fcont3(p):
    '''d_content : iterable COMMA time_mes'''
    p[0]=NonTerminalNode("Fcont3",[p[1],TerminalNode("Comma","COMMA"),p[3]])
    

def p_Fcont4(p):
    '''tf : T'''
    p[0]=NonTerminalNode("Fcont4",[TerminalNode("T","T")])
    

def p_Fcont5(p):
    '''tf : F'''
    p[0]=NonTerminalNode("Fcont5",[TerminalNode("F","F")])
    

def p_Fcont6(p):
    '''i_content : iterable COMMA insertable'''
    p[0]=NonTerminalNode("Fcont6",[p[1],TerminalNode("Comma","COMMA"),p[3]])
   

def p_Fcont7(p):
    '''i_content : iterable COMMA INT i_ind'''
    p[0]=NonTerminalNode("Fcont7",[p[1],TerminalNode("Comma","COMMA"),TerminalNode("Int",p[3]),p[4]])
    





##########---LISTAS Y MATRICES---##########
def p_list(p):
    '''list : PARENTCL list_term PARENTCR'''
    p[0]=NonTerminalNode("List",[TerminalNode("Parentcl","PARENTCL"),p[2],TerminalNode("Parentcr","PARENTCR")])
   

def p_EmptyList(p):
    '''list : PARENTCL empty PARENTCR'''
    p[0]=NonTerminalNode("EmptyList",[TerminalNode("Parentcl","PARENTCL"),Null(),TerminalNode("Parentcr","PARENTCR")])
    

def p_listT0(p):
    '''list_term : list_value COMMA list_term'''
    p[0]=NonTerminalNode("ListT0",[p[1],TerminalNode("Comma","COMMA"),p[3]])
    

def p_listT1(p):
    '''list_term : list_value'''
    p[0]=NonTerminalNode("ListT1",[p[1]])
    

def p_listV(p):
    '''list_value : value'''
    p[0]=NonTerminalNode("ListV",[p[1]])
    

def p_mat(p):
    '''mat : PARENTCL mat_term PARENTCR'''
    p[0]=NonTerminalNode("Mat",[TerminalNode("Parentcl","PARENTCL"),p[2],TerminalNode("Parentcr","PARENTCR")])
    

def p_matT0(p):
    '''mat_term : mat_value COMMA mat_term'''
    p[0]=NonTerminalNode("MatT0",[p[1],TerminalNode("Comma","COMMA"),p[3]])
    

def p_matT1(p):
    '''mat_term : mat_value'''
    p[0]=NonTerminalNode("MatT1",[p[1]])
    

def p_matV(p):
    '''mat_value : list'''
    p[0]=NonTerminalNode("MatV",[p[1]])
    

def p_3dmat(p):
    '''3dmat : PARENTCL 3dmat_term PARENTCR'''
    p[0]=NonTerminalNode("3dMat",[TerminalNode("Parentcl","PARENTCL"),p[2],TerminalNode("Parentcr","PARENTCR")])
    

def p_3dmatT0(p):
    '''3dmat_term : 3dmat_value COMMA 3dmat_term'''
    p[0]=NonTerminalNode("ThreeDMatT0",[p[1],TerminalNode("Comma","COMMA"),p[3]])
    

def p_3dmatT1(p):
    '''3dmat_term : 3dmat_value'''
    p[0]=NonTerminalNode("ThreeDMatT1",[p[1]])
    

def p_3dmatV(p):
    '''3dmat_value : mat'''
    p[0]=NonTerminalNode("ThreeDMatV",[p[1]])
    

def p_consult0(p):
    '''consult : list_consult '''
    p[0]=NonTerminalNode("Consult0",[p[1]])
    

def p_consult1(p):
    '''consult : mat_consult '''
    p[0]=NonTerminalNode("Consult1",[p[1]])
    

def p_consult2(p):
    '''consult : 3dmat_consult'''
    p[0]=NonTerminalNode("Consult2",[p[1]])
    

def p_Listconsult(p):
    '''list_consult : ID list_consultT '''
    p[0]=NonTerminalNode("ListConsult",[TerminalNode("Id",p[1]),p[2]])
    

def p_ListconsultT0(p):
    '''list_consultT : PARENTCL indice PARENTCR'''
    p[0]=NonTerminalNode("ListConsultT0",[TerminalNode("Parentcl","PARENTCL"),p[2],TerminalNode("Parentcr","PARENTCR")])
    

def p_LstconsultT1(p):
    '''list_consultT : PARENTCL indice TP indice PARENTCR '''
    p[0]=NonTerminalNode("ListConsultT1",[TerminalNode("Parentcl","PARENTCL"),p[2],TerminalNode("Tp","TP"),p[4],TerminalNode("Parentcr","PARENTCR")])
    

def p_Matconsult(p):
    '''mat_consult : ID mat_consultT '''
    p[0]=NonTerminalNode("MatConsult",[TerminalNode("Id",p[1]),p[2]])
    

def p_MatconsultT0(p):
    '''mat_consultT : PARENTCL indice COMMA indice PARENTCR'''
    p[0]=NonTerminalNode("MatConsultT0",[TerminalNode("Parentcl","PARENTCL"),p[2],TerminalNode("Comma","COMMA"),p[4],TerminalNode("Parentcr","PARENTCR")])
    

def p_MatconsultT1(p):
    '''mat_consultT : PARENTCL TP COMMA indice PARENTCR '''
    p[0]=NonTerminalNode("MatConsultT1",[TerminalNode("Parentcl","PARENTCL"),TerminalNode("Tp","TP"),TerminalNode("Comma","COMMA"),p[4],TerminalNode("Parentcr","PARENTCR")])
    

def p_MatconsultT2(p):
    '''mat_consultT : PARENTCL TP PARENTCR list_consultT '''
    p[0]=NonTerminalNode("MatConsultT2",[TerminalNode("Parentcl","PARENTCL"),TerminalNode("Tp","TP"),TerminalNode("Parentcr","PARENTCR"),p[4]])
    

def p_MatconsultT3(p):
    '''mat_consultT : PARENTCL indice PARENTCR list_consultT'''
    p[0]=NonTerminalNode("MatConsultT3",[TerminalNode("Parentcl","PARENTCL"),p[2],TerminalNode("Parentcr","PARENTCR"),p[4]])
    

def p_3dMatconsult(p):
    '''3dmat_consult : ID 3dmat_consultT'''
    p[0]=NonTerminalNode("ThreeDMatConsult",[TerminalNode("Id",p[1]),p[2]])
    

def p_3dMatconsultT0(p):
    '''3dmat_consultT : PARENTCL indice COMMA indice COMMA indice PARENTCR'''
    p[0]=NonTerminalNode("ThreeDMatConsultT0",[TerminalNode("Parentcl","PARENTCL"),p[2],TerminalNode("Comma","COMMA"),p[4],TerminalNode("Comma","COMMA"),p[6],TerminalNode("Parentcr","PARENTCR")])
    

def p_3dMatconsultT1(p):
    '''3dmat_consultT : PARENTCL indice PARENTCR mat_consultT'''
    p[0]=NonTerminalNode("ThreeDMatConsultT1",[TerminalNode("Parentcl","PARENTCL"),p[2],TerminalNode("Parentcr","PARENTCR"),p[4]])
    



##########---INDICES---##########
def p_indice0(p):
    '''indice : INT'''
    p[0]=NonTerminalNode("Indice0",[TerminalNode("Int",p[1])])
   

def p_indice1(p):
    '''indice : ID'''
    p[0]=NonTerminalNode("Indice1",[TerminalNode("Id",p[1])])
    

def p_Insind0(p):
    '''i_ind : COMMA iterable'''
    p[0]=NonTerminalNode("Insind0",[TerminalNode("Comma","COMMA"),p[2]])
    

def p_InsindEmp(p):
    '''i_ind : empty'''
    p[0]=Null()
    



##########---DIMENSIONES---##########
def p_dim0(p):
    '''dimension : DIMFILAS'''
    p[0]=NonTerminalNode("Dim0",[TerminalNode("Dimfilas","DIMFILAS")])
    

def p_dim1(p):
    '''dimension : DIMCOLUMNAS'''
    p[0]=NonTerminalNode("Dim1",[TerminalNode("Dimcolumnas","DIMCOLUMNAS")])
    





##########---MEDIDAS DE TIEMPO---##########
def p_timeM0(p):
    '''time_mes : QUOTES MIL QUOTES'''
    p[0]=NonTerminalNode("TimeM0",[TerminalNode("Mil","MIL")])
    

def p_timeM1(p):
    '''time_mes : QUOTES MIN QUOTES'''
    p[0]=NonTerminalNode("TimeM1",[TerminalNode("Min","MIN")])
    

def p_timeM2(p):
    '''time_mes : QUOTES SEG QUOTES'''
    p[0]=NonTerminalNode("TimeM2",[TerminalNode("Seg","SEG")])
    





##########---OPERADORES---##########
def p_addingOp0(p):
    '''adding_operator : PLUS'''
    p[0]=NonTerminalNode("AddingOp0",[TerminalNode("Plus","PLUS")])
    

def p_addingOp1(p):
    '''adding_operator : MINUS'''
    p[0]=NonTerminalNode("AddingOp1",[TerminalNode("Minus","MINUS")])
    

def p_multiplyingOp0(p):
    '''multiplying_operator : TIMES'''
    p[0]=NonTerminalNode("MultiplyingOp0",[TerminalNode("Times","TIMES")])
    
def p_multiplyingOp1(p):
    '''multiplying_operator : EXP'''
    p[0]=NonTerminalNode("MultiplyingOp1",[TerminalNode("Exp","EXP")])
    
def p_multiplyingOp2(p):
    '''multiplying_operator : DIVIDE'''
    p[0]=NonTerminalNode("MultiplyingOp2",[TerminalNode("Divide","DIVIDE")])
    

def p_multiplyingOp3(p):
    '''multiplying_operator : DIVENT'''
    p[0]=NonTerminalNode("MultiplyingOp3",[TerminalNode("Divent","DIVENT")])
    

def p_multiplyingOp4(p):
    '''multiplying_operator : MOD'''
    p[0]=NonTerminalNode("MultiplyingOp4",[TerminalNode("Mod","MOD")])
    





##########---VALORES---##########
def p_value0(p):
    '''value : FALSE'''
    p[0]=NonTerminalNode("Value0",[TerminalNode("FalseV","FALSE")])
    

def p_value1(p):
    '''value : TRUE'''
    p[0]=NonTerminalNode("Value1",[TerminalNode("TrueV","TRUE")])
    

def p_Bifvalue0(p):
    '''bif_value : value'''
    p[0]=NonTerminalNode("BifValue0",[p[1]])
    

def p_Bifvalue1(p):
    '''bif_value : arithmetic'''
    p[0]=NonTerminalNode("BifValue1",[p[1]])
    





##########---RELACIONES---##########
def p_relation0(p):
    '''relation : ASSIGN'''
    p[0]=NonTerminalNode("Relation0",[TerminalNode("Assign","ASSIGN")])
    

def p_relation1(p):
    '''relation : NE'''
    p[0]=NonTerminalNode("Relation1",[TerminalNode("Ne","NE")])
    

def p_relation2(p):
    '''relation : LT'''
    p[0]=NonTerminalNode("Relation2",[TerminalNode("Lt","LT")])
    

def p_relation3(p):
    '''relation : GT'''
    p[0]=NonTerminalNode("Relation3",[TerminalNode("Gt","GT")])
    

def p_relation4(p):
    '''relation : LTE'''
    p[0]=NonTerminalNode("Relation0",[TerminalNode("Lte","LTE")])
    

def p_relation5(p):
    '''relation : GTE'''
    p[0]=NonTerminalNode("Relation5",[TerminalNode("Gte","GTE")])
    

def p_relation6(p):
    '''relation : COMPARE'''
    p[0]=NonTerminalNode("Relation6",[TerminalNode("Compare","COMPARE")])
    



##########---IDENTIFICADORES---##########
def p_identifier0(p):
    '''identifier : ID'''
    p[0]=NonTerminalNode("Identifier0",[TerminalNode("Id",p[1])])
    

def p_identifier1(p):
    '''identifier : consult'''
    p[0]=NonTerminalNode("Identifier1",[p[1]])
    





##########---ITERABLES---##########
def p_iterable0(p):
    '''iterable : identifier'''
    p[0]=NonTerminalNode("Iterable0",[p[1]])
    

def p_iterable1(p):
    '''iterable : INT'''
    p[0]=NonTerminalNode("Iterable1",[TerminalNode("Int",p[1])])

def p_iterable2(p):
    '''iterable : list'''
    p[0]=NonTerminalNode("Iterable2",[p[1]])

def p_iterable3(p):
    '''iterable : mat'''
    p[0]=NonTerminalNode("Iterable3",[p[1]])


##########---INSERTABLES---#########
def p_insertable0(p):
    '''insertable : value'''
    p[0]=NonTerminalNode("Insertable0",[p[1]])

def p_insertable1(p):
    '''insertable : identifier'''
    p[0]=NonTerminalNode("Insertable1",[p[1]])




##########---VARIOS---##########
def p_empty(p):
    'empty : '
    pass

def translate(result):
	graphFile = open('graphviztree.vz', 'w')
	graphFile.write(result.translate())
	graphFile.close()




##########---ERRORES---##########
def p_error(p):
    if (p):
        print(colorama.Fore.RED + "SYNTACTIC ERROR: line:", p.lexer.lineno, "position:", p.lexpos, "Syntax error:", p.value, colorama.Fore.RESET)
    else:
        print(colorama.Fore.RED + "SYNTACTIC ERROR: Unknown syntax error" + colorama.Fore.RESET)
    sys.exit()

test = 'C:/Users/dcama/Desktop/Compilador/Test'
fp = codecs.open(test, "r", "utf-8")
chain = fp.read()
parser = yacc.yacc()
#tv(chain)
result = parser.parse(chain)
translate(result)
