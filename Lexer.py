import ply.lex as lex
import re
import codecs
import os
import sys

#TODO pasasrlo posiblemente a orientado a objetos
''' ID: Identificador
    PLUS: Sumando
    MINUS: Minuendo
    TIMES: Multiplicacion
    DIVIDE:Divicion
    ASSIGN: Asignacion
    COMMA: Coma
    SEMICOLON: Punto y coma
    LT: Menor que
    GT: Mayor que
    LTE: Menor igual
    GTE: Mayor igual
    LPARENT: Parentesis izquierdo
    RPARENT: Parentesis derecho
    DOT: Punto
    INT: Entero
    BOOKED:Palabra reservada(Caso especial para booleanos)
    MOD: Modulo
    DIVENT: Divicion entera
    EXP: Exponente
'''
tokens = ['ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN', 'COMMA', 'SEMMICOLOM',
          'LT', 'GT', 'LTE', 'GTE', 'LPARENT', 'RPARENT', 'DOT', 'INT','LENGHTERROR']

reserved = {'if': 'IF',
            'else': 'ELSE',
            'while': 'WHILE',
            'for': 'FOR',
            'const': 'CONST',
            'procedure': 'PROCEDURE',
            'type': 'TYPE',
            'True':'TRUE',
            'False': 'FALSE'}

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

#idd = r'[a-zA-Z@&_][a-zA-Z0-9_]*'
#t_DASSIGN = idd + r',' + idd



# TODO debe tener un maximo de 10 posiciones
# Reconoce variables y palabras reservadas
def t_ID(t):

    r'[a-zA-Z@&_][a-zA-Z0-9_]*'
    if len(t.value)>10:
        t.type = "LENGHTERROR"
        return t
    elif t.value in reserved:
        t.type = reserved[t.value]
        #t.value = (t.value,symbol_lookup(t.value)) Para devolver el valor a la tabla de signos
    else:
        t.type="ID"
        return t


#Reconoce Digitos
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# TODO buscar una forma de  crear ID ASSIGN ID ID ASSIGN ID preguntarle al profe
#def t_DASSIGN(t):
 #   r'[a-zA-Z0-9@&_]*,[a-zA-Z0-9_]*'
  #  return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Reconoce que un string no está en el alfabeto
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Reconoce comentarios
def t_COMMENT(t):
    r'\--.*'
    pass


#todo Verificar que siempre se usen parentesis en las operaciones
lexer = lex.lex()
data1 = """for result 
        = (3+4*10+-20*2) True False @holaaaaaaa"""
data2 = "a,b = 3,4"
lexer.input(data2)

while 1:
    tok = lexer.token()

    if not tok:
        break
    print(tok)

#Atributos del objeto LexToken
# .value .type .lexpos






