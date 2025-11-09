from kivy. app import App
from kivy.uix.progressbar import ProgressBar
from kivy.lang import Builder

KV = '''
ProgressBar:
    max: 100
    value: 45
'''

class MainApp (App):
    def build (self):
        # Progress = ProgressBar (max=1000)
        # Progress.value = 650
        # return Progress
        return Builder.load_string(KV)

MainApp().run()