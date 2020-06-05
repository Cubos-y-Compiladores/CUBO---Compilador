# -*- coding: utf-8 -*-
import wx
import time
class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
#        kwds["pos"] = (10,10)
        self.frame = wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle("Move around the screen")
        self.InitUI()

    def InitUI(self):
        self.location1 = wx.Point(10,10)
        self.location2 = wx.Point(500,500)
        self.panel1 = wx.Panel(self)
        self.button1 = wx.Button(self.panel1, -1, label="Move", size=(80,25), pos=(10,10))
        self.button1.Bind(wx.EVT_BUTTON, self.OnItem1Selected)
        self.Show()
        self.Move(self.location1)

    def OnItem1Selected(self, event):
        self.MoveAround()

    def MoveAround(self):
        #Judder effect by moving the window
        for i in range(30):
            curr_location = self.GetPosition() #or self.GetPositionTuple()
            if curr_location == self.location1:
                print ("moving to ", self.location2)
                self.Move(self.location2) #Any of these 3 commands will work
    #            self.MoveXY(500,500)
    #            self.SetPosition(wx.Point(500,500), wx.SIZE_USE_EXISTING)
            else:
                print ("moving to ", self.location1)
                self.Move(self.location1) #Any of these 3 commands will work
    #            self.MoveXY(10,10)
    #            self.SetPosition(wx.Point(10,10), wx.SIZE_USE_EXISTING)
            self.Update()
            time.sleep(0.1)

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame(None)
    app.MainLoop()