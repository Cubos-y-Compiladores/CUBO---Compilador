import wx
import os
from functools import partial
import ply.lex as lex
import re
import sys
import threading
import wx.lib.agw.multidirdialog as MDD
import time

wildcard = "*.cbc"
tokens = ['ID', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE','DIVENT','MOD','EXP', 'ASSIGN', 'COMMA', 'SEMICOLON',
          'LT', 'GT', 'LTE', 'GTE', 'NE', 'LPARENT', 'RPARENT', 'DOT', 'INT', 'LENGHTERROR','VARERROR', 'BOOKED',
          'PARENTCL', 'PARENTCR', 'LCORCH', 'RCORCH', 'TP','QUOTES',"newline","SPACE","TAB","COMMENT"]

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

t_ignore = '\r' # t_ignore es usado para ignorar todos los caracteres dentro de esta lista
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
t_SPACE = r'\s'
t_TAB = r"\t"


# Reconoce variables y palabras reservadas
def t_ID(t):
    r"""[a-zA-Z][a-zA-Z0-9_@&]*"""
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
    return t
    #t.lexer.lineno += len(t.value)


# Reconoce que un string no está en el alfabeto
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Reconoce comentarios
def t_COMMENT(t):
    r"""\--.*"""
    return t

def t_EXP(t):
    r'[*][*]'
    return t
def t_DIVENT(t):
    r'[/][/]'
    return t



