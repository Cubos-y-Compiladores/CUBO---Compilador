import ply.lex as lex
import re
import codecs
import os
import sys
from pip._vendor import colorama

# LOGICA

def printC(data,color):
    if color == "r":
        print(colorama.Fore.RED + str(data) + colorama.Fore.RESET)
    elif color == "b":
        print(colorama.Fore.BLUE + str(data) + colorama.Fore.RESET)
    elif color == "g":
        print(colorama.Fore.GREEN + str(data) + colorama.Fore.RESET)
    elif color == "bk":
        print(colorama.Fore.BLACK + str(data) + colorama.Fore.RESET)
    elif color == "y":
        print(colorama.Fore.YELLOW + str(data) + colorama.Fore.RESET)
    elif color == "m":
        print(colorama.Fore.MAGENTA + str(data) + colorama.Fore.RESET)
    elif color == "c":
        print(colorama.Fore.CYAN + str(data) + colorama.Fore.RESET)
    elif color == "lr":
        print(colorama.Fore.LIGHTRED_EX + str(data) + colorama.Fore.RESET)
    elif color == "lb":
        print(colorama.Fore.LIGHTBLUE_EX + str(data) + colorama.Fore.RESET)
    elif color == "lg":
        print(colorama.Fore.LIGHTGREEN_EX + str(data) + colorama.Fore.RESET)
    elif color == "lbk":
        print(colorama.Fore.LIGHTBLACK_EX + str(data) + colorama.Fore.RESET)
    elif color == "lc":
        print(colorama.Fore.LIGHTCYAN_EX + str(data) + colorama.Fore.RESET)
    elif color == "lm":
        print(colorama.Fore.LIGHTMAGENTA_EX + str(data) + colorama.Fore.RESET)
    elif color == "ly":
        print(colorama.Fore.LIGHTYELLOW_EX + str(data) + colorama.Fore.RESET)
    elif color == "w":
        print(colorama.Fore.WHITE + str(data) + colorama.Fore.RESET)
    elif color == "lw":
        print(colorama.Fore.LIGHTWHITE_EX + str(data) + colorama.Fore.RESET)


# TODO pasasrlo posiblemente a orientado a objetos

tokens = ['ID', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE','DIVENT','MOD','EXP', 'ASSIGN', 'COMMA', 'SEMICOLON',
          'LT', 'GT', 'LTE', 'GTE', 'NE', 'LPARENT', 'RPARENT', 'DOT', 'INT', 'LENGHTERROR','VARERROR', 'BOOKED',
          'PARENTCL', 'PARENTCR', 'LCORCH', 'RCORCH', 'TP','QUOTES']

reserved = {'if': 'IF',
            'else': 'ELSE',
            'while': 'WHILE',
            'for': 'FOR',
            'const': 'CONST',
            'Procedure': 'PROCEDURE',
            'type': 'TYPE',
            'True': 'TRUE',
            'False': 'FALSE',
            'global': 'GLOBAL',
            'range': 'RANGE',
            'insert':'INSERT',
            'del':'DELETE',
            'len':'LEN',
            'Neg':'NEG',
            'T':'T',
            'F':'F',
            'Blink':'BLINK',
            'Delay':'DELAY',
            'in':'IN',
            'Step':'STEP',
            'shapeC':'SHAPEC',
            'shapeF':'SHAPEF',
            'shapeA':'SHAPEA',
            'Main':'MAIN',
            'CALL':'CALL',
            'Timer':'TIMER',
            'Rango_Timer':'RANGOTIMER',
            'Dim_Filas':'DIMFILAS',
            'Dim_Columnas':'DIMCOLUMNAS',
            'Cubo':'CUBO',
            'Mil': 'MIL',
            'Seg': 'SEG',
            'Min': 'MIN'
            }

tokens = tokens + list(reserved.values())

t_ignore = '\t\r ' # t_ignore es usado para ignorar todos los caracteres dentro de esta lista
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
t_SEMICOLON = r';'
t_DOT = r'\.'
t_PARENTCL = '\['
t_PARENTCR = '\]'
t_NE = '!='
t_LCORCH = '\{'
t_RCORCH = '\}'
t_TP = '\:'
t_MOD = '%'
t_QUOTES = '"'



# Reconoce variables y palabras reservadas
def t_ID(t):
    r"""[a-z][a-zA-Z0-9_@&]*"""
    if len(t.value)>10:
        t.type = "LENGHTERROR"

    elif t.value in reserved:
        t.type = reserved[t.value]
        # t.value = (t.value,symbol_lookup(t.value)) Para devolver el valor a la tabla de signos

    else:
        t.type = "ID"
    return t

# Reconoce booleanos
def t_BOOKED(t):
    r"""[a-zA-Z][a-zA-Z0-9_]*"""
    if t.value in reserved:
        t.type = reserved[t.value]
    else:
        t.type = "VARERROR"
    return t

# Reconoce numeros
def t_INT(t):
    r"""\d+"""
    t.value = int(t.value)
    return t
# Reconoce saltos de linea
def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)


# Reconoce que un string no está en el alfabeto
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Reconoce comentarios
def t_COMMENT(t):
    r"""\--.*"""
    pass

def t_EXP(t):
    r'[*][*]'
    return t
def t_DIVENT(t):
    r'[/][/]'
    return t




# Remplaza un caracter de un string en una posición especifica por otro valor
def replaceC(data,i,value):
    data = list(data)
    data[i] = value
    data = "".join(data)
    return data

