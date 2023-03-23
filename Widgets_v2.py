from copy import copy
import math
import random

from Styles import Fonts
from Styles_loader import LoadFile
import pygame
from pygl_nf import GL

class WPlace():
    def __init__(self,Wname,style,win: GL.Display_init_) -> None:
        self.Wname = Wname
        self.win = win
        self.allStyles = style
        
        self.Placed = False
        self.ParentPlaceStyle = None
        
        self.StylesInit()
        self.ParentStylesInit()
        
    def StylesInit(self):
        for styl in self.allStyles:
            try:
                
                ind = styl.obj.index(':')
                
                if styl.obj[:ind] == 'place() '+ self.Wname:
                    self.selfstyle = styl
                    self.Placed = True
                    self.place_name = styl.obj[ind+1:]
            except:
                if styl.obj == 'place() '+ self.Wname:
                    self.selfstyle = styl
                                    
    def ParentStylesInit(self):
        if self.Placed:
            for styl in self.allStyles:
                if styl.obj.find('place() '+self.place_name)!=-1:
                    self.ParentPlaceStyle = styl
                               
    def SelfStylesUpdate(self):
        self.P1_position = self.selfstyle.style['position']
        self.P1_width = self.selfstyle.style['place.width']
        self.P1_height = self.selfstyle.style['place.height']
        self.P1_color = self.selfstyle.style['place.color']
        self.P1_rougres = int(self.selfstyle.style['place.rougres'])
        self.P1_outline_size = int(self.selfstyle.style['place.outline.size'])
        self.P1_outline_color = self.selfstyle.style['place.outline.color']
        
        self.P1_on_window = self.selfstyle.style['place.on.window']
        self.P1_on_window_dx = self.selfstyle.style['place.on.window.dx']
        self.P1_on_window_dy = self.selfstyle.style['place.on.window.dy']
        
        self.P1_on_place = self.selfstyle.style['place.on.place']
        self.P1_on_place_dx = self.selfstyle.style['place.on.place.dx']
        self.P1_on_place_dy = self.selfstyle.style['place.on.place.dy']
        
        self.P1_parent_place_dw = self.selfstyle.style['place.parent.place.dw']
        self.P1_parent_place_dh = self.selfstyle.style['place.parent.place.dh']
        
        self.P1_mouse_oning = self.selfstyle.style['mouse-oning']
        self.P1_mouse_oning_color = self.selfstyle.style['mouse-oning-color']
        self.P1_mouse_oning_outline_size = int(self.selfstyle.style['mouse-oning-outline-size'])
        self.P1_mouse_oning_outline_color = self.selfstyle.style['mouse-oning-outline-color']
        
    def ParentStylesUpdate(self):
        
        if self.ParentPlaceStyle!=None:
            self.Parent_position = self.ParentPlaceStyle.stylebuf['position']
            self.Parent_width = self.ParentPlaceStyle.stylebuf['place.width']
            self.Parent_height = self.ParentPlaceStyle.stylebuf['place.height']
                
    def SelfStylesManipulate(self):
       
        self.P2_position = [None,None]
        self.P2_width = 0
        self.P2_height = 0
        
        
        if self.Placed:
            if type(self.P1_width)==str:
                if 'parent.width' in self.P1_width:
                    self.P2_width = self.Parent_width+self.P1_parent_place_dw
            else:
                self.P2_width = self.P1_width
            if type(self.P1_height)==str:
                if 'parent.height' in self.P1_height:
                    self.P2_height = self.Parent_height+self.P1_parent_place_dh
            else:
                self.P2_height = self.P1_height
        else:
            self.P2_height = self.P1_height
            self.P2_width = self.P1_width
            
            
        if self.Placed: 
            self.P2_position[0]=self.P1_position[0] + self.Parent_position[0]
            self.P2_position[1]=self.P1_position[1] + self.Parent_position[1]
        else:
            self.P2_position = self.P1_position
        
        if self.P1_on_window!=None:
            if 'center' in self.P1_on_window:
                self.P2_position[0] = self.win.GET_WIN_WIDTH()/2-self.P2_width/2+self.P1_on_window_dx
                self.P2_position[1] = self.win.GET_WIN_HEIGHT()/2-self.P2_height/2+self.P1_on_window_dy
                
            if 'left' in self.P1_on_window:
                self.P2_position[0] = 0+self.P1_on_window_dx
            if 'right' in self.P1_on_window:
                self.P2_position[0] = self.win.GET_WIN_WIDTH()-self.P2_width+self.P1_on_window_dx
            if 'top' in self.P1_on_window:
                self.P2_position[1] = 0+self.P1_on_window_dy
            if 'down' in self.P1_on_window:
                self.P2_position[1] = self.win.GET_WIN_HEIGHT()-self.P2_height+self.P1_on_window_dy
            
        if self.P1_on_place!=None:
            
            if 'center' in self.P1_on_place:
                self.P2_position[0] = self.Parent_width/2-self.P2_width/2+self.Parent_position[0]+self.P1_on_place_dx
                self.P2_position[1] = self.Parent_height/2-self.P2_height/2+self.Parent_position[1]+self.P1_on_place_dy
            if 'left' in self.P1_on_place:
                self.P2_position[0] = 0+self.Parent_position[0]+self.P1_on_place_dx
            if 'right' in self.P1_on_place:
                self.P2_position[0] = self.Parent_width-self.P2_width+self.Parent_position[0]+self.P1_on_place_dx
            if 'top' in self.P1_on_place:
                self.P2_position[1] = 0+self.Parent_position[1]+self.P1_on_place_dy
            if 'down' in self.P1_on_place:
                self.P2_position[1] = self.Parent_height-self.P2_height+self.Parent_position[1]+self.P1_on_place_dy
            
        self.selfstyle.stylebuf['position']=self.P2_position
        self.selfstyle.stylebuf['place.width']=self.P2_width
        self.selfstyle.stylebuf['place.height']=self.P2_height
        
    def Update(self):
        if self.P1_mouse_oning:
            rect = pygame.Rect(self.P2_position,[self.P2_width,self.P2_height])
            if rect.collidepoint(*GL.om.pos):
                self.P2_color = self.P1_mouse_oning_color
                self.P2_outline_size = self.P1_mouse_oning_outline_size
                self.P2_outline_color = self.P1_mouse_oning_outline_color
            else:
                self.P2_color = self.P1_color
                self.P2_outline_size = self.P1_outline_size
                self.P2_outline_color = self.P1_outline_color
        else:
            self.P2_color = self.P1_color
            self.P2_outline_size = self.P1_outline_size
            self.P2_outline_color = self.P1_outline_color
              
    def Render(self):
        self.SelfStylesUpdate()
        self.ParentStylesUpdate()
        self.SelfStylesManipulate()
        self.Update()
        
        self.win.GL.Rect(self.P2_color,self.P2_position,[self.P2_width,self.P2_height],'s',0,'OF',self.P1_rougres,THICKNESS_2=self.P2_outline_size,THICKNESS_2_COLOR=self.P2_outline_color)
    
