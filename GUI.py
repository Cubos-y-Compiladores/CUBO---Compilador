import wx
import os
from functools import partial
import ply.lex as lex
import os.path
from os import path
import pathlib
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
            'del':'DEL',
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
            'Call':'CALL',
            'Timer':'TIMER',
            'Rango_Timer':'RANGOTIMER',
            'Dim_Filas':'DIMFILAS',
            'Dim_Columnas':'DIMCOLUMNAS',
            'Cubo':'CUBO',
            'Mil': 'MIL',
            'Seg': 'SEG',
            'Min': 'MIN',
            'begin':'BEGIN',
            'end':'END',
            'delete':'DELETE'
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

# Reglas para cambios de color

# Reconoce variables y palabras reservadas
def t_ID(t):
    r"""[a-zA-Z][a-zA-Z0-9_@&]*"""

    if t.value in reserved:
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
# Reconoce exponentes
def t_EXP(t):
    r'[*][*]'
    return t
# Reconoce eivisiones enteras
def t_DIVENT(t):
    r'[/][/]'
    return t


class MyApp(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent = parent, title = title, size = (1350,750))

        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap(os.getcwd() + "/Resources/icon.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)




        # COLORS
        # otros colores
        self.colorPurple = (224, 71, 158)
        self.colorLightBlue = (79, 200, 218)
        self.colorComent = (165, 197, 195)
        self.colorOrange = (255, 119, 0)
        self.colorGreen = (0, 179, 131)
        self.colorRed = (254, 74, 38)
        self.colorGrey = (166, 162, 162)
        self.colorWhite = (255, 255, 255)
        self.colorOrange2 = (251, 139, 36)
        self.colorBG = (20,18,18)  #54 72 101
        self.colorLabel = (93,253,203) # 38,216,205
        self.colorErrorBg = (255,145,164)
        self.colorLineNumberBorder = (32,32,32)
        self.colorLime = (222,255,79)
        self.colorBegin = (128,237,153)
        self.colorEnd = (87,204,153)
        self.colorLineNumber = (173,172,181)
        self.colorBorder = (40,40,40) #57,61,63
        self.colorLineCol = (40,40,40)
        self.colorLightOn = (52,58,64)


        # Paleta de colores para el idle

        self.colorTrue = (0, 179, 131)
        self.colorFalse = (254, 74, 38)
        self.colorsymbols = (244,140,6) #165,190,0 #244,140,6
        self.colorcomment = (125,133,151) # 151, 157, 172
        self.colorfunctions = (0,168,150)
        self.colorReserverd1 = (192,76,253)
        self.colorReserved2 = (2,128,144)
        self.colorReserved3 = (5,102,141)




        # TextControls

        self.textMain = wx.TextCtrl(self,style=wx.TE_MULTILINE|wx.TE_RICH|wx.BORDER_NONE,pos=(38,21),size=(1277,425))
        self.textConsole = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.TE_RICH|wx.BORDER_NONE|wx.TE_READONLY, pos=(52,465), size=(1259, 209))
        self.textConsole.AppendText("CubeCompiler [Version 1.0.0.0.1.0.1]\n(c) 2020 DD&D Corporation. All rights reserved.")
        self.textConsole.AppendText("\n\n")






        self.textMain.SetEvtHandlerEnabled(True)
        self.SetMaxSize((1350,750))
        self.SetMinSize((1350,750))

        # Paneles
        self.mainPanel = wx.Panel(self,1, pos = (39,22), size = (1276,424))
        self.mainPanel.SetBackgroundColour(self.colorWhite)

        self.panelLine1 = wx.Panel(self,1,pos = (0,20) ,size = (1350,1))
        self.panelLine1.SetBackgroundColour(self.colorBG)

        self.panelLine2 = wx.Panel(self,1,pos = (0,445) ,size = (1350,1))
        self.panelLine2.SetBackgroundColour(self.colorBG)

        self.panelLine3 = wx.Panel(self,1,pos = (0,460) ,size = (1350,1))
        self.panelLine3.SetBackgroundColour(self.colorBG)

        self.panelLine4 = wx.Panel(self,1,pos = (0,674) ,size = (1350,1))
        self.panelLine4.SetBackgroundColour(self.colorBG)

        self.panelLineVertical1 = wx.Panel(self,1,pos = (18,461) ,size = (1,214))
        self.panelLineVertical1.SetBackgroundColour(self.colorBG)

        self.panelLineVertical2 = wx.Panel(self,1,pos = (40,461) ,size=(1271, 214))
        self.panelLineVertical2.SetBackgroundColour(self.colorBG)


        self.currentDirectory = os.getcwd() + "/Files"
        self.currentFile = ""
        self.currenttext = ""
        self.pastLabelFileName = ""
        self.pastLabelNumberPosition = -1
        self.currentLabelFileName = ""
        self.flagSlider = False
        self.startEnd = [0,0]
        self.flagBgError = False
        self.textRestauration = ""
        self.currentLineNumber = self.textMain.PositionToXY(self.textMain.GetInsertionPoint())[2]
        self.pasPosxyList = self.textMain.PositionToXY(self.textMain.GetInsertionPoint())
        self.plusNumberLine = 0
        self.pastRowLen = 0
        self.maxNumberLine = 0
        self.minNumberLine = 0
        self.pasScrollPosition = 0

        # Lista de archivos

        self.filesList = self.readFilesList().split(",")
        self.contNewFiles = self.filesList[0]
        if self.contNewFiles == "":
            self.contNewFiles = "0"
        self.actualFontSize = 0

        # Reserved words
        self.rTrue = ["TRUE","T"]
        self.rFalse = ["FALSE","F"]
        self.symbols = ['COMMA', 'LCORCH', 'RCORCH', 'QUOTES', 'ASSIGN', "RPARENT", "LPARENT"]
        self.coment = ["PARENTCL", "PARENTCR", "MIL", "SEG", "MIN", "BEGIN", "END", "COMMENT"]
        self.functions = ["INSERT","NEG","DEL","DELETE","SHAPEF","SHAPEC","SHAPEA","RANGE","TYPE","BLINK","DELAY","LEN"]
        self.reservedWords1 = ["GLOBAL", "CALL"]
        self.reservedWords2 = ["PROCEDURE", "MAIN", "TIMER", "DIMFILAS", "DIMCOLUMNAS", "RANGOTIMER", "CUBO"]
        self.reservedWords3 = ["FOR","IF","ELSE","STEP","IN"]







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

        self.mainMenu.SetBackgroundColour(self.colorLime)
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


        self.textMain.Bind(wx.EVT_SET_CURSOR, self.focusOnTextCtrl)




        # Funcion boton

        self.Bind(wx.EVT_BUTTON,self.click1)

        # Labels

        self.lblFileName = wx.StaticText(self,-1,"",(1076,658))
        self.lblLineNumber = wx.StaticText(self,-1,"1",(1,21)) #38
        self.lblLineNumber.SetForegroundColour(self.colorLineNumber)


        # Set Size to a label
        self.fontNumberLabel = self.lblLineNumber.GetFont()
        self.fontNumberLabel.SetPointSize(12)
        self.lblLineNumber.SetFont(self.fontNumberLabel)
        self.fontNumberLabel.SetPointSize(12)

        self.lblBackG = wx.StaticText(self,-1," " + "\t"*15 +" ",(1184,658))
        self.lblBackG.SetBackgroundColour(self.colorBorder)
        # self.lblBackG.SetForegroundColour()


        self.fontNumberLabel.SetPointSize(9)
        self.lblLine = wx.StaticText(self, -1, "  line : ", (1184, 658))
        self.lblPosY = wx.StaticText(self,-1,"1",(1224,658))
        self.lblCol = wx.StaticText(self, -1, "col : ", (1254, 658))
        self.lblPosX = wx.StaticText(self, -1, "0", (1284, 658))


        self.lblpanel = wx.StaticText(self,-1,"\n......."*13,(19,462))
        self.lblpanel.SetForegroundColour(self.colorBorder)
        self.lblpanel.SetBackgroundColour(self.colorBorder)

        # Botones

        self.bmpRun = wx.Bitmap(os.getcwd() + "/Resources/buttonPlay.png", wx.BITMAP_TYPE_ANY)
        self.buttonRun = wx.BitmapButton(self.lblpanel, id=wx.ID_ANY, bitmap=self.bmpRun,
                                 size=(self.bmpRun.GetWidth() + 8, self.bmpRun.GetHeight() + 8), style = wx.NO_BORDER, pos = (0,5))
        self.buttonRun.SetBackgroundColour(self.colorBorder)

        self.buttonRun.Bind(wx.EVT_ENTER_WINDOW,self.buttonRunLightOn)
        self.buttonRun.Bind(wx.EVT_LEAVE_WINDOW, self.buttonRunLightOff)

        self.bmpCube = wx.Bitmap(os.getcwd() + "/Resources/cube1.png", wx.BITMAP_TYPE_ANY)
        self.buttonCube = wx.BitmapButton(self.lblpanel, id=wx.ID_ANY, bitmap=self.bmpCube,
                                 size=(self.bmpCube.GetWidth() + 8, self.bmpCube.GetHeight() + 8), style = wx.NO_BORDER, pos = (0,40))
        self.buttonCube.SetBackgroundColour(self.colorBorder)

        self.buttonCube.Bind(wx.EVT_ENTER_WINDOW,self.buttonCubeLightOn)
        self.buttonCube.Bind(wx.EVT_LEAVE_WINDOW, self.buttonCubeLightOff)



        # btn1 = wx.Button(self.lblpanel,-1,u"B",pos=(0,10),size=(20,20))
        # btn1.Bind(wx.EVT_BUTTON,self.click1)

        self.lblPosY.SetBackgroundColour(self.colorBorder)
        self.lblLine.SetBackgroundColour(self.colorBorder)
        self.lblCol.SetBackgroundColour(self.colorBorder)
        self.lblPosX.SetBackgroundColour(self.colorBorder)

        self.lblLine.SetFont(self.fontNumberLabel)
        self.lblPosY.SetFont(self.fontNumberLabel)
        self.lblCol.SetFont(self.fontNumberLabel)
        self.lblPosX.SetFont(self.fontNumberLabel)

        self.lblLine.SetForegroundColour(self.colorLabel)
        self.lblPosY.SetForegroundColour(self.colorLabel)
        self.lblCol.SetForegroundColour(self.colorLabel)
        self.lblPosX.SetForegroundColour(self.colorLabel)

        self.resetLabel("","NewFile.cbc")




        # Sliders

        # self.slideFont = wx.Slider(self,-1,12,12,28,(1000,0),(150,20))
        # self.Bind(wx.EVT_SLIDER,self.onSlider)
        # self.slideFont.Bind(wx.EVT_SET_FOCUS,self.focusOnSlider)
        # self.textConsole.Bind(wx.EVT_SET_CURSOR,self.focusOnTextCtrl)


        # Fuentes de Texto

        self.setFontSize(12)
        self.textMain.SetOwnBackgroundColour(self.colorBG)
        self.textConsole.SetBackgroundColour(self.colorBG)
        self.textMain.SetForegroundColour(self.colorWhite)
        self.textConsole.SetForegroundColour(self.colorLabel)


        # Sizer , Proporciona tamaño a los controles


        # sizer = wx.BoxSizer(wx.VERTICAL)
        # sizer.Add(self.textMain,2,wx.SHAPED|wx.LEFT|wx.UP,40)
        # sizer.Add(self.textConsole, 1, wx.SHAPED|wx.UP|wx.RIGHT|wx.LEFT,17)



        # self.SetSizer(sizer)

        # AceleratorTable

        randomPaste = wx.NewId()
        self.textMain.Bind(wx.EVT_MENU, self.test , id = randomPaste)
        accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('Q'), randomPaste)])
        self.textMain.SetAcceleratorTable(accel_tbl)

        # Show Frame


        self.Centre(1)
        self.SetBackgroundColour(self.textMain.GetBackgroundColour())
        self.SetBackgroundColour(self.colorLineNumberBorder)


        self.Show()

        # Thread for reserverd words

        self.t = threading.Thread(target = self.loop, args=())
        self.initThread()


    # FUNCTIONS
    def buttonRunLightOn(self,event):
        self.buttonRun.SetBackgroundColour(self.colorLightOn)
    def buttonRunLightOff(self,event):
        self.buttonRun.SetBackgroundColour(self.colorBorder)
    def buttonCubeLightOn(self,event):
        self.buttonCube.SetBackgroundColour(self.colorLightOn)
    def buttonCubeLightOff(self,event):
        self.buttonCube.SetBackgroundColour(self.colorBorder)

    def test(self,text):
        print("ctrl-v pressed")
        print("text: " + str(text))
    def readFilesList(self):
        listFilesFile = open(os.getcwd() + "/Files/Root/Files.txt", "r")
        txt = listFilesFile.read()
        listFilesFile.close()
        return txt
    def writeFilesList(self):
        self.filesList[0] = self.contNewFiles
        f = open(self.currentDirectory+"/Root/Files.txt","w")
        f.write(",".join(self.filesList))
        f.close()
    # Funcion para boton1, imprime lo que esté escrito en las entradas de texto
    def initThread(self):
        self.t.start()
    def loop(self):
        while 1:
            # self.changeReservedWords()
            self.changeReservedWords2()

    def click1(self,event):
        # list1 = ['"', ",", "{", "}", "=", "--", "(", ")", "[", "]"]
        # self.textMain.SetStyle(0,1,wx.TextAttr(wx.GREEN))
        # print(self.textMain.GetLineText(0)[0] in list1)
        # line = len(self.textMain.GetRange(0, self.textMain.GetInsertionPoint()).split("\n"))
        self.setErrorBackground(1)
        pixelpos = self.textMain.PositionToXY(self.textMain.GetInsertionPoint())
        print("pixelpos: ",pixelpos)
        text = ""
        for i in range(1,self.textMain.GetInsertionPoint()):
            text += str(i) + "\n"
        print(text)


    def insertList(self,event):
        self.textMain.AppendText("list" + str(self.contList) +"= [];\n")
        self.contList += 1
        self.changeTextColorWithoutClear()
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
        self.changeTextColorWithoutClear()
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


        self.textMain.AppendText("matriz3D" + str(self.contMatriz3) +"= "+ textFinal)
        self.contMatriz3 += 1
        self.changeTextColorWithoutClear()
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

            self.textMain.SetValue(txt)
            self.Disable()

            self.changeTextColor()

            self.Enable()

            self.currentLabelFileName = paths[0].split("\\")[-1]
            self.resetLabel(self.pastLabelFileName,self.currentLabelFileName)
            self.pastLabelFileName = self.currentLabelFileName

        dlg.Destroy()
    def resetLabel(self, number, newLabel):

        lbls = [widget for widget in self.GetChildren() if isinstance(widget, wx.StaticText)]

        for lbl in lbls:

            if number in lbl.GetLabel():
                text = "  File -> " + newLabel + "  "
                lbl.SetLabel(text)
                lbl.SetPosition((1183 - lbl.Size[0], 658))


                lbl.SetForegroundColour(self.colorLabel)
                lbl.SetBackgroundColour(self.colorBorder)

                break

    def saveFile(self,event):
        if  self.currentLabelFileName in self.filesList and self.currentLabelFileName != "":

            f = open(self.currentDirectory +"/" + self.currentLabelFileName,"w")
            f.write(self.textMain.GetValue())
            f.close()

        else:
            self.onSaveFile()
    def saveFileAs(self,event):
        self.onSaveFile()
    def onSaveFile(self):

        dlg = wx.FileDialog(
            self, message="Save file as ...",
            defaultDir=self.currentDirectory,
            defaultFile="New"+str(self.contNewFiles), wildcard=wildcard, style=wx.FD_SAVE
        )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            f = open(path,"w")
            f.write(self.textMain.GetValue())
            f.close()



            self.currentLabelFileName = path.split("\\")[-1]
            self.resetLabel(self.pastLabelFileName,self.currentLabelFileName)
            self.pastLabelFileName = self.currentLabelFileName


            self.filesList += [str(path.split("\\")[-1])]

            self.contNewFiles = str(int(self.contNewFiles) + 1)
            self.writeFilesList()

        dlg.Destroy()

    def newFile(self,event):

        if self.currentFile != "":
            f = open(self.currentFile, "w")
            f.write(self.textMain.GetValue())
            f.close()

        self.textMain.Clear()
        # self.currentDirectory = os.getcwd() + "/Files/New" + str(self.contNewFiles) +".cbc"
        # print("Current Directory -> " + self.currentDirectory)

        self.currentLabelFileName = "New"+str(self.contNewFiles)+".cbc"


        self.resetLabel(self.pastLabelFileName,self.currentLabelFileName)
        self.pastLabelFileName = self.currentLabelFileName
    def runFile(self,event):
        # TODO aqui se inserta la logica del compilador
        print("Running")
    def setFontSize(self,size):
        font = self.textMain.GetFont()
        font.SetPointSize(size)
        self.textMain.SetFont(font)

        self.actualFontSize = size
    def onSlider(self,event):
        self.setFontSize(self.slideFont.GetValue())
    def focusOnTextCtrl(self,event):
        self.flagSlider = False
    def focusOnSlider(self,event):
        self.flagSlider = True
    def writeColor(self,text,t):
        self.textMain.SetDefaultStyle(wx.TextAttr(t))
        self.textMain.WriteText(str(text))

        self.textMain.SetDefaultStyle(wx.TextAttr(wx.WHITE))
    def setStyleText(self,start,end,color):
        self.textMain.SetStyle(start, end, wx.TextAttr(color))
        self.textMain.SetDefaultStyle(wx.TextAttr(self.colorWhite))

    def setErrorBackground(self,line):
        text = self.textMain.GetValue()

        lista = text.split("\n")

        start = 1
        for i in range(0,line):
            start += len(lista[i])
        end = len(lista[line])
        
        self.startEnd = [start,end]
        self.flagBgError = not self.flagBgError

        self.textRestauration = lista[line]

        self.textMain.SetStyle(start,start + end,wx.TextAttr(self.colorWhite,self.colorErrorBg))
        self.textMain.SetDefaultStyle(wx.TextAttr(self.colorWhite,self.colorBG))

    def resetErrorBackground(self):

        self.textMain.SetStyle(self.startEnd[0],self.startEnd[1]+self.startEnd[0]+1,wx.TextAttr(self.colorWhite,self.colorBG))
        self.changeReservedWords(self.startEnd[0],self.textRestauration)
        self.textMain.SetDefaultStyle(wx.TextAttr(self.colorWhite,self.colorBG))


    def changeReservedWords(self,pos,text):

        lexer = lex.lex()
        lexer.input(text)
        posInit = pos

        while 1:
            tok = lexer.token()
            if not tok:
                break
            else:
                if tok != None:
                    if tok.type in self.rTrue:
                        self.setStyleText(tok.lexpos+posInit,tok.lexpos + len(tok.value)+posInit, self.colorTrue)
                    elif tok.type in self.rFalse:
                        self.setStyleText(tok.lexpos+posInit, tok.lexpos + len(tok.value)+posInit, self.colorFalse)
                    elif tok.type in self.symbols:
                        self.setStyleText(tok.lexpos+posInit, tok.lexpos + len(tok.value)+posInit, self.colorsymbols)
                    elif tok.type in self.coment:
                        self.setStyleText(tok.lexpos+posInit, tok.lexpos + len(tok.value)+posInit, self.colorcomment)
                    elif tok.type in self.functions:
                        self.setStyleText(tok.lexpos+posInit, tok.lexpos + len(tok.value)+posInit, self.colorfunctions)
                    elif tok.type in self.reservedWords1:
                        self.setStyleText(tok.lexpos+posInit, tok.lexpos + len(tok.value)+posInit, self.colorReserverd1)
                    elif tok.type in self.reservedWords2:
                        self.setStyleText(tok.lexpos+posInit, tok.lexpos + len(tok.value)+posInit, self.colorReserved2)
                    elif tok.type in self.reservedWords3:
                        self.setStyleText(tok.lexpos+posInit, tok.lexpos + len(tok.value)+posInit, self.colorReserved3)
                    elif tok.type == "ID":
                        self.setStyleText(tok.lexpos+posInit, tok.lexpos + len(tok.value)+posInit, self.colorWhite)
                    elif tok.type == "DOT" or tok.type == "SEMICOLON":
                        self.setStyleText(tok.lexpos+posInit, tok.lexpos + len(tok.value)+posInit, self.colorWhite)
                    elif tok.type == "INT":
                        self.setStyleText(tok.lexpos + posInit, tok.lexpos + len(str(tok.value)) + posInit, self.colorWhite)


    def changeReservedWords2(self):

        scrollPos = self.textMain.GetScrollPos(1)//20
        curpos = self.textMain.GetInsertionPoint()
        lxy = self.textMain.PositionToXY(curpos)

        if lxy[1] != self.pasPosxyList[1] or lxy[2] != self.pasPosxyList[2]:
            self.pasPosxyList = lxy
            self.lblPosY.SetLabel(str(lxy[2]+1))
            self.lblPosX.SetLabel(str(lxy[1]))

        if self.flagSlider:
            self.changeTextColorWithoutClear()

        if lxy[2] != self.pastLabelNumberPosition:

            newRowLen = len(self.textMain.GetValue().split("\n"))

            self.plusNumberLine = lxy[2]-20

            self.pastLabelNumberPosition = lxy[2]
            text = ""

            if newRowLen != self.pastRowLen:


                # TODO crear caso para cuando se borra , self.pasRowLen > newRowLen

                if newRowLen > self.pastRowLen: #or newRowLen <= self.pastRowLen:
                    if lxy[2] != self.maxNumberLine and self.maxNumberLine > 20:
                        posInit = self.maxNumberLine - 20
                        cont = 0
                        self.minNumberLine = posInit +1
                        for i in range(self.minNumberLine, newRowLen):
                            cont+=1
                            if text == "":
                                text += " " * (4 - len(str(i))) + str(i)
                            else:
                                text +=  "\n" + " "*(4-len(str(i))) + str(i)
                            if cont == 20:
                                self.maxNumberLine = i
                                break
                    elif lxy[2] + 1 > 20:
                        cont = 0
                        self.minNumberLine = self.plusNumberLine + 1
                        for i in range(self.minNumberLine + 1, newRowLen+2):
                            cont+=1
                            if text == "":

                                text += " "*(4-len(str(i))) + str(i)
                            else:
                                text += "\n" + " " * (4 - len(str(i))) + str(i)
                            if cont == 20:
                                self.maxNumberLine = i
                                break

                    else:
                        cont = 0
                        self.minNumberLine = 1
                        for i in range(self.minNumberLine, newRowLen + 1):
                            cont += 1
                            if text == "":
                                text +=  " "*(4-len(str(i))) + str(i)
                            else:
                                text += "\n" + " " * (4 - len(str(i))) + str(i)
                            self.maxNumberLine = i
                            if cont == 20:
                                break
                elif newRowLen < self.pastRowLen:
                    print("Borrando")

                     # TODO Logica para el borrado

                    cont = 0
                    for i in range(self.minNumberLine , len(self.textMain.GetValue().split("\n")) + 1):
                        cont += 1
                        if text == "":
                            text += " "*(4-len(str(i))) + str(i)
                        else:
                            text += "\n" + " " * (4 - len(str(i))) + str(i)
                        self.maxNumberLine = i
                        if cont == 20:
                            break
                    print("menor")

                self.pastRowLen = newRowLen
                self.lblLineNumber.SetLabel("" + text)

            # Aca entra solo en el movimiento del scrol pero sin cambio de posicion del mouse

        elif lxy[2] == self.pastLabelNumberPosition and scrollPos != self.pasScrollPosition:
            text = ""
            if scrollPos > self.pasScrollPosition:
                dif = scrollPos - self.pasScrollPosition
                self.minNumberLine += dif

                cont = 0
                for i in range(self.minNumberLine , len(self.textMain.GetValue().split("\n")) + 2 ):
                    cont+=1
                    if text == "":

                        text += " "*(4-len(str(i))) + str(i)
                    else:
                        text += "\n" + " " * (4 - len(str(i))) + str(i)

                    if cont == 20:
                        self.maxNumberLine = i
                        break

                print("down")
            elif scrollPos < self.pasScrollPosition:
                print("up")

                dif = self.pasScrollPosition - scrollPos
                print("DIF", dif)
                self.minNumberLine -= dif

                if scrollPos == 0:
                    self.minNumberLine = 1

                cont = 0
                for i in range(self.minNumberLine , len(self.textMain.GetValue().split("\n")) + 2):
                    cont += 1
                    if text == "":

                        text +=  " "*(4-len(str(i))) + str(i)
                    else:
                        text += "\n" + " " * (4 - len(str(i))) + str(i)

                    if cont == 20:
                        self.maxNumberLine = i
                        break
            self.pasScrollPosition = scrollPos
            self.lblLineNumber.SetLabel("" + text)


        if self.textMain.GetValue() != self.currenttext or len(self.textMain.GetValue()) != len(self.currenttext):
            if self.flagBgError:
                self.flagBgError = not self.flagBgError
                self.resetErrorBackground()

            if self.textMain.GetValue() != "":

                curPos = self.textMain.GetInsertionPoint()
                linenumber = self.textMain.PositionToXY(curPos)
                lineText = self.textMain.GetLineText(linenumber[2])

                text = self.textMain.GetValue()
                lexer = lex.lex()
                lexer.input(lineText)
                self.currenttext = text
                posInit = curPos - linenumber[1]

                if "-" in lineText:
                    self.changeReservedWords(posInit,lineText)
                else:

                    list1 = ['"',",","{","}","=","--","(",")","[","]"," "]
                    listNum = "1234567890"
                    list2 = "abcdefghijklmnñopqrstuvwxyzCALL"

                    pack = []

                    if len(lineText) != 0:
                        if lineText[linenumber[1]-1] in list1 or lineText[linenumber[1]-1] in listNum:
                            pack = (linenumber[1]-1,linenumber[1],lineText[linenumber[1]-1:linenumber[1]],posInit)
                        
                        else:

                            s = linenumber[1] -1

                            e = linenumber[1]
                            if s <= 0:
                                s = 0
                            if e >= len(lineText):
                                e = len(lineText)
                            if s-1 >= 0:
                                while s != 0 and lineText[s] in list2 and lineText[s-1] not in list1:
                                    s-=1
                            while e != len(lineText) and lineText[e] in list2:
                                e+=1
                            pack = (s,e,lineText[s:e],posInit)


                        self.changeWordColor(pack)

        # Test when an enter has inserted
            #curPos = self.textMain.GetInsertionPoint()
            #linenumber = self.textMain.PositionToXY(curPos)
            #lineText = self.textMain.GetLineText(linenumber[2]-1)
            #print("LENLINTEXTPrevious" + str(len(lineText)))
            #if lineText.endswith("{") and self.textMain.PositionToXY(self.textMain.GetInsertionPoint())[2] > self.currentLineNumber :
                    #self.textMain.AppendText("\t")
                    #self.textMain.AppendText("\n}")
                    #self.currentLineNumber = self.textMain.PositionToXY(self.textMain.GetInsertionPoint())[2]
                    #self.textMain.SetInsertionPoint(len(lineText)+4 + (4*lineText.count("\t")))
                    #self.textMain.Refresh()
                    #self.changeTextColorWithoutClear()


    def changeWordColor(self,tuple):

        lexer = lex.lex()
        lexer.input(tuple[2])

        while 1:
            tok = lexer.token()
            if not tok:
                break
            else:
                if tok != None:
                    if tok.type in self.rTrue:
                        self.setStyleText(tuple[0] + tuple[3], tuple[1] + tuple[3], self.colorTrue)
                    elif tok.type in self.rFalse:
                        self.setStyleText(tuple[0] + tuple[3], tuple[1] + tuple[3],self.colorFalse)
                    elif tok.type in self.symbols:
                        self.setStyleText(tuple[0] + tuple[3], tuple[1] + tuple[3],self.colorsymbols)
                    elif tok.type in self.coment:
                        self.setStyleText(tuple[0] + tuple[3], tuple[1] + tuple[3], self.colorcomment)
                    elif tok.type in self.functions:
                        self.setStyleText(tuple[0] + tuple[3], tuple[1] + tuple[3], self.colorfunctions)
                    elif tok.type in self.reservedWords1:
                        self.setStyleText(tuple[0] + tuple[3], tuple[1] + tuple[3], self.colorReserverd1)
                    elif tok.type in self.reservedWords2:
                        self.setStyleText(tuple[0] + tuple[3], tuple[1] + tuple[3], self.colorReserved2)
                    elif tok.type in self.reservedWords3:
                        self.setStyleText(tuple[0] + tuple[3], tuple[1] + tuple[3], self.colorReserved3)
                    elif tok.type == "ID":
                        self.setStyleText(tuple[0] + tuple[3], tuple[1] + tuple[3], self.colorWhite)
                    elif tok.type == "DOT" or tok.type == "SEMICOLON":
                        self.setStyleText(tuple[0] + tuple[3], tuple[1] + tuple[3], self.colorWhite)
                    elif tok.type == "INT":
                        self.setStyleText(tuple[0] + tuple[3], tuple[1] + tuple[3],self.colorWhite)


