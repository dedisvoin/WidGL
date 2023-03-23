from pygl_nf import GL
from Widgets import TextW,ButtonW,PlaceW,TogleW
from Widgets_v2 import WPlace,WText,WButton
 
 
 
 
class Wrapper:
    def __init__(self,styles:list,win) -> None:
        self.objects = []
        self.styles = styles
        self.win = win
        
        self.wrap()
        
    def wrap(self):
        for style in self.styles:

            if style.genname[0] == '$':
                try:
                    closescobindx = style.genname.index(')')
                except:...
                if ':' in style.genname:
                    widgetname = style.genname[closescobindx+2:style.genname.index(':')]
                else:
                    widgetname = style.genname[closescobindx+2:]
                
                
                widgettype = style.genname[1:closescobindx+1]
                
                
                if widgettype == 'place()':
                    place = PlaceW(widgetname,self.styles,self.win)
                    self.objects.append(place)
                if widgettype == 'bt()':
                    button = ButtonW(widgetname,0,self.styles,self.win)
                    self.objects.append(button)
                if widgettype == 'togle()':
                    togle = TogleW(widgetname,self.styles)
                    self.objects.append(togle)
                if widgettype == 'text()':
                    text = TextW(widgetname,self.styles)
                    self.objects.append(text)
                    
    
    def Render(self):
        for obj in self.objects:
            try:
                obj.Render()
            except:
                obj.Render(self.win)
                
class Wrapper_v2:
    def __init__(self,styles:list,win) -> None:
        self.objects = []
        self.styles = styles
        self.win = win
        
        self.wrap()
        
    def wrap(self):
        for style in self.styles:

            if style.genname[0] == '$':
                try:
                    closescobindx = style.genname.index(')')
                except:...
                if ':' in style.genname:
                    widgetname = style.genname[closescobindx+2:style.genname.index(':')]
                else:
                    widgetname = style.genname[closescobindx+2:]
                
                
                widgettype = style.genname[1:closescobindx+1]
                
                
                if widgettype == 'place()':
                    place = WPlace(widgetname,self.styles,self.win)
                    self.objects.append(place)
                if widgettype == 'text()':
                    text = WText(widgetname,self.styles,self.win)
                    self.objects.append(text)
                if widgettype == 'button()':
                    button = WButton(widgetname,self.styles,self.win)
                    self.objects.append(button)
                
                    
    
    def Render(self):
        for obj in self.objects:
                obj.Render()
                   
            
 
 
