import wx
import wx.lib.scrolledpanel
import os
class matrizFrame(wx.Frame):
    def __init__(self, title,col,row,height,mainWindow,mainDirectory, parent=None):
        wx.Frame.__init__(self, parent=parent, title=title, size=(337, 300))

        icon = wx.Icon()
        self.mainDirectory = mainDirectory
        icon.CopyFromBitmap(wx.Bitmap(self.mainDirectory + "/Resources/icon.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        self.Bind(wx.EVT_CLOSE, self.closeWindow)
        self.mainWindow = mainWindow
        self.colorTrue = (2,195,154)
        self.colorFalse = (231,29,54)
        self.colorBG = (20,18,18)
        self.colorLabel = (93,253,203)
        self.colorBorder = (40,40,40)
        self.colorWhite = (255, 255, 255)
        self.colorLime = (222, 255, 79)
        self.colorLineNumberBorder = (32, 32, 32)
        self.SetMaxSize((337,300))
        self.SetMinSize((337,300))
        self.SetBackgroundColour("black")
        self.matrices = []
        self.currentMatrix = None
        self.btnMatrix = []

        self.panel3 = wx.Panel(self, size=(120, 60), pos=(0, 201), style=wx.NO_BORDER)
        self.panel3.SetBackgroundColour(self.colorBorder)

        self.panel1 = wx.lib.scrolledpanel.ScrolledPanel(self, -1, size=(120, 200), pos=(0, 0),style=wx.NO_BORDER)
        self.panel1.SetupScrolling(scroll_y=True)
        self.panel1.SetBackgroundColour(self.colorBorder)

        self.panel2 = wx.Panel(self, size=(200, 200), pos=(122, 2), style=wx.NO_BORDER)
        self.panel2.SetBackgroundColour(self.colorBG)


        self.panel4 = wx.Panel(self, size=(200, 60), pos=(121, 202), style=wx.NO_BORDER)
        self.panel4.SetBackgroundColour(self.colorLineNumberBorder)


        self.entryVar = wx.TextCtrl(self.panel4, style = wx.TE_RICH | wx.BORDER_NONE ,pos=(85, 20), size=(95, 20))
        self.entryVar.SetBackgroundColour(self.colorBG)
        self.entryVar.SetForegroundColour(self.colorWhite)

        self.btnAcept = wx.Button(self.panel3,-1,"Done", pos = (17,10), size = (80,40), style = wx.NO_BORDER)
        self.btnAcept.SetBackgroundColour(self.colorBG)
        self.btnAcept.SetForegroundColour(self.colorLime)
        self.btnAcept.Bind(wx.EVT_BUTTON,self.acept)
        self.btnAcept.Bind(wx.EVT_ENTER_WINDOW,self.buttonAceptLightOn)
        self.btnAcept.Bind(wx.EVT_LEAVE_WINDOW, self.buttonAcepLightOff)


        self.lblentryVar = wx.StaticText(self.panel4, -1, "VarName:", (30, 20))
        self.lblentryVar.SetForegroundColour(self.colorLabel)

        if height <= 7:

            gridSizer1 = wx.GridSizer(7,1,0,0)
        else:
            gridSizer1 = wx.GridSizer(height, 1, 0, 0)
        self.Show()
        self.Move(wx.Point(530, 255))


        for i in range(height):
            btn = wx.Button(self.panel1,label = "Matriz" + str(i),size = (103,29),style = wx.NO_BORDER)
            btn.SetForegroundColour(self.colorLabel)
            if i%2 == 0:
                btn.SetBackgroundColour(self.colorLineNumberBorder)

            else:
                btn.SetBackgroundColour(self.colorBorder)

            btn.Bind(wx.EVT_BUTTON,self.click)
            gridSizer1.Add(btn)
            matriz = []
            for i in range(row):
                lista = []
                for j in range(col):
                    lista.append(False)
                matriz.append(lista)
            self.matrices.append(matriz)
        if height <= 7:

            for i in range(height,7):
                p = wx.Panel(self.panel1, size = (103,29), style=wx.NO_BORDER)
                if i % 2 == 0:
                    p.SetBackgroundColour(self.colorLineNumberBorder)
                else:
                    p.SetBackgroundColour(self.colorBorder)
                gridSizer1.Add(p)

        posy = 0
        for i in range(8):
            posx = 0
            lista = []
            for j in range(8):
                btn = wx.Button(self.panel2, label="", size=(23, 23), style=wx.NO_BORDER, pos=(posx, posy))
                btn.mypos = (i,j)
                btn.Bind(wx.EVT_BUTTON, self.clickOnbutton)
                lista.append(btn)
                posx += 25
                btn.Disable()
            self.btnMatrix.append(lista)
            posy += 25

        for i in range(row):
            for j in range(col):
                self.btnMatrix[i][j].Enable()


        self.currentMatrix = "Matriz0"
        self.matrixUpdater(0)

        self.panel1.SetSizer(gridSizer1)

    def buttonAceptLightOn(self,event):
        self.btnAcept.SetBackgroundColour(self.colorLabel)
        self.btnAcept.SetForegroundColour(self.colorBG)
    def buttonAcepLightOff(self,event):
        self.btnAcept.SetBackgroundColour(self.colorBG)
        self.btnAcept.SetForegroundColour(self.colorLime)

    def closeWindow(self,event):
        self.mainWindow.Enable()
        self.Destroy()

    def click(self, event):

        ind = int(event.GetEventObject().GetLabel().replace("Matriz",""))
        self.currentMatrix = event.GetEventObject().GetLabel()
        self.matrixUpdater(ind)

    def acept(self,event):
        abc = "abcdefghijklmnopqrstuvwxyzñ"

        if self.entryVar.GetValue() == "":
            wx.MessageBox("The variable name cannot be empty", 'Warning', wx.OK | wx.ICON_WARNING)
        elif self.entryVar.GetValue()[0].isdigit():
            wx.MessageBox("The variable name cannot start with a number", 'Warning', wx.OK | wx.ICON_WARNING)
        elif self.entryVar.GetValue()[0] in abc.upper() :
            wx.MessageBox("Variable name cannot be capitalized", 'Warning', wx.OK | wx.ICON_WARNING)
        else:
            # TODO logica para escribir variable en el textmain
            self.mainWindow.Enable()
            self.mainWindow.textMain.WriteText("\n"+self.entryVar.GetValue() + " = " + self.splitCube(self.matrices) + "\n")

            #self.mainWindow.changeTextColor()
            self.Destroy()
            print("acepted")
    def splitCube(self,cube):
        text = "["+str(cube[0])+",\n"
        for i in range(1,len(cube)-1):
            text += "\t"+str(cube[i])+",\n"
        text += "\t"+str(cube[-1])+"];"
        return text

    def clickOnbutton(self,event):

        pos = event.GetEventObject().mypos

        l = pos[0]
        c = pos[1]

        self.matrices[int(self.currentMatrix.replace("Matriz",""))][l][c] = not self.matrices[int(self.currentMatrix.replace("Matriz",""))][l][c]

        self.matrixUpdater(int(self.currentMatrix.replace("Matriz","")))

    def matrixUpdater(self,ind):
        matriz = self.matrices[ind]
        l = 0

        for line in matriz:
            c = 0
            for col in line:
                if col:
                    self.btnMatrix[l][c].SetBackgroundColour(self.colorTrue)
                else:

                    self.btnMatrix[l][c].SetBackgroundColour(self.colorFalse)

                c += 1
            l += 1