# Creando funcion que reconoce solo el texto nuevo para colorearlo
    def changeTextColor(self):

        text = self.textMain.GetValue()
        self.textMain.Clear()
        lexer = lex.lex()
        lexer.input(text)

        while 1:
            tok = lexer.token()
            if not tok:
                break
            else:
                if tok != None:
                    if tok.type in self.rTrue:
                        self.writeColor(tok.value,self.colorTrue)
                    elif tok.type in self.rFalse:
                        self.writeColor(tok.value, self.colorFalse)
                    elif tok.type in self.symbols:
                        self.writeColor(tok.value, self.colorsymbols)
                    elif tok.type in self.coment:
                        self.writeColor(tok.value, self.colorcomment)
                    elif tok.type in self.functions:
                        self.writeColor(tok.value, self.colorfunctions)
                    elif tok.type in self.reservedWords1:
                        self.writeColor(tok.value, self.colorReserverd1)
                    elif tok.type in self.reservedWords2:
                        self.writeColor(tok.value, self.colorReserved2)
                    elif tok.type in self.reservedWords3:
                        self.writeColor(tok.value, self.colorReserved3)
                    else:
                        self.writeColor(tok.value, self.colorWhite)

    def changeTextColorWithoutClear(self):

        text = self.textMain.GetValue()

        lexer = lex.lex()
        lexer.input(text)

        while 1:
            tok = lexer.token()
            if not tok:
                break
            else:
                if tok != None:
                    if tok.type in self.rTrue:
                        self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), self.colorTrue)
                    elif tok.type in self.rFalse:
                        self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), self.colorFalse)
                    elif tok.type in self.symbols:
                        self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), self.colorsymbols)
                    elif tok.type in self.coment:
                        self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), self.colorcomment)
                    elif tok.type in self.functions:
                        self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), self.colorfunctions)
                    elif tok.type in self.reservedWords1:
                        self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), self.colorReserverd1)
                    elif tok.type in self.reservedWords2:
                        self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), self.colorReserved2)
                    elif tok.type in self.reservedWords3:
                        self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), self.colorReserved3)
                    elif tok.type == "ID" or tok.type == "SEMICOLON" or tok.type == "DOT":
                        self.setStyleText(tok.lexpos, tok.lexpos + len(tok.value), self.colorWhite)
                    elif tok.type == "INT":
                        self.setStyleText(tok.lexpos, tok.lexpos + len(str((tok.value))), self.colorWhite)

if __name__ == '__main__':
    app = wx.App()
    frame = MyApp(None,"CubeCompiler")
    app.MainLoop()