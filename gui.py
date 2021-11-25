import wx


class MyFrame(wx.Frame):
    def __init__(self, superior):
        wx.Frame.__init__(self, parent=superior, title="example")
        self.panel1 = wx.Panel(self)
        self.panel1.Bind(wx.EVT_LEFT_UP, self.onclick)

    def onclick(self, event):
        pos = event.GetPosition()
        wx.StaticText(parent=self.panel1, label='hi', pos=(pos.x, pos.y))


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None)
    frame.Show(True)
    app.MainLoop()
