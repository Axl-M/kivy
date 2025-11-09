from kivy. app import App
from kivy.uix.image import Image
from kivy.lang import Builder

KV = '''
BoxLayout:
    Image:
        source: "../my.jpeg"
        color: 10,0,0,0.3
    Image:
        source: "../my.jpeg"
    Slider:
        orientation: 'vertical'
    Slider:
        orientation: 'horizontal'
        value_track: True
        value_track_color: 1, 0, 0, 1
'''

class MainApp (App):
    def build (self):
        # img = Image(source="../my.jpeg")
        # return img
        return Builder.load_string(KV)

MainApp().run()