class MyApp(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent = parent , title = title, size = (1200,750))
        # TODO arreglar por qué siempre cubre toda la pantalla
        self.textMain = wx.TextCtrl(self,style=wx.TE_MULTILINE|wx.TE_RICH,pos=(0,0),size=(1,1))
        self.textConsole = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.TE_RICH, pos=(0, 0), size=(1, 1))

        self.currentDirectory = os.getcwd()
        self.currentFile = ""
        # Reserved words
        self.reservedWords1 = ["WHILE","FOR","IF","ELSE","CONST","GLOBAL","IN"]
        self.reservedWords2 = ["PROCEDURE","MAIN","TIMER","DIMFILAS","DIMCOLUMNAS","RANGOTIMER","CUBO","BEGIN","END"]
        self.reservedWords3 = ["RANGE","TYPE","BLINK","DELAY","LEN","STEP","CALL","T","F","DEL","DELETE","SHAPEF","SHAPEC","SHAPEA","NEG","DELETE"]
        self.symbols = ['COMMA', 'LCORCH', 'RCORCH', 'QUOTES', 'ASSIGN'] # 'SEMICOLON',
        self.comment = "COMMENT"
        self.rTrue = "TRUE"
        self.rFalse = ["FALSE"]
        self.parentscorchs = ["PARENTCL","PARENTCR","RPARENT","LPARENT","MIL","SEG","MIN"]

        self.currenttext = ""

        # Main File
        self.mainFile = "Files/test.txt"
        # VariablesContadores
        self.contList = 0
        self.contMatriz2 = 0
        self.contMatriz3 = 0

        # Barra Menu
        self.mainMenu = wx.MenuBar()

        # SubMenus
        self.subMenuFile = wx.Menu()
        self.subMenuInsert = wx.Menu()
        self.subMenuRun = wx.Menu()
        # SubMenusInsert
        self.subMenuMat2D = wx.Menu()
        self.subMenuMat3D = wx.Menu()
        # Agregando a los submenus


        self.subOpen = self.subMenuFile.Append(-1, "Open\tCtrl-O")
        self.subNew = self.subMenuFile.Append(-1,"New\tCtrl-N")
        self.subSave = self.subMenuFile.Append(-1, "Save\tCtrl-S")
        self.subSaveAs = self.subMenuFile.Append(-1, "Save As\tCtrl-G")
        self.subExit = self.subMenuFile.Append(-1,"Exit\tCtrl-X")


        self.subInsertL = self.subMenuInsert.Append(-1,"List\tCtrl-Q")
        self.sub1x1 = self.subMenuMat2D.Append(1, "1x1")
        self.sub2x2 = self.subMenuMat2D.Append(2, "2x2")
        self.sub3x3 = self.subMenuMat2D.Append(3, "3x3")
        self.sub4x4 = self.subMenuMat2D.Append(4, "4x4")
        self.sub5x5 = self.subMenuMat2D.Append(5, "5x5")
        self.sub6x6 = self.subMenuMat2D.Append(6, "6x6")
        self.sub7x7 = self.subMenuMat2D.Append(7, "7x7")
        self.sub8x8 = self.subMenuMat2D.Append(8, "8x8")
        self.subInsertM2 = self.subMenuInsert.AppendSubMenu(self.subMenuMat2D,"Matriz2D")

        self.sub1x1x1 = self.subMenuMat3D.Append(11, "1x1x1")
        self.sub2x2x2 = self.subMenuMat3D.Append(22, "2x2x2")
        self.sub3x3x3 = self.subMenuMat3D.Append(33, "3x3x3")
        self.sub4x4x4 = self.subMenuMat3D.Append(44, "4x4x4")
        self.sub5x5x5 = self.subMenuMat3D.Append(55, "5x5x5")
        self.sub6x6x6 = self.subMenuMat3D.Append(66, "6x6x6")
        self.sub7x7x7 = self.subMenuMat3D.Append(77, "7x7x7")
        self.sub8x8x8 = self.subMenuMat3D.Append(88, "8x8x8")
        self.subInsertM3 = self.subMenuInsert.AppendSubMenu(self.subMenuMat3D,"Matriz3D")

        self.subRun = self.subMenuRun.Append(-1,"Run This\tCtrl-F5")
        # Agregando al menu principal
        self.mainMenu.Append(self.subMenuFile,"File")
        self.mainMenu.Append(self.subMenuInsert,"Insert")
        self.mainMenu.Append(self.subMenuRun,"Run")
        # Agregando barra al frame
        self.SetMenuBar(self.mainMenu)
        # Eventos menu
        self.Bind(wx.EVT_MENU, self.insertList, self.subInsertL)
        self.Bind(wx.EVT_MENU, self.subExitWindow, self.subExit)
        self.Bind(wx.EVT_MENU, self.openFileTXT, self.subOpen)
        self.Bind(wx.EVT_MENU, self.saveFile, self.subSave)
        self.Bind(wx.EVT_MENU, self.saveFileAs, self.subSaveAs)
        self.Bind(wx.EVT_MENU, self.newFile, self.subNew)
        self.Bind(wx.EVT_MENU, self.runFile, self.subRun)




        # Eventos Submenus de matrices 2D

        self.Bind(wx.EVT_MENU, partial(self.insertMatriz2D,1), self.sub1x1)
        self.Bind(wx.EVT_MENU, partial(self.insertMatriz2D,2), self.sub2x2)
        self.Bind(wx.EVT_MENU, partial(self.insertMatriz2D,3), self.sub3x3)
        self.Bind(wx.EVT_MENU, partial(self.insertMatriz2D,4), self.sub4x4)
        self.Bind(wx.EVT_MENU, partial(self.insertMatriz2D,5), self.sub5x5)
        self.Bind(wx.EVT_MENU, partial(self.insertMatriz2D,6), self.sub6x6)
        self.Bind(wx.EVT_MENU, partial(self.insertMatriz2D,7), self.sub7x7)
        self.Bind(wx.EVT_MENU, partial(self.insertMatriz2D,8), self.sub8x8)

        self.Bind(wx.EVT_MENU, partial(self.insertMatriz3D,11), self.sub1x1x1)
        self.Bind(wx.EVT_MENU, partial(self.insertMatriz3D,22), self.sub2x2x2)
        self.Bind(wx.EVT_MENU, partial(self.insertMatriz3D,33), self.sub3x3x3)
        self.Bind(wx.EVT_MENU, partial(self.insertMatriz3D,44), self.sub4x4x4)
        self.Bind(wx.EVT_MENU, partial(self.insertMatriz3D,55), self.sub5x5x5)
        self.Bind(wx.EVT_MENU, partial(self.insertMatriz3D,66), self.sub6x6x6)
        self.Bind(wx.EVT_MENU, partial(self.insertMatriz3D,77), self.sub7x7x7)
        self.Bind(wx.EVT_MENU, partial(self.insertMatriz3D,88), self.sub8x8x8)




        # Botones
        btn1 = wx.Button(self,-1,u"B",pos=(0,4),size=(20,20))
        # Funcion boton
        self.Bind(wx.EVT_BUTTON,self.click1)

        # Labels
        self.lblFileName = wx.StaticText(self,-1,"",(0,0))
        self.upDateFileName("")

        #Sliders
        self.slideFont = wx.Slider(self,-1,12,12,28,(1000,0),(150,20))
        self.Bind(wx.EVT_SLIDER,self.onSlider)

        # Fuentes de Texto
        self.setFontSize(12)

        self.textMain.SetOwnBackgroundColour((54,72,101))
        self.textConsole.SetBackgroundColour((54, 72, 101))
        self.textMain.SetForegroundColour((255,255,255))
        self.textConsole.SetForegroundColour((255, 255, 255))



        # Sizer , Proporciona tamaño a los controles
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.textMain,2,wx.EXPAND|wx.LEFT|wx.UP,20)
        sizer.Add(self.textConsole, 1, wx.EXPAND|wx.LEFT|wx.UP,10)
        self.SetSizer(sizer)
        self.lblFileName = wx.StaticText()

        #self.initFILE()

        # self.onOpenFile()

        self.Centre(1)
        self.SetBackgroundColour(self.textMain.GetBackgroundColour())

        self.Show()
        # TODO: investigar como unir el thread para que siempre se esté actuaizando el texto
        self.t = threading.Thread(target = self.loop, args=())
        self.initThread()



    # Funcion para boton1, imprime lo que esté escrito en las entradas de texto
    def initThread(self):
        self.t.start()

    def loop(self):
        while 1:
            self.changeReservedWords()
            time.sleep(1)

    def click1(self,event):
        # print("Input1: " + str(self.textMain.GetValue()))
        # print("Input2: " + str(self.textConsole.GetValue()))
        # self.changeReservedWords()
        self.textMain.SetStyle(0,3,wx.TextAttr(wx.GREEN))
    def insertList(self,event):
        self.textMain.AppendText("list" + str(self.contList) +"= [];\n")
        self.contList += 1
    def insertMatriz2D(self,number,event):

        text = " ["
        for i in range(number-1):
            text+="[],\n\t\t"

        text += "[]];\n"

            # text += "["
            # text += "False,"*(number-1)
            # text += "Fase],"
            # text += "\n\t     "
        # text += "["
        # text += "False,"*(number-1)
        # text += "False]"
        # text+="];\n"

        self.textMain.AppendText("matriz2D" + str(self.contMatriz2) +"= "+ text)
        self.contMatriz2 += 1
    def insertMatriz3D(self,number,event):
        number = number%10
        textFinal = " ["

        for i in range(number-1):
            text = "["

            for j in range(number - 1):
                text += "[],"
            text += "[]"
            text += "]"
            textFinal += text+",\n\t\t"

        text = "["
        for k in range(number - 1):
            text += "[],"
        text += "[]"
        text += "]"
        textFinal += text+"];\n"
        print(textFinal)

        self.textMain.AppendText("matriz3D" + str(self.contMatriz3) +"= "+ textFinal)
        self.contMatriz3 += 1

    def subExitWindow(self,event):
        self.Close(1)
    def initFILE(self):
        f = open(self.mainFile, "r")
        txt = f.read()
        f.close()
        self.textMain.SetValue(txt)
    def openFileTXT(self,event):
        self.onOpenFile()


    def onOpenFile(self):

        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=self.currentDirectory,
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
        )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            self.currentFile = paths[0]
            f = open(paths[0],"r")
            txt = f.read()
            f.close()

            self.upDateFileName(paths[0].split("\\")[-1])
            self.textMain.SetValue(txt)

        dlg.Destroy()

    def saveFile(self,event):
        f = open(self.currentFile,"w")
        f.write(self.textMain.GetValue())
        f.close()

    def saveFileAs(self,event):
        self.onSaveFile()

    def onSaveFile(self):

        dlg = wx.FileDialog(
            self, message="Save file as ...",
            defaultDir=self.currentDirectory,
            defaultFile="New", wildcard=wildcard, style=wx.FD_SAVE
        )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            f = open(path,"w")
            f.write(self.textMain.GetValue())
            f.close()
            self.upDateFileName(path.split("\\")[-1])
        dlg.Destroy()

    def newFile(self,event):
        if self.currentFile != "":
            f = open(self.currentFile, "w")
            f.write(self.textMain.GetValue())
            f.close()
            self.textMain.Clear()
        self.upDateFileName("New")

    def runFile(self,event):
        print("Running")

    def upDateFileName(self,name):
        self.lblFileName = wx.StaticText(self,-1,"File-> "+name,(35,0))
        self.lblFileName.SetForegroundColour((38,216,205))
    def setFontSize(self,size):
        font = self.textMain.GetFont()
        font.SetPointSize(size)
        self.textMain.SetFont(font)
        self.textConsole.SetFont(font)

    def onSlider(self,event):
        self.setFontSize(self.slideFont.GetValue())

    def writeColor(self,text,t):
        self.textMain.SetDefaultStyle(wx.TextAttr(t))
        self.textMain.WriteText(text)
        self.textMain.SetDefaultStyle(wx.TextAttr(wx.WHITE))

    def setStyleText(self,start,end,color):
        self.textMain.SetStyle(start, end, wx.TextAttr(color))
        self.textMain.SetDefaultStyle(wx.TextAttr((255,255,255)))

    def getLenNumber(self,number):
        cont = 0
        while number != 0:
            number = number%10
            cont+=1
        return cont
    # TODO: crear funcion de busqueda
    def changeReservedWords(self):
        curPos = self.textMain.GetInsertionPoint()
        print("curPos: "+ str(curPos))
        linenumber = self.textMain.PositionToXY(curPos)
        print("linenumber: "+str(linenumber[2]))
        # lineNum = self.textMain.GetRange(0,self.textMain.GetInsertionPoint())
        lineText = self.textMain.GetLineText(linenumber[2])
        print(lineText)

        if self.textMain.GetValue() != self.currenttext or len(self.textMain.GetValue()) != len(self.currenttext):
        
            text = self.textMain.GetValue()

            lexer = lex.lex()
            lexer.input(text)
            self.currenttext = text
            while 1:
                tok = lexer.token()
                if not tok:
                    break
                else:
                    if tok != None:
                        if tok.type in self.reservedWords1:
                            self.setStyleText(tok.lexpos,tok.lexpos + len(tok.value),(224,71,158))
                        elif tok.type in self.reservedWords2:
                            self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), (79, 200, 218))
                        elif tok.type == self.comment:
                            self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), (165, 197, 195))
                        elif tok.type in self.symbols:
                            self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), (251, 139, 36))
                        elif tok.type in self.reservedWords3:
                            self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), (252, 163, 17))
                        elif tok.type == self.rTrue:
                            self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), (0, 179, 131))
                        elif tok.type in self.rFalse:
                            self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), (254, 74, 38))
                        elif tok.type in self.parentscorchs:
                            self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), (166, 162, 162))
                        elif tok.type == "ID":
                            self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), (255, 255, 255))



