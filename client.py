import pygooey
import pygame as pg
import socket

host = ''
port = 5000



white = (255,255,255)
black = (0,0,0)


def textbox_callback(id, final):
    Pan3.addText(final)
    print('enter pressed, textbox contains {}'.format(final))
    
def alternative_callback(id, final):
    
    print('alternative textbox contains {}'.format(final))
    
def button_callback():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(entry.final)
    data = s.recv(1024)
    s.close()
    Pan3.addText(data)
    print('button pressed, textbox contains {}'.format(entry.final))


class Pane(object):
    def __init__(self):
        pg.init()
        self.font = pg.font.SysFont('Arial', 25)
        pg.display.set_caption('Box Test')
        self.screen = pg.display.set_mode((600,400), 0, 32)
        self.screen.fill((white))
        pg.display.update()


    def addText(self,text="default"):
        self.screen.fill((white))
        self.screen.blit(self.font.render(text, True, (255,0,0)), (300, 100))
        pg.display.update()


pg.init()
screen = pg.display.set_mode((600,400))
screen_rect = screen.get_rect()
done = False
widgets = []


#see all settings help(pygooey.TextBox.__init__)
entry_settings = {
    "inactive_on_enter" : False,
    'active':False
}
entry = pygooey.TextBox(rect=(70,100,150,30), command=textbox_callback, **entry_settings)
widgets.append(entry)

#see all settings help(pygooey.Button.__init__)
btn_settings = {
    "clicked_font_color" : (0,0,0),
    "hover_font_color"   : (205,195, 100),
    'font'               : pg.font.Font(None,16),
    'font_color'         : (255,255,255),
    'border_color'       : (0,0,0),
}
btn = pygooey.Button(rect=(10,10,105,25), command=button_callback, text='OK', **btn_settings)
widgets.append(btn)
Pan3 = Pane()
Pan3.addText()



while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        for w in widgets:
            w.get_event(event)
    for w in widgets:
        w.update()
        w.draw(screen)
    pg.display.update()


