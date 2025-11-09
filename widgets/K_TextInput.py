from kivy. app import App
from kivy. uix. textinput import TextInput
from kivy.lang import Builder

KV = '''
TextInput:
    font_size: 30
    # color: 0,200,0
    # password_mask: '_'
    
'''

class MainApp (App):
    def build (self):
        # my_text = TextInput (font_size=30)
        # return my_text
        return Builder.load_string(KV)

MainApp().run()