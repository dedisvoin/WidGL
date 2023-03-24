# WidGL
WidGL - это небольшой модуль для компилирования стилей виджетов.


Чтобы начать исползовать WidGL необходимо установить модуль pygl_nf через pip
Обязательно v21.8 
```pip
pip install pygl-nf==21.8
```
Код создания окна выглядит так, правда меньше чеи в pygame?
```python
from pygl_nf import GL
 
win = GL.Display_init_(flags=GL.D_Full)
 
while win.CEUF():
    pass
```

После необходимо установить сам парсер WidScrypt
```pip
pip install WidGL
```


# Подготовка необходимых файлов.
Сначала нужно скачать все файлы с данного репозитория и положить их в одну папку.

Для начала импортируем все нобходимые модули
```python
from WidGL import Styles_loader,wrapper
# python      version 3.10.4  [ рекомендуется ]
# pygl_nf     version 22.1 
from pygl_nf import GL
```

Далее создадим объект окна
```python
win = GL.Display_init_(flags=GL.D_Full,size=[700,400])
```

Загрузим наш файл со стилями виджетов
```python
style = Styles_loader.LoadFile('style.txt',win)
```


Создадим объект контроллер он и будет создавать и управлять всеми виджетами
```python
w = wrapper.Wrapper(style,win)
```

Запустим цикл отрисовки
```python
while win.CEUF(FPS=1000):
    w.Render()
    
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
После нам необходимо запустить наш файл с расширением ```.py``` и мы увидем:


![Снимок экрана 2023-03-24 124708](https://user-images.githubusercontent.com/88434293/227486150-0f8a25b5-1f83-43a1-9aa8-be8e8147bd43.png)

# Вот небольшой гайд.

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
Класс ```place``` обьединяет все атрибуты присущие лишь данному классу.

Атрибут ```position``` общий атрибут, его могут использовать объекты любых видов.

Создание кнопки.
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
Сдесь мы используем наследование. 
Текст наследуется от поверхности кнопи при помощи ```:```, тем самым мы можем легко позиционировать текст на кнопке при помощи атрибута ```text.om.place``` указывая необходимое нам положение.

Мы можем добавить текст отдельно.
```ruby
$text() t1:UpPlace{
    text:My style language!
    text.on.place:top center
    text.on.place.dy:10
    text.color:(255,255,255)
    text.font.size:50
    text.font:calibri
}
```
# Некоторые полезные атрибуты.

## Для текста

```text.outline``` включение выключение обводки текста

```text.outline.color``` цвет обводки текста в rgb формате

```text.outline.size``` ширина обводки

```text.on.place``` позиция текста относительно поверхности или кноки, может принимать ```center``` ```top``` ```down``` ```left``` ```right```

```text.on.place.dx``` cмещение текста отновистельно поверхности или кнопки по оси x

```text.on.place.dy``` cмещение текста отновистельно поверхности или кнопки по оси y

```text.font``` устанавливает шрифт

```text.bold``` устанавливает будет ли ваш шрифт жирным или нет, принимает 1 или 0

```text.italic``` устанавливает будет ли ваш шрифт под наклоном или нет, принимает 1 или 0

```text.centering``` цетрирует текст относительно своих координат

```text.scale``` коэфициент масштабирования текста

```text.on.window``` позиция текста относительно окна приложения, может принимать ```center``` ```top``` ```down``` ```left``` ```right```


## Для поверхности

