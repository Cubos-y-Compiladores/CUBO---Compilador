import wx


class MyApp(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent = parent, title = title, size = (1350,750))
        self.mainPanel = wx.Panel(self,1, pos = (37,21), size = (1278,424))
        self.mainPanel.SetBackgroundColour(self.colorBG)
        self.textMain = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_RICH | wx.BORDER_NONE, pos=(0,0),size=(1277, 420))
        self.colorBG = (20, 18, 18)
        self.textMain.SetBackgroundColour(self.colorBG)
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyApp(None,"CubeCompiler")
    app.MainLoop()