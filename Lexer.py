import ply.lex as lex
import re
import codecs
import os
import sys

# TODO pasasrlo posiblemente a orientado a objetos

tokens = ['ID', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE','DIVENT','MOD','EXP', 'ASSIGN', 'COMMA', 'SEMMICOLOM',
          'LT', 'GT', 'LTE', 'GTE', 'LPARENT', 'RPARENT', 'DOT', 'INT', 'LENGHTERROR','BOOKED']

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

# Prueba para doble asignacion
# idd = r'[a-zA-Z@&_][a-zA-Z0-9_]*'
# t_DASSIGN = idd + r',' + idd

global errorFlag
errorFlag = False

# TODO debe tener un maximo de 10 posiciones
# Reconoce variables y palabras reservadas
def t_ID(t):
    r'[a-z][a-zA-Z0-9_]*'
    if len(t.value)>10:
        t.type = "LENGHTERROR"

        # t.value = (t.value,symbol_lookup(t.value)) Para devolver el valor a la tabla de signos
    else:
        t.type = "ID"
    return t

def t_BOOKED(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

# Reconoce Digitos
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# TODO buscar una forma de  crear ID ASSIGN ID ID ASSIGN ID preguntarle al profe
# def t_DASSIGN(t):
 #   r'[a-zA-Z0-9@&_]*,[a-zA-Z0-9_]*'
  #  return t

def t_newline(t):
    r'\n+'
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


# TODO Verificar que siempre se usen parentesis en las operaciones
lexer = lex.lex()
data1 = """var = 5;"""
data2 = "Var = 5;"
data3 = "a,b = 3,4"
data4 = "type(a)"
data5 = "global var = 1; global var2 = True"
lexer.input(data5)

while 1:

    tok = lexer.token()
    if errorFlag:
        print("Error de entrada en el token", tok)
        errorFlag = not errorFlag
    if not tok:
        break
    print(tok)

# Atributos del objeto LexToken
# .value .type .lexpos

# Funcion que se aplica antes de analizar cualquier texto, para preparar las asignaciones multiples

# TODO para que funcione no pueden haber espacios entre las comas 3, 3 => error
def findDassign(data):
    cont = 0
    print("len",len(data))
    temp1 = ""
    temp2 = ""
    while cont != int(len(data)):
        if data[cont] == ",":
            data = data[:cont] + " " + data[cont:]
            temp1 = data[:cont-2] + "," + data[cont-2:]

        elif data[cont] == "=":
            temp2 = temp1[:cont+1] + "," + temp1[cont+1:]

        cont+=1

    return temp2.split(",")

foo = "hola x,y = 2,3"
foo.replace(4,"@")
print(foo)
#print(foo[:4] + " " + foo[4:])

#print(findDassign(foo))