class WButton():
    def __init__(self,Wname,style,win: GL.Display_init_) -> None:
        self.Wname = Wname
        self.win = win 
        self.allStyles = style
        
        self.Placed = False
        self.ParentPlaceStyle = None 
        
        
        
        self.StylesInit()
        self.ParentStylesInit()
        self.SelfStylesUpdate()
        
    def ParentStylesInit(self):
        if self.Placed:
            for styl in self.allStyles:
                if styl.obj.find('button() '+self.place_name)!=-1:
                    self.ParentPlaceStyle = styl
        
    def StylesInit(self):
        for styl in self.allStyles:
            try:
                
                ind = styl.obj.index(':')
                
                if styl.obj[:ind] == 'button() '+ self.Wname:
                    self.selfstyle = styl
                    self.Placed = True
                    self.place_name = styl.obj[ind+1:]
            except:
                if styl.obj == 'button() '+ self.Wname:
                    self.selfstyle = styl
        
    def SelfStylesUpdate(self):
        self.B1_position = self.selfstyle.style['position']
        self.B1_width = self.selfstyle.style['bt.width']
        self.B1_height = self.selfstyle.style['bt.height']
        
        self.B1_rougresdata:str = self.selfstyle.style['bt.rougres']
        self.B1_rougresdata = self.B1_rougresdata.split(' ')
        self.B2_rougresdata:list[str] = []
        
        self.B1_rougres = 0
        self.B1_release_rougres = 0
        self.B1_press_rougres = 0
        
        for value in self.B1_rougresdata:
            if value!='':
                self.B2_rougresdata.append(value)
        
        for value in self.B2_rougresdata:
            chortind = value.index('-')
            name = value[:chortind]
            number = int(value[chortind+1:])
            
            if name == 'defold':
                self.B1_rougres = number
            if name == 'releas':
                self.B1_release_rougres = number
            if name == 'press':
                self.B1_press_rougres = number
            
            
            
            
        
        
        self.B1_color = self.selfstyle.style['bt.color']
        self.B1_release_color = self.selfstyle.style['bt.release.color']
        self.B1_press_color = self.selfstyle.style['bt.press.color']
        
    def Render(self):
        self.rect = pygame.Rect(self.B1_position,[self.B1_width,self.B1_height])
        
        if self.rect.collidepoint(*GL.om.pos):
            
         
            if GL.om.GET_PRESS_ON_PYGL_WINDOW():
                self.win.GL.Rect(self.B1_press_color,self.B1_position,[self.B1_width,self.B1_height],'s',0,'F',R=self.B1_press_rougres)
            else:
                self.win.GL.Rect(self.B1_release_color,self.B1_position,[self.B1_width,self.B1_height],'s',0,'F',R=self.B1_release_rougres)
        else:
            self.win.GL.Rect(self.B1_color,self.B1_position,[self.B1_width,self.B1_height],'s',0,'F',R=self.B1_rougres)
            
        
