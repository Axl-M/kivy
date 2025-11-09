# Задание параметров виджету Button – размер и положение

from kivy. app import App
from kivy.lang import Builder

KV = '''
Button:
    text: 'Это кнопка'
    # size_hint:.5,.5     # – относительный размер кнопки
    # – — – — – — – — – —
    # size_hint:.8,.5
    # size_hint:.5,.8
    # size_hint:.1,.05
    # pos_hint: {'center_x':.5, 'center_y':.5}  # относительное положение кнопки в окне приложения
    # – — – — – — – — – — – — – — – — – — – — – —
    # size_hint:.2,.1
    
    size_hint: None, None # отменить использование автоматической перерисовки элемента (подгонку под размер родительского виджета)
    size: 150, 50 # абсолютный размер элемента в пикселах, (150 – ширина элемента, 50 – высота элемента)
    
    # pos_hint: {'center_x':.15, 'center_y':.5}
    # pos_hint: {'center_x':.85, 'center_y':.5}
    # pos_hint: {'center_x':.5, 'center_y':.15}
    # pos_hint: {'center_x':.5, 'center_y':.85}
    # pos_hint: {'x':.5, 'y':.5}
    pos: 10, 40  # абсолютная позиция элемента в окне приложения в пикселах (140 – координата по оси x, 40 – координата по оси y)
'''

class MainApp (App):
    def build (self):
        return Builder.load_string(KV)

MainApp().run()