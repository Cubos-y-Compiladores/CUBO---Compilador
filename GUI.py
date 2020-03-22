import wx
from functools import partial

class MyApp(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent = parent , title = title, size = (1200,750))
        # TODO arreglar por qué siempre cubre toda la pantalla
        self.textMain = wx.TextCtrl(self,style=wx.TE_MULTILINE,pos=(0,0),size=(1,1))
        self.textConsole = wx.TextCtrl(self, style=wx.TE_MULTILINE, pos=(0, 0), size=(1, 1))
        # VariablesContadores
        self.contList = 0
        self.contMatriz2 = 0
        self.contMatriz3 = 0

        # Barra Menu
        self.mainMenu = wx.MenuBar()

        # SubMenus
        self.subMenuOpen = wx.Menu()
        self.subMenuFile = wx.Menu()
        self.subMenuInsert = wx.Menu()
        self.subMenuRun = wx.Menu()
        # SubMenusInsert
        self.subMenuMat2D = wx.Menu()
        self.subMenuMat3D = wx.Menu()
        # Agregando a los submenus
        self.subOpenCBC = self.subMenuOpen.Append(-1,"File.cbc\tCtrl-C")
        self.subOpenTXT = self.subMenuOpen.Append(-1, "File.txt\tCtrl-T")
        self.subMenuFile.AppendSubMenu(self.subMenuOpen,"Open")



        self.subNew = self.subMenuFile.Append(-1,"New\tCtrl-N")
        self.subSave = self.subMenuFile.Append(-1, "Save\tCtrl-S")
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
        self.Bind(wx.EVT_MENU, self.openFileCBC , self.subOpenCBC)
        self.Bind(wx.EVT_MENU, self.openFileTXT, self.subOpenTXT)
        self.Bind(wx.EVT_MENU, self.saveFile, self.subSave)
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


        # Fuentes de Texto
        font = self.textMain.GetFont()
        font.SetPointSize(12)
        self.textMain.SetFont(font)
        self.textConsole.SetFont(font)


        # Probando los estilos de texto (color)
        self.textMain.SetOwnBackgroundColour((73,73,73))
        # self.textMain.SetStyle(0,20,wx.TextAttr(wx.WHITE))
        self.textMain.SetDefaultStyle(wx.TextAttr(wx.WHITE))

        self.textMain.SetDefaultStyle(wx.TextAttr(wx.WHITE))
        # a = textMain.XYToPosition(2,2)
        # print(a)
        self.textConsole.SetBackgroundColour((73,73,73))
        # textConsole.SetDefaultStyle(wx.TextAttr(wx.BLUE))


        # Funciona para que cuando se inicie el idle ya tenga las constantes de configuración
        # Se podria generar un error en caso de que no exisan esas palabras
        # textMain.AppendText("Hello World")

        # Sizer , Proporciona tamaño a los controles
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.textMain,2,wx.EXPAND|wx.LEFT,20)
        sizer.Add(self.textConsole, 1, wx.EXPAND|wx.LEFT|wx.UP,10)
        self.SetSizer(sizer)
        self.Centre(1)
        self.SetBackgroundColour(self.textMain.GetBackgroundColour())
        self.Show()

    # Funcion para boton1, imprime lo que esté escrito en las entradas de texto
    def click1(self,event):
        print("Input1: " + str(self.textMain.GetValue()))
        print("Input2: " + str(self.textConsole.GetValue()))
    def insertList(self,event):
        self.textMain.AppendText("list" + str(self.contList) +"= [];\n")
        self.contList += 1
    def insertMatriz2D(self,number,event):

        text = "["
        for i in range(number-1):
            text+="[],\n\t     "

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
        textFinal = "["

        for i in range(number-1):
            text = "["

            for j in range(number - 1):
                text += "[],"


            text += "[]"
            text += "]"
            textFinal += text+",\n\t     "

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
    def openFileCBC(self,event):
        print("Opened cbc")
    def openFileTXT(self):
        print("Opened txt")
    def newFile(self,event):
        print("New file")
    def saveFile(self,event):
        print("Saved")

    def runFile(self,event):
        print("Running")

if __name__ == '__main__':
    app = wx.App()
    frame = MyApp(None,"Test")
    app.MainLoop()