class WText():
    def __init__(self,Wname,style,win: GL.Display_init_) -> None:
        self.Wname = Wname
        self.win = win 
        self.allStyles = style
        
        self.Placed = False
        self.ParentPlaceStyle = None 
        
        self.StylesInit()
        self.ParentStylesInit()
        self.SelfStylesUpdate()
        self.ParentStylesUpdate()
        self.Update()
        self.SelfStylesmanipulate()
        
        
    def StylesInit(self):
        for styl in self.allStyles:
            try:
                
                ind = styl.obj.index(':')
                
                if styl.obj[:ind] == 'text() '+ self.Wname:
                    self.selfstyle = styl
                    self.Placed = True
                    self.place_name = styl.obj[ind+1:]
            except:
                if styl.obj == 'text() '+ self.Wname:
                    self.selfstyle = styl
    
    def ParentStylesInit(self):
        self.ParentButton = False
        self.ParentPlace = False
        if self.Placed:
            for styl in self.allStyles:
                if styl.obj.find('place() '+self.place_name)!=-1:
                    self.ParentPlaceStyle = styl
                    self.ParentPlace = True
                if styl.obj.find('button() '+self.place_name)!=-1:
                    self.ParentPlaceStyle = styl
                    self.ParentButton = True
        
        
    def SelfStylesUpdate(self):
        self.T1_position = self.selfstyle.style['position']
        self.T1_text = str(self.selfstyle.style['text'])
        self.T1_antialising = self.selfstyle.style['text.antialising']
        self.T1_bold = self.selfstyle.style['text.bold']
        self.T1_color = self.selfstyle.style['text.color']
        self.T1_italic = self.selfstyle.style['text.italic']
        self.T1_centering = self.selfstyle.style['text.centering']
        
        self.T1_font_size = int(self.selfstyle.style['text.font.size'])
        self.T1_font = self.selfstyle.style['text.font']
        self.T1_rotate_angle = self.selfstyle.style['text.rotate.angle']
        
        self.T1_on_window = self.selfstyle.style['text.on.window']
        self.T1_on_window_dx = self.selfstyle.style['text.on.window.dx']
        self.T1_on_window_dy = self.selfstyle.style['text.on.window.dy']
        
        self.T1_on_place = self.selfstyle.style['text.on.place']
        self.T1_on_place_dx = self.selfstyle.style['text.on.place.dx']
        self.T1_on_place_dy = self.selfstyle.style['text.on.place.dy']
        
        self.T1_outline = self.selfstyle.style['text.outline']
        self.T1_outline_size = int(self.selfstyle.style['text.outline.size'])
        self.T1_outline_color = self.selfstyle.style['text.outline.color']
        
        self.T1_scale = self.selfstyle.style['text.scale']
        self.T1_scale_x = self.selfstyle.style['text.scale.x']
        self.T1_scale_y = self.selfstyle.style['text.scale.y']
        
        self.T1_mouse_oning = self.selfstyle.style['mouse-oning']
        self.T1_mouse_oning_color = self.selfstyle.style['mouse-oning-color']
        self.T1_mouse_oning_outline_size = int(self.selfstyle.style['mouse-oning-outline-size'])
        self.T1_mouse_oning_outline_color = self.selfstyle.style['mouse-oning-outline-color']
        
        if self.T1_scale!=None:
            self.T1_scale_x = self.T1_scale
            self.T1_scale_y = self.T1_scale
        
    def ParentStylesUpdate(self):
        if self.ParentPlaceStyle!=None:
            if self.ParentPlace:
                self.Parent_position = self.ParentPlaceStyle.stylebuf['position']
                self.Parent_width = self.ParentPlaceStyle.stylebuf['place.width']
                self.Parent_height = self.ParentPlaceStyle.stylebuf['place.height']
            elif self.ParentButton:
                self.Parent_position = self.ParentPlaceStyle.style['position']
                self.Parent_width = self.ParentPlaceStyle.style['bt.width']
                self.Parent_height = self.ParentPlaceStyle.style['bt.height']
                
    def Update(self):
        
        
        self.T1_font_obj = pygame.font.SysFont(self.T1_font,self.T1_font_size,self.T1_bold,self.T1_italic)
        
        self.T1_textoutline_surface = self.T1_font_obj.render(self.T1_text,True,self.T1_outline_color)
        
        
        self.T1_text_surface = self.T1_font_obj.render(self.T1_text,self.T1_antialising,self.T1_color)
        
        self.T2_text_surface = self.T1_text_surface
        
        self.T1_surface = pygame.Surface([self.T2_text_surface.get_width()+self.T1_outline_size*2,self.T2_text_surface.get_height()+self.T1_outline_size*2]).convert()
        
        
        if self.T1_outline:
            for i in range(-self.T1_outline_size,self.T1_outline_size):
                for j in range(-self.T1_outline_size,self.T1_outline_size):
                    self.T1_surface.blit(self.T1_textoutline_surface,[self.T1_outline_size+j,self.T1_outline_size+i])
            self.T1_surface.blit(self.T2_text_surface,[self.T1_outline_size,self.T1_outline_size])
        else:
            self.T1_surface.blit(self.T2_text_surface,[0,0])
            
        self.T1_surface = pygame.transform.rotate(self.T1_surface,self.T1_rotate_angle)
        self.T1_surface = pygame.transform.scale(self.T1_surface,[self.T1_surface.get_width()*self.T1_scale_x,self.T1_surface.get_height()*self.T1_scale_y])
                    
        self.T1_surface.set_colorkey((0,0,0))
        self.T2_text_surface_width = self.T1_surface.get_width()
        self.T2_text_surface_height = self.T1_surface.get_height()
               
    def SelfStylesmanipulate(self):
        self.T2_position = [None,None]
        self.T3_position = [None,None]
        
        
        if self.T1_centering:
            self.T2_position = [
                self.T1_position[0]-self.T1_surface.get_width()/2,
                self.T1_position[0]-self.T1_surface.get_height()/2
            ]
        else:
            self.T2_position = self.T1_position

        if self.Placed: 
            self.T3_position[0]=self.T2_position[0] + self.Parent_position[0]
            self.T3_position[1]=self.T2_position[1] + self.Parent_position[1]
        else:
            self.T3_position = self.T2_position
        
        if type(self.T1_on_window)==str:
            if 'center' in self.T1_on_window:
                self.T3_position[0] = self.win.GET_WIN_WIDTH()/2-self.T2_text_surface_width/2+self.T1_on_window_dx
                self.T3_position[1] = self.win.GET_WIN_HEIGHT()/2-self.T2_text_surface_height/2+self.T1_on_window_dy
            
            if 'left' in self.T1_on_window:
                self.T3_position[0] = 0+self.T1_on_window_dx
            if 'right' in self.T1_on_window:
                self.T3_position[0] = self.win.GET_WIN_WIDTH()-self.T2_text_surface_width+self.T1_on_window_dx
            if 'top' in self.T1_on_window:
                self.T3_position[1] = 0+self.T1_on_window_dy
            if 'down' in self.T1_on_window:
                self.T3_position[1] = self.win.GET_WIN_HEIGHT()-self.T2_text_surface_height+self.T1_on_window_dy
                
        if type(self.T1_on_place)==str:
            if self.Placed:
                if 'center' in self.T1_on_place:
                    self.T3_position[0] = self.Parent_width/2-self.T2_text_surface_width/2+self.Parent_position[0]+self.T1_on_place_dx
                    self.T3_position[1] = self.Parent_height/2-self.T2_text_surface_height/2+self.Parent_position[1]+self.T1_on_place_dy
                if 'left' in self.T1_on_place:
                    self.T3_position[0] = 0+self.Parent_position[0]+self.T1_on_place_dx
                if 'right' in self.T1_on_place:
                    self.T3_position[0] = self.Parent_width-self.T2_text_surface_width+self.Parent_position[0]+self.T1_on_place_dx
                if 'top' in self.T1_on_place:
                    self.T3_position[1] = 0+self.Parent_position[1]+self.T1_on_place_dy
                if 'down' in self.T1_on_place:
                    self.T3_position[1] = self.Parent_height-self.T2_text_surface_height+self.Parent_position[1]+self.T1_on_place_dy
        
    def Render(self):
        self.ParentStylesUpdate()
        self.SelfStylesmanipulate()
        self.Update()
        self.win.screen.blit(self.T1_surface,self.T3_position)