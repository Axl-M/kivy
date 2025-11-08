# Демонстрация использования выражений в KV

from kivy. app import App
from kivy.lang import Builder

KV = '''
BoxLayout:
    orientation: 'vertical'
    Button:
        id: bt1
        # text: 'Кнопка 1'
        text: 'Отпущена' if bt1.state == 'normal' else 'Нажата'
    Label:
        # допускается использования некоторых
        # операторов и выражений Python. При этом выражение может занимать
        # только одну строку и должно возвращать значение. 
        text: 'Кнопка отпущена' if bt1.state == 'normal' else 'Кнопка нажата'
'''

class MainApp (App):
    def build (self):
        return Builder.load_string(KV)

MainApp().run()