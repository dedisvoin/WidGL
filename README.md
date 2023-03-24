# WidGL


Чтобы начать исползовать WidGL необходимо установить модуль pygl_nf через pip
Обязательно v21.8 
```pip
pip install pygl-nf==21.8
```


# Подготовка необходимых файлов.
Сначала нужно скачать все файлы с данного репозитория и положить их в одну папку.

В этой же папке необходимо создать файл ```main.py``` вот с таким кодом.
```python
# python 3.10.4

from pygl_nf import GL
from Styles_loader import LoadFile
from wrapper import Wrapper_v2

win = GL.Display_init_(flags=GL.D_Resize,size=[700,400])  # создание окна

style = LoadFile('style.txt',win)                         # загрузка файла стилей

w = Wrapper_v2(style,win)                                 # парсинг стилей

timer = 1                                                 # таймер для обновления виджетов

while win.CEUF(FPS=1000):                                 # цикл работы
    timer+=1                                              # таймер для обновления виджетов
    if timer%200==0:                                      # таймер для обновления виджетов
        try:
            style = LoadFile('style.txt',win)
            w = Wrapper_v2(style,win)
        except:...
    
    
    w.Render()                                            # отрисовка виджетов
```

Далее необходимо создать сам файл ```style.txt``` где мы и будем прописывать стили.

##### Вот базовый пример.
```ruby
$place() bgPlace{
    position:(0,0)
    place.rougres:20
    place.color:(200,200,200)
    place.width:win.width
    place.height:win.height
    place.on.window:None
}

$place() UpPlace:bgPlace{
    position:(0,0)
    place.color:(150,100,200)
    place.rougres:20
    place.width:500
    place.height:400
    place.on.place:center top
    place.outline.size:5
    place.outline.color:(200,150,250)
}

$place() UpPlac:UpPlace{
    position:(0,0)
    place.on.place:center down
    place.width:490
    place.color:(100,50,150)
    place.rougres:15
    place.on.place.dy:-5
    
}

$text() t1:UpPlace{
    text:My style language!
    text.on.place:top center
    text.on.place.dy:10
    text.color:(255,255,255)
    text.font.size:50
    text.font:calibri
}

$text() t2:UpPlac{
    text:By DEVER
    text.on.place:right down
    text.on.place.dy:10
    text.color:(100,50,150)
    text.font.size:30
    text.font:calibri
    text.outline:1
    text.outline.size:2
    text.outline.color:(0,0,10)
    text.on.place.dy:0
    text.on.place.dx:-10
}
```
После нам необходимо запустить ```main.py``` и мы увидем:


![Снимок экрана 2023-03-24 124708](https://user-images.githubusercontent.com/88434293/227486150-0f8a25b5-1f83-43a1-9aa8-be8e8147bd43.png)

# Вот еже несколько примеров.

Это простой пример создания подповерхности.

```ruby
$place() bgPlace{
    position:(0,0)
    place.rougres:20
    place.color:(200,200,200)
    place.width:win.width
    place.height:win.height
    place.on.window:None
}
```
А это создание кнопки.
```ruby
$button() bt{
    position:(10,10)
    bt.width:200
    bt.height:50
    bt.color:(150,50,255)
    bt.release.color:(50,100,150)
    bt.rougres:defold-10 press-10 releas-10
}

$text() btText:bt{
    position:(0,0)
    text:Press me!
    text.on.place:center
    text.font.size:30
    text.color:(50,50,80)
}
```
Сдесь мы используем наследование. Текст наследуется от поверхности кнопи при помощи ```:```, тем самым мы можем легко позиционировать текст на кнопке.

