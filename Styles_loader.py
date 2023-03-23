from Styles import Style
from pygl_nf import GL


def LoadFile(file,win: GL.Display_init_):
    file = open(file,'r')
    
    data = file.readlines()
    for i in range(len(data)):
        data[i] = data[i].replace('\n','')
        
        
    
    widgetName = ''
    allStyles = []
    styles = []
    
    for index,stroke in enumerate(data):
        if stroke == '}':
            
            allStyles.append([widgetName,styles,widgetgenname])
            widgetName = ''
            styles = []

        if stroke!='':
            try:
                ind = stroke.index(':')
                style_name = stroke[0:ind]
                style_value = stroke[ind+1:]
                
                style = [style_name.replace(' ',''),style_value]
                styles.append(style)
            except:...
            
        if stroke!='':
            if stroke[0] == '$' and stroke[-1] == '{':
                widgetName = stroke[1:-1]
                widgetgenname = stroke[0:-1]
            
    
    for styleobj in allStyles:
        
        for styleindex in range(len(styleobj[1])):
            
            stylevalue = styleobj[1][styleindex][1]

            
            if stylevalue =='True' or stylevalue == 'False':
                stylevalue = bool(stylevalue)
            else:
                try:
                    styleobj[1][styleindex][1] = float(stylevalue)
                except:
                    stylevalue = stylevalue.replace('(','')
                    stylevalue = stylevalue.replace(')','')
                    stylevalue = stylevalue.replace(',',' ')
                    stylevalue = list(stylevalue.split())
                    try:
                        styleobj[1][styleindex][1] = list(map(float,stylevalue))
                    except:...
                    
            try:
                if 'win.width' in stylevalue:
                    styleobj[1][styleindex][1] = win.GET_WIN_WIDTH()  

                if 'win.height' in stylevalue:
                    styleobj[1][styleindex][1] = win.GET_WIN_HEIGHT()
            except:...
            
            
            
            
                
    returnStyles = []
    for styleobj in allStyles:
        st = Style(styleobj[0])
        for style in styleobj[1]:
            st.SetValue(style[0],style[1])
            st.genname = styleobj[2]
            st.name = GetName(styleobj[2])
            
            
        returnStyles.append(st)
        
    return returnStyles

def GetName(stroke:str):
    dot_ind = stroke.find(':')
    scob_ind = stroke.find(')')
    if dot_ind!=-1 and scob_ind!=-1:
        return stroke[scob_ind+2:dot_ind]
    
    if dot_ind==-1 and scob_ind!=-1:
        return stroke[scob_ind+2:]
    
    

            
            
            
                
        
    
    
        
        
            
            
            
            
        
    
    
    
