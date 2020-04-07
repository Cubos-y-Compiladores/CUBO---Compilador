import wx


class Example(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None)

        btn = wx.Button(self, label="press me")
        self.Sizer = wx.BoxSizer()
        self.Sizer.Add(btn)

        self.ctrl_down = False

        self.Bind(wx.EVT_KEY_UP, self.OnUpdateCtrlState)
        self.Bind(wx.EVT_KEY_DOWN, self.OnUpdateCtrlState)
        btn.Bind(wx.EVT_KEY_UP, self.OnUpdateCtrlState)
        btn.Bind(wx.EVT_KEY_DOWN, self.OnUpdateCtrlState)
        btn.Bind(wx.EVT_BUTTON, self.OnButton)

    def OnUpdateCtrlState(self, event):
        self.ctrl_down = event.ControlDown()
        self.v_down = event.GetEventObject().GetRefData()
        print( self.v_down)
       #print(self.ctrl_down)
        event.Skip()

    def OnButton(self, event):
        if self.ctrl_down:
            wx.MessageBox("control down")


app = wx.App(False)
app.TopWindow = f = Example()
f.Show()
app.MainLoop()