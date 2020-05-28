import wx
import wx.lib.scrolledpanel
import os

class matrizFrame(wx.Frame):
    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, parent=parent, title=title, size=(337, 300))


        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap(os.getcwd() + "/Resources/icon.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)

        screenSize = wx.DisplaySize()
        screenWidth = screenSize[0]
        screenHeight = screenSize[1]
        self.colorTrue = (2,195,154)
        self.colorFalse = (231,29,54)
        self.colorBG = (20,18,18)
        self.colorLabel = (93,253,203)
        self.colorBorder = (40,40,40)
        self.colorLineNumberBorder = (32, 32, 32)
        self.SetMaxSize((337,300))
        self.SetMinSize((337,300))
        self.SetBackgroundColour("black")
        self.matrices = []
        self.currentMatrix = None
        self.btnMatrix = []

        panel3 = wx.Panel(self, size=(120, 60), pos=(0, 201), style=wx.NO_BORDER)
        panel3.SetBackgroundColour(self.colorBorder)
        # self.bmpRun = wx.Bitmap(os.getcwd() + "/Resources/icon.png", wx.BITMAP_TYPE_ANY)
        # self.stcbmp = wx.StaticBitmap(parent = panel3 , bitmap = self.bmpRun, pos = (0,0), size = (60,30))


        panel1 = wx.lib.scrolledpanel.ScrolledPanel(self, -1, size=(120, 200), pos=(0, 0),style=wx.NO_BORDER)
        panel1.SetupScrolling(scroll_y=True)
        panel1.SetBackgroundColour(self.colorBorder)

        panel2 = wx.Panel(self, size=(200, 200), pos=(122, 2), style=wx.NO_BORDER)
        panel2.SetBackgroundColour(self.colorBG)


        panel4 = wx.Panel(self, size=(200, 60), pos=(121, 202), style=wx.NO_BORDER)
        panel4.SetBackgroundColour(self.colorLineNumberBorder)



        gridSizer1 = wx.GridSizer(8,1,0,0)

       # for i in self.cube.getMatrices():
        #    gridSizer1.Add(i[1])




        for i in range(8):
            btn = wx.Button(panel1,label = "Matriz" + str(i),size = (103,29),style = wx.NO_BORDER)
            btn.SetForegroundColour(self.colorLabel)
            if i%2 == 0:
                btn.SetBackgroundColour(self.colorLineNumberBorder)

            else:
                btn.SetBackgroundColour(self.colorBorder)

            btn.Bind(wx.EVT_BUTTON,self.click)
            gridSizer1.Add(btn)
            matriz = []
            for i in range(8):
                lista = []
                for j in range(8):
                    lista.append(False)
                matriz.append(lista)
            self.matrices.append(matriz)

        posy = 0
        for i in range(8):
            posx = 0
            lista = []
            for j in range(8):
                btn = wx.Button(panel2, label="", size=(23, 23), style=wx.NO_BORDER, pos=(posx, posy))
                btn.mypos = (i,j)
                btn.Bind(wx.EVT_BUTTON, self.clickOnbutton)
                lista.append(btn)
                posx += 25
            self.btnMatrix.append(lista)
            posy += 25

        self.currentMatrix = "Matriz0"
        self.matrixUpdater(0)

        panel1.SetSizer(gridSizer1)


    def click(self, event):
        print(event.GetEventObject().GetLabel())
        ind = int(event.GetEventObject().GetLabel().replace("Matriz",""))
        self.currentMatrix = event.GetEventObject().GetLabel()
        self.matrixUpdater(ind)


    def clickOnbutton(self,event):
        print(event.GetEventObject().GetLabel())
        pos = event.GetEventObject().mypos
        print(pos)
        l = pos[0]
        c = pos[1]

        self.matrices[int(self.currentMatrix.replace("Matriz",""))][l][c] = not self.matrices[int(self.currentMatrix.replace("Matriz",""))][l][c]
        print(self.matrices[l])
        self.matrixUpdater(int(self.currentMatrix.replace("Matriz","")))

    def matrixUpdater(self,ind):
        matriz = self.matrices[ind]
        l = 0
        print(matriz)
        for line in matriz:
            c = 0
            for col in line:
                if col:
                    self.btnMatrix[l][c].SetBackgroundColour(self.colorTrue)
                else:
                    self.btnMatrix[l][c].SetBackgroundColour(self.colorFalse)

                c += 1
            l += 1















if __name__=='__main__':
    app = wx.App()
    frame = matrizFrame(title="QuickCube")
    frame.Show()
    app.MainLoop()