# Пример использования виджета Label

from kivy. app import App
from kivy.uix.label import Label
from kivy.lang import Builder

KV = '''
Label:
    text: "Это текст"
    font_size: 50
    color: 'magenta'
    

'''

class MainApp (App):
    def build (self):
        # L = Label (text="Это текст", font_size=50, color='magenta')
        # return L
        return Builder.load_string(KV)

MainApp().run()