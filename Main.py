from pygl_nf import GL #нужна самая новая версия!!!!

from Styles_loader import LoadFile
from wrapper import Wrapper_v2
#python 3.10.4



win = GL.Display_init_(flags=GL.D_Resize,size=[700,400])
 


style = LoadFile('имяфайла стилей.txt',win)



w = Wrapper_v2(style,win)

timer = 1

while win.CEUF(FPS=1000):
    timer+=1
    if timer%200==0:
        try:
            style = LoadFile('style.txt',win)
            w = Wrapper_v2(style,win)
        except:...
    
    
    w.Render()
