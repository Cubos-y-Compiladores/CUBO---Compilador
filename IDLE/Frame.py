import wx
import wx.lib.scrolledpanel
import os
import wx.stc
import IDLE.QuickCube as QuickCube

class Frame(wx.Frame):
    def __init__(self, title,mainWindow,mainDirectory,parent=None):
        wx.Frame.__init__(self, parent=parent, title=title, size=(270, 230))

        self.mainWindow = mainWindow
        self.mainDirectory = mainDirectory
        self.Bind(wx.EVT_CLOSE, self.closeWindow)
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap(self.mainDirectory + "/Resources/icon.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        self.colorBG = (20, 18, 18)
        self.colorWhite = (255, 255, 255)
        self.colorBorder = (40, 40, 40)
        self.colorLabel = (93, 253, 203)
        self.colorLightOn = (52,58,64)

        self.SetBackgroundColour(self.colorBorder)

        self.SetMinSize((270, 230))
        self.SetMaxSize((270, 230))
        self.entryCol = wx.TextCtrl(self, style = wx.TE_RICH | wx.BORDER_NONE ,pos=(90, 45), size=(75, 20))
        self.entryCol.SetBackgroundColour(self.colorBG)
        self.entryCol.SetForegroundColour(self.colorWhite)
        self.entryRow = wx.TextCtrl(self, style = wx.TE_RICH | wx.BORDER_NONE ,pos=(90, 80), size=(75, 20))
        self.entryRow.SetBackgroundColour(self.colorBG)
        self.entryRow.SetForegroundColour(self.colorWhite)
        self.entryHeight = wx.TextCtrl(self, style = wx.TE_RICH | wx.BORDER_NONE ,pos=(90, 115), size=(75, 20))
        self.entryHeight.SetBackgroundColour(self.colorBG)
        self.entryHeight.SetForegroundColour(self.colorWhite)

        self.lbl = wx.StaticText(self, -1, "Please insert the cube's configuration values", (10, 9))

        self.lblentryCol = wx.StaticText(self, -1, "Col:", (45, 45))
        self.lblentryRow = wx.StaticText(self, -1, "Row:", (45, 80))
        self.lblentryHeight = wx.StaticText(self, -1, "Height:", (45, 115))

        self.lbl.SetForegroundColour(self.colorLabel)
        self.lblentryCol.SetForegroundColour(self.colorLabel)
        self.lblentryRow.SetForegroundColour(self.colorLabel)
        self.lblentryHeight.SetForegroundColour(self.colorLabel)

        self.bmpCube = wx.Bitmap(mainDirectory + "/Resources/cube1.png", wx.BITMAP_TYPE_ANY)
        self.buttonCube = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=self.bmpCube,
                                 size=(self.bmpCube.GetWidth() + 8, self.bmpCube.GetHeight() + 8), style = wx.NO_BORDER, pos = (115,155))
        self.buttonCube.SetBackgroundColour(self.colorBorder)


        self.buttonCube.Bind(wx.EVT_ENTER_WINDOW,self.buttonCubeLightOn)
        self.buttonCube.Bind(wx.EVT_LEAVE_WINDOW, self.buttonCubeLightOff)
        self.buttonCube.Bind(wx.EVT_BUTTON, self.click)

        # Bordes del boton

        self.panelIV = wx.Panel(self,1,pos = (114,155) ,size = (1,25))
        self.panelIV.SetBackgroundColour(self.colorBG)

        self.panelDV = wx.Panel(self,1,pos = (139,155) ,size = (1,25))
        self.panelDV.SetBackgroundColour(self.colorBG)

        self.panelAH = wx.Panel(self,1,pos = (114,154) ,size = (26,1))
        self.panelAH.SetBackgroundColour(self.colorBG)

        self.panelBH = wx.Panel(self,1,pos = (114,179) ,size = (25,1))
        self.panelBH.SetBackgroundColour(self.colorBG)


        self.Show()
        self.Move(wx.Point(550,275))

    def closeWindow(self,event):
        self.mainWindow.Enable()
        self.Destroy()

    def buttonCubeLightOn(self,event):
        self.buttonCube.SetBackgroundColour(self.colorLightOn)
    def buttonCubeLightOff(self,event):
        self.buttonCube.SetBackgroundColour(self.colorBorder)
    def isWord(self,input):
        abc = "abcdefghijklmnopqrstuvwxyzñ"
        for i in input:
            if i in abc:
                return True
        return False
    def click(self,event):

        # Validaciones

        if self.entryCol.GetValue().isdigit() and self.entryRow.GetValue().isdigit() and self.entryHeight.GetValue().isdigit():
            if int(self.entryCol.GetValue()) > 8 or int(self.entryRow.GetValue()) > 8:
                wx.MessageBox("Col and Row can't be greater than 8", 'Warning', wx.OK | wx.ICON_WARNING)
            else:
                quickCube = QuickCube.matrizFrame("Quick Cube",int(self.entryCol.GetValue()),int(self.entryRow.GetValue()),
                                                  int(self.entryHeight.GetValue()),self.mainWindow,self.mainDirectory)

                self.Destroy()
        elif self.entryCol.GetValue() == "" or self.entryRow.GetValue() == "" or self.entryHeight.GetValue() == "":
            wx.MessageBox("No configuration value can be empty", 'Warning', wx.OK | wx.ICON_WARNING)
        elif self.isWord(self.entryCol.GetValue()) or  self.isWord(self.entryRow.GetValue()) or  self.isWord(self.entryHeight.GetValue()):
            wx.MessageBox("Configuration values can only be integeres", 'Warning', wx.OK | wx.ICON_WARNING)



