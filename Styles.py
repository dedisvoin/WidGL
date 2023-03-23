from colorama import Fore

Fonts = {
    1:'Arial',
    2:'Calibri',
    3:'Cambria',
    4:'Candara',
    5:'Comic Sans',
    6:'Consolas',
    7:'Constantia',
    8:'Corbel',
    9:'Courier New',
    10:'Georgia',
    11:'Palatino',
    12:'Segoe UI',
    13:'Trebuchet MS',
    14:'Verdana'
}
    
    

class Style():
    def __init__(self,objname) -> None:
        self.obj = objname
        self.genname = ''
        self.name = ''
        self.stylebuf = {
            'text':'None',
            'text.color':[50,50,50],
            'text.font.size':20,
            'text.surf.size':[100,30],
            'text.font':'Arial',
            'text.antialising':True,
            'text.bold':True,
            'text.italic':False,
            
            'text.outline':False,
            'text.outline.color':[100,100,100],
            'text.outline.size':5,
            'text.outline.dx':0,
            'text.outline.dy':0,
            
            'text.centering':False,
            'text.rotate.angle':0,
            'text.dx':0,
            'text.dy':0,
            
            'position':[0,0],
            
            'text.scale.x':1,
            'text.scale.y':1,
            'text.scale':None,
            
            'text.on.window':None,
            
            'mouse-oning':False,
            'mouse-oning-color':(200,200,200),
            'mouse-oning-outline-dx':0,
            'mouse-oning-outline-dy':0,
            'mouse-oning-outline-size':-1,
            'mouse-oning-outline-color':(100,100,100),
            
            
            
            'bt.width':100,
            'bt.height':40,
            
            'bt.color':(100,100,100),
            'bt.releasd.color':(80,80,80),
            'bt.pressed.color':(60,60,60),
            
            'bt.global.outline.size':-1,
            'bt.pressed.outline.size':-1,
            'bt.releasd.outline.size':-1,
            
            'bt.outline.size':-1,
            'bt.outline.color':(0,0,0),
            'bt.outline.pressed.color':(0,0,0),
            'bt.outline.releasd.color':(0,0,0),
            
            'bt.place.width.delta':0,
            'bt.place.height.delta':0,
            
            
            
            'bt.global.rougres':-1,
            'bt.rougres':0,
            'bt.pressed.rougres':0,
            'bt.releasd.rougres':0,
            
            'bt.on.window':None,
            
            'togle.dot.type':'togle.circle',
            'togle.dot.size':20,
            'togle.width':100,
            'togle.height':40,
            'togle.dot.true.color':(100,100,100),
            'togle.dot.false.color':(200,150,150),
            
            'togle.line.true.color':(70,70,70),
            'togle.line.false.color':(100,40,40),
            'togle.start.value':True,
            'togle.dot.speed':10,
            'togle.line.rougres':10,
            
            'togle.dot.outline.size':-1,
            'togle.dot.outline.color':(0,0,0),
            'togle.line.outline.size':-1,
            'togle.line.outline.color':(0,0,0),
            
            'togle.place.width.delta':0,
            'togle.place.height.delta':0,
            
            
            
            
            'place.color':(100,100,100),
            'place.width':100,
            'place.height':100,
            'place.rougres':0,
            'place.outline.size':-1,
            'place.outline.color':(0,0,0),
            
            'place.on.window':None,
            'place.on.window.dx':0,
            'place.on.window.dy':0,
            
            'place.on.place':None,
            'place.on.place.dx':0,
            'place.on.place.dy':0,
            
            'place.parent.place.dw':0,
            'place.parent.place.dh':0,
            
            'togle.dot.animate':None,
            'togle.line.animate':None,
            'togle.dot.left.dx':20,
            'togle.dot.right.dx':20,
            'animate.delta':1
            
            
            
            
            
            
        }
        self.style = {
            'text':'None',
            'text.color':[50,50,50],
            'text.font.size':20,
            'text.surf.size':[100,30],
            'text.font':'Arial',
            'text.antialising':True,
            'text.bold':True,
            'text.italic':False,
            
            'text.outline':False,
            'text.outline.color':[100,100,100],
            'text.outline.size':5,
            'text.outline.dx':0,
            'text.outline.dy':0,
            
            'text.centering':False,
            'text.rotate.angle':0,
            'text.dx':0,
            'text.dy':0,
            
            'position':[0,0],
            
            'text.scale.x':1,
            'text.scale.y':1,
            'text.scale':None,
            
            'text.on.window':None,
            'text.on.window.dx':0,
            'text.on.window.dy':0,
            
            'text.on.place':None,
            'text.on.place.dx':0,
            'text.on.place.dy':0,
            
            'mouse-oning':False,
            'mouse-oning-color':(200,200,200),
            'mouse-oning-outline-dx':0,
            'mouse-oning-outline-dy':0,
            'mouse-oning-outline-size':-1,
            'mouse-oning-outline-color':(100,100,100),
            
            
            
            'bt.width':100,
            'bt.height':40,
            
            'bt.color':(100,100,100),
            'bt.release.color':(80,80,80),
            'bt.press.color':(60,60,60),
            
            'bt.global.outline.size':-1,
            'bt.pressed.outline.size':-1,
            'bt.releasd.outline.size':-1,
            
            'bt.outline.size':-1,
            'bt.outline.color':(0,0,0),
            'bt.outline.pressed.color':(0,0,0),
            'bt.outline.releasd.color':(0,0,0),
            
            'bt.place.width.delta':0,
            'bt.place.height.delta':0,
            
            
            

            'bt.rougres':'defold',

            
            'bt.on.window':None,
            
            'togle.dot.type':'togle.circle',
            'togle.dot.size':20,
            'togle.width':100,
            'togle.height':40,
            'togle.dot.true.color':(100,100,100),
            'togle.dot.false.color':(200,150,150),
            
            'togle.line.true.color':(70,70,70),
            'togle.line.false.color':(100,40,40),
            'togle.start.value':True,
            'togle.dot.speed':10,
            'togle.line.rougres':10,
            
            'togle.dot.outline.size':-1,
            'togle.dot.outline.color':(0,0,0),
            'togle.line.outline.size':-1,
            'togle.line.outline.color':(0,0,0),
            
            'togle.place.width.delta':0,
            'togle.place.height.delta':0,
            
            
            
            
            'place.color':(100,100,100),
            'place.width':100,
            'place.height':100,
            'place.rougres':0,
            'place.outline.size':-1,
            'place.outline.color':(0,0,0),
            'place.on.window':None,
            'place.on.window.dx':0,
            'place.on.window.dy':0,
            'place.parent.place.dw':0,
            'place.parent.place.dh':0,
            
            'place.on.place':None,
            'place.on.place.dx':0,
            'place.on.place.dy':0,
            
            
            'togle.dot.animate':None,
            'togle.line.animate':None,
            'togle.dot.left.dx':20,
            'togle.dot.right.dx':20,
            'animate.delta':1
            
            
            
            
            
            
        }
        
    def SetValue(self,StyleName,Value):    
        try:
            self.style[StyleName] = Value
        except:...
        
    def Show(self):
        print(self.obj)
        for sti in self.style:
            if type(self.style[sti])==str:
                print(Fore.YELLOW+f'{sti:<40}'+Fore.GREEN+f'{str(self.style[sti]):>0}'+Fore.RESET)
            elif type(self.style[sti])==list:
                print(Fore.YELLOW+f'{sti:<40}'+Fore.CYAN+f'{str(self.style[sti]):>0}'+Fore.RESET)
            else:
                print(Fore.YELLOW+f'{sti:<40}'+Fore.BLUE+f'{str(self.style[sti]):>0}'+Fore.RESET)


                
    
                
            
            



        
    
            
    
                
                
                
 
            
                
            
        
        


            
    