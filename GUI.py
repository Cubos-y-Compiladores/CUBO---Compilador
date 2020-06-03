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
import QuickCube
import wx.stc
import Frame


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
            'delete':'DELETE',
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

        self.Bind(wx.EVT_CLOSE,self.closeWindow)

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
        self.colorBG = (20,18,18)
        self.colorLabel = (93,253,203)
        self.colorErrorBg = (255,145,164)
        self.colorLineNumberBorder = (32,32,32)
        self.colorLime = (222,255,79)
        self.colorBegin = (128,237,153)
        self.colorEnd = (87,204,153)
        self.colorLineNumber = (173,172,181)
        self.colorBorder = (40,40,40)
        self.colorLineCol = (40,40,40)
        self.colorLightOn = (52,58,64)



        # Paleta de colores para el idle

        self.colorTrue = (51,255,255)
        self.colorFalse = (255,87,20)
        self.colorsymbols = (244,140,6) #165,190,0 #244,140,6
        self.colorcomment = (2,255,194) # 151, 157, 172
        self.colorfunctions = (240,246,0)
        self.colorReserverd1 = (192,76,253)
        self.colorReserved2 = (175,43,191)
        self.colorReserved3 = (100,223,223)

        # TextControls

        self.textConsole = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.TE_RICH|wx.BORDER_NONE|wx.TE_READONLY, pos=(52,465), size=(1259, 209))
        self.textConsole.AppendText("CubeCompiler [Version 1.0.0.0.1.0.1]\n(c) 2020 DD&D Corporation. All rights reserved.")
        self.textConsole.AppendText("\n\n")


        self.SetMaxSize((1350,750))
        self.SetMinSize((1350,750))


        # STYLEDTEXTCTRL
        self.textMain = wx.stc.StyledTextCtrl(self,1,pos = (18,22),size=(1288, 424), style = wx.TE_MULTILINE | wx.TE_WORDWRAP | wx.BORDER_NONE)
        self.textMain.StyleSetSpec(wx.stc.STC_P_DEFAULT, 'fore:#ffffff,back:#141212')
        self.textMain.StyleSetSpec(wx.stc.STC_STYLE_INDENTGUIDE, 'fore:#323232,back:#141212')


        self.textMain.SetMargins(9,9)
        self.textMain.SetMarginType(1,wx.stc.STC_MARGIN_NUMBER)
        self.textMain.SetMarginWidth(wx.stc.STC_MARGIN_NUMBER,26)
        self.textMain.StyleSetSpec(11,'fore:#ffffff,back:#323232')
        self.textMain.StyleSetBackground(wx.stc.STC_STYLE_DEFAULT,self.colorBG)
        self.textMain.SetIndent(8)
        self.textMain.SetLexer(wx.stc.STC_LEX_CONTAINER)
        self.textMain.SetStyleBits(5)

        self.textMain.SetIndentationGuides(1)
        self.textMain.SetUseHorizontalScrollBar(False)
        self.textMain.SetUseVerticalScrollBar(False)


        # Paleta de colores

        self.textMain.StyleSetSpec(1, 'fore:#33ffff,back:#141212')
        self.textMain.StyleSetSpec(2, 'fore:#ff5714,back:#141212')
        self.textMain.StyleSetSpec(3, 'fore:#f49006,back:#141212')
        self.textMain.StyleSetSpec(4, 'fore:#02ffc2,back:#141212')
        self.textMain.StyleSetSpec(5, 'fore:#f0f600,back:#141212')
        self.textMain.StyleSetSpec(6, 'fore:#c04cfd,back:#141212')
        self.textMain.StyleSetSpec(7, 'fore:#af2bbf,back:#141212')
        self.textMain.StyleSetSpec(8, 'fore:#64dfdf,back:#141212')
        self.textMain.StyleSetSpec(9, 'fore:#141212,back:#141212')

        self.textMain.StyleSetSpec(12, 'fore:#ffffffff,back:#ffffffff')


        self.textMain.StyleSetSpec(wx.stc.STC_STYLE_LINENUMBER, 'fore:#323232,back:#141212')

        # self.textMain.StyleSetSpec(10, 'fore:#ffffff,back:#141212')


        # FINSTYLEDTEXTCTRL

        # Paneles

        self.panelLine1 = wx.Panel(self,1,pos = (0,21) ,size = (1350,1))
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
        self.mainDirectory = os.getcwd()
        self.currentFile = ""
        self.currenttext = ""
        self.pastLabelFileName = ""
        self.pastLabelNumberPosition = 1
        self.currentLabelFileName = ""
        self.flagSlider = False
        self.startEnd = [0,0]
        self.flagBgError = False
        self.textRestauration = ""
        self.currentLineNumber = self.textMain.PositionToXY(self.textMain.GetInsertionPoint())[2]
        self.pasPosxyList = self.textMain.PositionToXY(self.textMain.GetInsertionPoint())
        self.plusNumberLine = 0
        self.pastRowLen = 1
        self.maxNumberLine = 2
        self.minNumberLine = 1
        self.pasScrollPosition = 0

        self.loadingPath = None
        self.flagNeedLoading = False
        self.flagTemp = False

        self.flagO = False
        self.flagLoop = True


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
        self.space = ["SPACE"]

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

        # Labels
        self.lblFileName = wx.StaticText(self,-1,"",(1076,658))

        self.lblLoading = wx.StaticText(self,-1,"", (55,500)) #55 500
        self.lblLoading.SetBackgroundColour(self.colorBG)
        self.lblLoading.SetForegroundColour(self.colorLime)

        # Set Size to a label
        self.fontNumberLabel = self.lblFileName.GetFont()
        # self.fontNumberLabel.SetPointSize(12)
        # self.lblLineNumber.SetFont(self.fontNumberLabel)
        self.fontNumberLabel.SetPointSize(12)


        self.lblBackG = wx.StaticText(self,-1," " + "\t"*15 +" ",(1184,658))
        self.lblBackG.SetBackgroundColour(self.colorBorder)
        # self.lblBackG.SetForegroundColour()

        # self.fontNumberLabel.SetPointSize(9)
        self.lblLine = wx.StaticText(self, -1, "  line : ", (1184, 658))
        self.lblPosY = wx.StaticText(self,-1,"1",(1224,658))
        self.lblCol = wx.StaticText(self, -1, "col : ", (1254, 658))
        self.lblPosX = wx.StaticText(self, -1, "0", (1284, 658))

        self.lblpanel = wx.StaticText(self,-1,"\n......."*13,(19,462))
        self.lblpanel.SetForegroundColour(self.colorBorder)
        self.lblpanel.SetBackgroundColour(self.colorBorder)

        self.lblPosY.SetBackgroundColour(self.colorBorder)
        self.lblLine.SetBackgroundColour(self.colorBorder)
        self.lblCol.SetBackgroundColour(self.colorBorder)
        self.lblPosX.SetBackgroundColour(self.colorBorder)

        self.fontNumberLabel.SetPointSize(9)
        self.lblLine.SetFont(self.fontNumberLabel)
        self.lblPosY.SetFont(self.fontNumberLabel)
        self.lblCol.SetFont(self.fontNumberLabel)
        self.lblPosX.SetFont(self.fontNumberLabel)

        self.lblLine.SetForegroundColour(self.colorLabel)
        self.lblPosY.SetForegroundColour(self.colorLabel)
        self.lblCol.SetForegroundColour(self.colorLabel)
        self.lblPosX.SetForegroundColour(self.colorLabel)
        self.resetLabel("","NewFile.cbc")
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
        self.buttonCube.Bind(wx.EVT_BUTTON,self.openQuickCube)

        # Fuentes de Texto
        self.setFontSize(12)
        self.textMain.SetOwnBackgroundColour(self.colorBG)
        self.textConsole.SetBackgroundColour(self.colorBG)
        self.textMain.SetForegroundColour(self.colorWhite)
        self.textConsole.SetForegroundColour(self.colorLabel)
        # AceleratorTable
        randomPaste = wx.NewId()

        self.textMain.Bind(wx.EVT_MENU, self.test , id = randomPaste)

        accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('V'), randomPaste)])
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
    def closeWindow(self,event):
        self.flagLoop = False
        self.Destroy()
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
        while self.flagLoop:
            self.changeReservedWords2()

    def openQuickCube(self,event):
        self.Disable()
        Frame.Frame("Quick Cube",self,self.mainDirectory)

        # quickCube = QuickCube.matrizFrame("QuickCube")

    def insertList(self,event):
        self.textMain.AppendText("list" + str(self.contList) +"= [];\n")
        self.contList += 1
        self.changeTextColor()

    def insertMatriz2D(self,number,event):
        text = " ["
        for i in range(number-1):
            text+="[],\n\t\t"
        text += "[]];\n"
        self.textMain.AppendText("matriz2D" + str(self.contMatriz2) +"= "+ text)
        self.contMatriz2 += 1
        self.changeTextColor()

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
        self.changeTextColor()

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

            self.loadingPath = dlg.GetPaths()
            self.lblLoading.SetLabel("Loading . . .")
            self.flagNeedLoading = True

        dlg.Destroy()

    def loading(self):

        self.textMain.SetValue("")
        self.currentFile = self.loadingPath[0]
        f = open(self.loadingPath[0], "r")
        txt = f.read()
        f.close()

        self.textMain.Freeze()
        self.textMain.SetValue(txt)
        self.Disable()
        self.changeTextColor()
        self.textMain.Thaw()
        self.Enable()
        self.textMain.SetInsertionPoint(0)
        self.currentLabelFileName = self.loadingPath[0].split("\\")[-1]
        self.resetLabel(self.pastLabelFileName, self.currentLabelFileName)
        self.pastLabelFileName = self.currentLabelFileName
        self.flagTemp = False
        self.lblLoading.SetLabel("")
        self.flagNeedLoading = False
        self.loadingPath = None


    def loadingPoints(self,loadingText):
        if loadingText.count(".") == 0:
            return "Loading ."
        if loadingText.count(".") == 1:
            return "Loading . ."
        if loadingText.count(".") == 2:
            return "Loading . . ."
        if loadingText.count(".") == 3:
            return "Loading"
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
        if self.currentLabelFileName in self.filesList and self.currentLabelFileName != "":

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

        self.textMain.ClearAll()
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

    def loadingEffect(self):
        text = "Loading"
        while self.flagTemp:
            time.sleep(0.5)
            text = self.loadingPoints(text)
            self.lblLoading.SetLabel(text)
        self.lblLoading.SetLabel("")

    def getWordText(self,linenumber,lineText):
        list1 = ['"', ",", "{", "}", "=", "--", "(", ")", "[", "]", " "]
        list2 = "abcdefghijklmnñopqrstuvwxyzCALLTF_"
        s = linenumber[1] - 1
        e = linenumber[1]
        if s <= 0:
            s = 0
        if e >= len(lineText):
            e = len(lineText)
        if s - 1 >= 0:
            while s != 0 and lineText[s] in list2 and lineText[s - 1] not in list1:
                s -= 1
        while e != len(lineText) and lineText[e] in list2:
            e += 1
        s = s-1
        if s < 0 :
            s = 0
        p = (lineText[s:e],s,e)
        return p

    def changeReservedWords2(self):

        if self.flagNeedLoading:
            self.flagTemp = True
            threading.Thread(target=self.loading).start()
            self.loadingEffect()
        curpos = self.textMain.GetInsertionPoint()
        lxy = self.textMain.PositionToXY(curpos)
        if lxy[1] != self.pasPosxyList[1] or lxy[2] != self.pasPosxyList[2]:
            self.pasPosxyList = lxy
            self.lblPosY.SetLabel(str(lxy[2]+1))
            self.lblPosX.SetLabel(str(lxy[1]))


        # TODO : aqui hay que meter la funcion con la logica de colores
        if( self.textMain.GetValue() != self.currenttext or len(self.textMain.GetValue()) != len(self.currenttext)) and self.textMain.GetValue() != "":

            if self.textMain.GetValue() != "":
                curPos = self.textMain.GetInsertionPoint()
                linenumber = self.textMain.PositionToXY(curPos)
                print(linenumber)
                lineText = self.textMain.GetLineText(linenumber[2])
                posInit = curPos - linenumber[1]
                if "-" in lineText:
                    self.getWordColor(lineText, posInit)
                else:

                    list1 = ['"', ",", "{", "}", "=", "--", "(", ")", "[", "]", " "]
                    listNum = "1234567890"
                    list2 = "abcdefghijklmnñopqrstuvwxyzCALL_"
                    list3 = ["F", "T"]

                    if len(lineText) != 0:
                        word = self.getWordText(linenumber, lineText)

                        print(lineText[linenumber[1] - 1])

                        if (lineText[linenumber[1] - 1] in list1 or lineText[linenumber[1] - 1] in listNum or word[
                            0] in list3) and lineText[linenumber[1] - 1] != "_":
                            pack = (
                            linenumber[1], linenumber[1] + 1, lineText[linenumber[1]:linenumber[1] + 1], posInit + 1)
                        else:
                            if ("_" in word[0]):
                                pack = (word[1], word[2], word[0], posInit)
                            else:
                                s = linenumber[1] - 1
                                e = linenumber[1]
                                if s <= 0:
                                    s = 0
                                if e >= len(lineText):
                                    e = len(lineText)
                                if s - 1 >= 0:
                                    while s != 0 and lineText[s] in list2 and lineText[s - 1] not in list1:
                                        s -= 1
                                while e != len(lineText) and lineText[e] in list2:
                                    e += 1
                                print("word", lineText[s:e])
                                print("start", s)
                                print("end", e)
                                pack = (s, e, lineText[s:e], posInit)

                        self.getWordColor(pack[2], pack[0] + posInit)

            self.currenttext = self.textMain.GetValue()