# Creando funcion que reconoce solo el texto nuevo para colorearlo
    def changeWordColor(self,start,end):
        # como tomar el texto de la posicion inicial a la final para luego analizarla con el lexer

        if self.textMain.GetValue() != self.currenttext or len(self.textMain.GetValue()) != len(self.currenttext):

            text = self.textMain.GetValue()

            lexer = lex.lex()
            lexer.input(text)
            self.currenttext = text
            #Recalcular las posiciones de los tokens con start y end
            while 1:
                tok = lexer.token()
                if not tok:
                    break
                else:
                    if tok != None:
                        if tok.type in self.reservedWords1:
                            self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), (224, 71, 158))
                        elif tok.type in self.reservedWords2:
                            self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), (79, 200, 218))
                        elif tok.type == self.comment:
                            self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), (165, 197, 195))
                        elif tok.type in self.symbols:
                            self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), (251, 139, 36))
                        elif tok.type in self.reservedWords3:
                            self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), (252, 163, 17))
                        elif tok.type == self.rTrue:
                            self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), (0, 179, 131))
                        elif tok.type in self.rFalse:
                            self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), (254, 74, 38))
                        elif tok.type in self.parentscorchs:
                            self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), (166, 162, 162))
                        elif tok.type == "ID":
                            self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), (255, 255, 255))

if __name__ == '__main__':
    app = wx.App()
    frame = MyApp(None,"IDLE")
    app.MainLoop()