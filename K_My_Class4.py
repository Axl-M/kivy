# Пример использования динамического класса (Пользовательский)

from kivy. app import App
from kivy.lang import Builder

# KV = '''
# BoxLayout:
#     Button:
#         text: "Кнопка 1"
#         pos_hint: {'center_x':.5, 'center_y':.6}
#         font_size: '25sp'
#         markup: True
#     Button:
#         text: "Кнопка 2"
#         pos_hint: {'center_x':.5, 'center_y':.6}
#         font_size: '25sp'
#         markup: True
#     Button:
#         text:  "Кнопка 3"
#         pos_hint: {'center_x':.5, 'center_y':.6}
#         font_size: '25sp'
#         markup: True

# чтобы не повторять многократно задание одних и тех же свойств каждому элементу
KV = '''
<MyButton@Button>:
    pos_hint: {'center_x':.5, 'center_y':.6}
    font_size: '25sp'
    markup: True

BoxLayout:
    orientation: "vertical"
    MyButton:
        text: "Кнопка 1^"
    MyButton:
        text: "Кнопка 2^"
    MyButton:
        text: "Кнопка 3^"
'''



class MainApp (App):
    def build (self):
        return Builder.load_string(KV)

MainApp().run()