# Verifica si la lista contiene un multiplo 3 de elementos
def fun(d):
    if "=" in d:
        d = d.replace("=", " = ")
        d = d.replace(" ", "@")
        temp =d.split("@")
        for i in range(temp.count("")):
            temp.remove("")
        if len(temp)%3 != 0:
            return True
    return False

# Transforma la la oracion de sintaxis x,y=2,3; a x=2;y=3;
def transformData(list1):
    cont = 0
    while cont != len(list1):
        if "=" in list1[cont] and fun(list1[cont]): # TODO arreglar por las expresiones simples como x = 7;

            list1[cont] = list1[cont].replace("="," = ")
            list1[cont] = list1[cont].replace(" ","@")
            temp = list1[cont].split("@")
            for i in range(temp.count("")):
                temp.remove("")

            if len(temp)%2 !=0:
                cont1 = 0
                cont2 = -1
                a = " " + temp[cont1] + "=" + temp[cont2-1] + ";"
                b = " "+ temp[cont1+1] + "=" + temp[cont2] + ";"
                c = a + " " + b
                list1[cont] = c
        elif "=" in list1[cont]:
            list1[cont] = list1[cont] + ";"
        cont+=1
    obj = "".join(list1)
    return obj

# Elimina de una lista elementos como "" y " "
def clean(inputlist):
    for i in range(inputlist.count("")):
        inputlist.remove("")
    for j in range(inputlist.count(" ")):
        inputlist.remove(" ")
    return inputlist

# Funcion que se aplica antes de analizar cualquier texto, para preparar las asignaciones multiples
def findDassign(data):
    cont = 0
    flag = True
    data = data.replace(";","; ")
    while cont != int(len(data)):
        if data[cont] == "," and flag:
            data = replaceC(data,cont," ")
            cont1 = cont-1
            if data[cont1] == " ":
                while data[cont1] == " ":
                    cont1-=1
            while 1:
                if data[cont1] == " " or cont1 == 0:
                    break
                cont1-=1
            if cont1 == 0:
                data = replaceC(data,cont1,","+data[cont1])
            else:
                data = replaceC(data,cont1,",")
            flag = not flag
        elif data[cont] == "," and flag == False:
            data = replaceC(data, cont, " ")
        elif data[cont] == ";":
            data = replaceC(data, cont , ",")
            flag = not flag
        cont += 1

    temp = data.split(",")
    temp = clean(temp)
    return transformData(temp)


# ARCHIVOS


path = "C:/Users/Usuario/Desktop/IS2020/CompiladoresLenguajes/Proyect/Tests/test1.pl0"
# file = findFile(path)
# file = input("Enter File Name: ")
test = path
fp = codecs.open(test, "r" , "utf-8")
text = fp.read()
fp.close()

# Prueba para remplazo de palabras de doble asignación
# foo = "hola varx,vary=221,345; hola zvar,xvar = 512,625;"
# foo = "-- xVAR      ,    yVAR=300    ,    200   ;"
# printC("ORIGINAL"+ "\n" +foo, "r")
# printC("CHANGED" + "\n" + findDassign(foo), "b")

lexer = lex.lex()
data1 = """var = 5; 
y= 2;"""
data2 = "Var = 5;"
data3 = "a,b = 3,4"
data4 = "type(a)"
data5 = "global var = 1; global var2 = True"
data6 = "var1 != var2"
data7 = "list = [True,False] lista[1:4] x = range(5,True)"
data8 = "x,y = 3,41;"
data9 = " const Var = 1; l.insert(2,True)"
data10 = "type(var).Blink.T.F.Neg Type"
lexer.input(text)
# print(findDassign(text))
# lexer.input(findDassign(text)) # Arreglar funcion de doble asignación


while 1:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

# TODO crear funciones para manejo de archivos para luego incorporarlo al ide

# TODO crear estructura de tabla de signos , posiblemente un objeto variable y una lista

class Var:
    def __init__(self,n,v,t = "null", isG = 0 , r = 1):
        self.name = n
        self.value = v
        self.type = t
        self.isGlobal = isG
        if isinstance(v,list):
            self.range = len(v)
            self.type = "list"
        else:
            self.range = r
            if isinstance(v,int):
                self.type = "int"
            if isinstance(v,bool):
                self.type = "bool"
                
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getType(self):
        return self.type
    def getIsGlobal(self):
        return self.isGlobal
    def getRange(self):
        return self.range
    def getInfo(self):
        return self.name,self.value,self.type,self.isGlobal,self.range

class SymbolTable:
    def __init__(self):
        self.array = []
    def getLen(self):
        return len(self.array)
    def getList(self):
        return self.array
    def insertVar(self,var):
# TODO preguntar al profe que pasa si uno define una variable normal y luego la vuelve global (se puede ? )
        self.array += [var]
    def findVar(self,nameVar):
        for i in self.array:
            if i.getName() == nameVar:
                return i.getInfo()
    def showAllSymbols(self):
        result = []
        for i in self.array:
            result += [("VAR = " + str(i.getName()), "VAL = "+str(i.getValue()))]
        printC(result,"g")

symboltable = SymbolTable()
printC(str(symboltable.getLen()),"r")
var1 = Var("var1",560)
symboltable.insertVar(var1)
printC(symboltable.findVar("var1"),"b")

var2 = Var("var2",1)
print(var2.getRange(),var2.getType())
symboltable.insertVar(var2)
var3 = Var("var3",True)
symboltable.insertVar(var3)

printC(symboltable.findVar("var3"),"b")
symboltable.showAllSymbols()


