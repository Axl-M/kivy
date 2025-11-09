from kivy. app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

KV = '''
BoxLayout:
    CheckBox:
        color: 200,0,0
        active: True
    CheckBox:
        
        
'''

class MainApp (App):
    def build (self):
        # checkbox = CheckBox ()
        # return checkbox

        # return CheckBox()

        return Builder.load_string(KV)

MainApp().run()