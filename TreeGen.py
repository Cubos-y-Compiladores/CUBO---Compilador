txt = " "
cont = 0
def incremetarContador():
	global cont
	cont +=1
	return "%d" %cont

class Node():
	pass

class Null(Node):
	def __init__(self):
		self.type = 'void'

	def imprimir(self,ident):
		print ident + "nodo nulo"

	def traducir(self):
		global txt
		id = incremetarContador()
		txt += id+"[label= "+"nodo_nulo"+"]"+"\n\t"

		return id





##########---BLOQUES BASICOS---#########
class p_program(Node):
    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_constB(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_block0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_block1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_blockEmp(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---BLOQUES ALTERNATIVOS---##########
class p_altBlock(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_emptyaltBlock(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_altContent0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_altContent1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---INSTRUCCIONES---##########
class p_instruction0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_instruction1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_instruction2(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_instruction3(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---ASIGNACIONES GLOBALES---##########
class p_globalAssignment(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---ASIGNACIONES---##########
class p_simpleAssignment(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_doubleAssignment(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---FUNCIONES---##########
class p_function0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_function1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_function2(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_function3(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_function4(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_function5(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_function6(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_function7(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_function8(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_function9(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_function10(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_type(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_range(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_insert(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_del(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_len(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_neg0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_tf(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_blink(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_delay(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_shapeArg0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_shapeArg1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_shapeArg2(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_shape(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_delete(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_call(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---CICLOS---##########
class p_cycle0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_for(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_step0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_stepEmp(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---BIFURCACIONES---##########
class p_statement(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_optStatment0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_optStatment1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---PROCEDIMIENTOS---##########
class p_procedure(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_procDec(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_procName(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_parameter0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_parameter1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_emptyParameter(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_procParam0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_body(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_mainProcedure(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_mainBody(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_mainBlock0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_emptyMainblk(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---OPERACIONES ARITMETICAS---##########
class p_arithmetic0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_arithmetic1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_arithmetic2(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---TERMINOS---##########
class p_term0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_term1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---FACTORES---##########
class p_factor0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_factor1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_factor2(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---CONSTANTES DE CONFIGURACION---##########
class p_const0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_const1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_const2(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_const3(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---CONTENIDO DE ASIGNACIONES---##########
class p_Acont0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Acont1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Acont2(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Acont3(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Acont4(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Acont5(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---CONTENIDO DE FUNCIONES---##########
class p_Fcont0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Fcont1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Fcont2(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Fcont3(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Fcont4(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Fcont5(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Fcont6(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Fcont7(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---LISTAS Y MATRICES---##########
class p_list(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_listEmp(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_listT0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_listT1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_listV0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_mat(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_matT0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_matT1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_matV0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_3dmat(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_3dmatT0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_3dmatT1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_3dmatV0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_consult0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output
        ("consult0")


class p_consult1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_consult2(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Lstconsult(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_LstconsultT0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_LstconsultT1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Matconsult(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_MatconsultT0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_MatconsultT1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_MatconsultT2(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_MatconsultT3(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_3dMatconsult(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_3dMatconsultT0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_3dMatconsultT1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---INDICES---##########
class p_indice0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_indice1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Insind0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_InsindEmp(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---DIMENSIONES---##########
class p_dim0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_dim1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---MEDIDAS DE TIEMPO---##########
class p_timeM0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_timeM1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_timeM2(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---OPERADORES---##########
class p_addingOp0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_addingOp1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_multiplyingOp0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_multiplyingOp1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_multiplyingOp2(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_multiplyingOp3(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_multiplyingOp4(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---VALORES---##########
class p_value0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_value1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Bifvalue0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Bifvalue1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---RELACIONES---##########
class p_relation0(Node):

    def __init__(self):


def printer(self, ident):
    def translate(self):
        global output


class p_relation1(Node):

    def __init__(self):


def printer(self, ident):
    def translate(self):
        global output


class p_relation2(Node):

    def __init__(self):


def printer(self, ident):
    def translate(self):
        global output


class p_relation3(Node):

    def __init__(self):


def printer(self, ident):
    def translate(self):
        global output


class p_relation4(Node):

    def __init__(self):


def printer(self, ident):
    def translate(self):
        global output


class p_relation5(Node):

    def __init__(self):


def printer(self, ident):
    def translate(self):
        global output


class p_relation6(Node):

    def __init__(self):


def printer(self, ident):
    def translate(self):
        global output





##########---IDENTIFICADORES---##########
class p_identifier0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_identifier1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---ITERABLES---##########
class p_iterable0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_iterable1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output