# Creando funcion que reconoce solo el texto nuevo para colorearlo
    def getWordColor(self,word,posInit):

        lexer = lex.lex()
        lexer.input(word)
        while 1:
            tok = lexer.token()
            if not tok:
                break
            else:
                if tok != None:
                    if tok.type in self.rTrue:
                        style = 1
                    elif tok.type in self.rFalse:
                        style = 2
                    elif tok.type in self.symbols:
                        style = 3
                    elif tok.type in self.coment:
                        style = 4
                    elif tok.type in self.functions:
                        style = 5
                    elif tok.type in self.reservedWords1:
                        style = 6
                    elif tok.type in self.reservedWords2:
                        style = 7
                    elif tok.type in self.reservedWords3:
                        style = 8
                    else:
                        style = 10

                    if style != 10:
                        self.textMain.StartStyling(posInit, style)
                        self.textMain.SetStyling(len(str(tok.value)), style)

    def changeTextColor(self):

        self.textMain.StyleSetSpec(1, 'fore:#33ffff,back:#141212')
        self.textMain.StyleSetSpec(2, 'fore:#ff5714,back:#141212')
        self.textMain.StyleSetSpec(3, 'fore:#f49006,back:#141212')
        self.textMain.StyleSetSpec(4, 'fore:#02ffc2,back:#141212')
        self.textMain.StyleSetSpec(5, 'fore:#f0f600,back:#141212')
        self.textMain.StyleSetSpec(6, 'fore:#c04cfd,back:#141212')
        self.textMain.StyleSetSpec(7, 'fore:#af2bbf,back:#141212')
        self.textMain.StyleSetSpec(8, 'fore:#64dfdf,back:#141212')
        self.textMain.StyleSetSpec(9, 'fore:#141212,back:#141212')


        self.textMain.StyleSetSpec(wx.stc.STC_STYLE_LINENUMBER, 'fore:#323232,back:#141212')
        self.textMain.StyleSetSpec(10, 'fore:#ffffff,back:#141212')

        text = self.textMain.GetValue()
        lexer = lex.lex()
        lexer.input(text)

        style = 0
        while 1:
            tok = lexer.token()
            if not tok:
                break
            else:
                if tok != None:
                    if tok.type in self.rTrue:
                        style = 1
                    elif tok.type in self.rFalse:
                        style = 2
                    elif tok.type in self.symbols:
                        style = 3
                    elif tok.type in self.coment:
                        style = 4
                    elif tok.type in self.functions:
                        style = 5
                    elif tok.type in self.reservedWords1:
                        style = 6
                    elif tok.type in self.reservedWords2:
                        style = 7
                    elif tok.type in self.reservedWords3:
                        style = 8
                    else:
                        style = 10

                    pos = tok.lexpos
                    self.textMain.StartStyling(pos, style)
                    self.textMain.SetStyling(len(str(tok.value)), style)


if __name__ == '__main__':
    app = wx.App()
    frame = MyApp(None,"CubeCompiler")
    app.MainLoop()