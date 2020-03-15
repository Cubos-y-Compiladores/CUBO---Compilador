import ply.lex as lex
import re
import codecs
import os
import sys

# TODO pasasrlo posiblemente a orientado a objetos

tokens = ['ID', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE','DIVENT','MOD','EXP', 'ASSIGN', 'COMMA', 'SEMMICOLOM',
          'LT', 'GT', 'LTE', 'GTE', 'NE', 'LPARENT', 'RPARENT', 'DOT', 'INT', 'LENGHTERROR', 'BOOKED',
          'PARENTCL', 'PARENTCR', 'LCORCH', 'RCORCH']

reserved = {'if': 'IF',
            'else': 'ELSE',
            'while': 'WHILE',
            'for': 'FOR',
            'const': 'CONST',
            'procedure': 'PROCEDURE',
            'type': 'TYPE',
            'True': 'TRUE',
            'False': 'FALSE',
            'global': 'GLOBAL'}

tokens = tokens + list(reserved.values())

t_ignore = '\t ' # t_ignore es usado para ignorar todos los caracteres dentro de esta lista
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_LT = r'<'
t_GT = r'>'
t_LTE = r'<='
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_PARENTCL = '\['
t_PARENTCR = '\]'
t_NE = '!='
t_LCORCH = '\{'
t_RCORCH = '\}'

# Prueba para doble asignacion
# idd = r'[a-zA-Z@&_][a-zA-Z0-9_]*'
# t_DASSIGN = idd + r',' + idd

global errorFlag
errorFlag = False

# TODO debe tener un maximo de 10 posiciones
# Reconoce variables y palabras reservadas
def t_ID(t):
    r"""[a-z][a-zA-Z0-9_]*"""
    if len(t.value)>10:
        t.type = "LENGHTERROR"
    elif t.value in reserved:
        t.type = reserved[t.value]
        # t.value = (t.value,symbol_lookup(t.value)) Para devolver el valor a la tabla de signos

    else:
        t.type = "ID"
    return t

def t_BOOKED(t):
    r"""[a-zA-Z][a-zA-Z0-9_]*"""
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

# Reconoce Digitos
def t_INT(t):
    r"""\d+"""
    t.value = int(t.value)
    return t

# TODO buscar una forma de  crear ID ASSIGN ID ID ASSIGN ID preguntarle al profe
# def t_DASSIGN(t):
 #   r'[a-zA-Z0-9@&_]*,[a-zA-Z0-9_]*'
  #  return t

def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)

# Reconoce que un string no está en el alfabeto
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    global errorFlag
    errorFlag = not errorFlag
    t.lexer.skip(1)

# Reconoce comentarios
def t_COMMENT(t):
    r"""\--.*"""
    pass



# Remplaza un caracter de un string en una posición especifica por otro valor
def replaceC(data,i,value):
    data = list(data)
    data[i] = value
    data = "".join(data)
    return data

# TODO para que funcione no pueden haber espacios entre las comas 3, 3 => error => pensarlo

def transformData(list1):
    cont = 0
    while  cont != len(list1):
        if "=" in list1[cont]:
            temp = list(list1[cont].replace(" ", ""))
            if len(list1)%2 !=0:
                cont1 = 0
                cont2 = -1
                a = " " + temp[cont1] + "=" + temp[cont2-1] + ";"
                b = " "+ temp[cont1+1] + "=" + temp[cont2] + ";"
                c = a + " " + b
                list1[cont] = c
            else:
                print("No se puede realizar asignaciones",list1[cont])
        cont+=1
    obj = "".join(list1)
    return obj


# Funcion que se aplica antes de analizar cualquier texto, para preparar las asignaciones multiples
# TODO dejarlo de la forma [a,exp,a] si exp%2 = 0 es invalido , debe ser != 0 para ir haciendo las asignaciones con
# TODO modo cont1=1 => +1 cont2=-1 => -1
def findDassign(data):
    cont = 0
    flag = True
    while cont != int(len(data)):
        if data[cont] == "," and flag:
            data = replaceC(data,cont," ")
            data = replaceC(data,cont-2,",")
            flag = not flag
        elif data[cont] == "," :
            data = replaceC(data, cont, " ")
        elif data[cont] == ";":
            data = replaceC(data, cont , ",")
            flag = not flag
        cont += 1
    return transformData(data.split(","))


# Atributos del objeto LexToken
# .value .type .lexpos

path = "C:/Users/Usuario/Desktop/IS2020/CompiladoresLenguajes/Proyect/Tests/test1.pl0"
#file = findFile(path)
#file = input("Enter File Name: ")
test = path
fp = codecs.open(test, "r" , "utf-8")
text = fp.read()
fp.close()

# TODO falta corregir si las variables y los números son más largos (usar algun separador y luego usar dentro de la
#  TODO funcion transform otro split con el separador utilizado en findassign)
# foo = "hola x,var1 = 2,32; hola z,x = 5,6;"
# print(findDassign(foo))


# TODO Verificar que siempre se usen parentesis en las operaciones
lexer = lex.lex()
data1 = """var = 5;"""
data2 = "Var = 5;"
data3 = "a,b = 3,4"
data4 = "type(a)"
data5 = "global var = 1; global var2 = True"
data6 = "var1 != var2"
data7 = "list = [True,False]"
data8 = "x,y = 3,41;"
lex.input(text)
# lexer.input(findDassign(text)) # Arreglar funcion de doble asignación

while 1:

    tok = lexer.token()
    if errorFlag:
        print("Error de entrada en el token", tok)
        errorFlag = not errorFlag
    if not tok:
        break
    print(tok)


# TODO crear funciones para manejo de archivos para luego incorporarlo al ide


