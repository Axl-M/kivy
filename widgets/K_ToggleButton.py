# кнопка с эффектом залипания
# она нажимается и остается в нажатом состоянии,
# после второго касания кнопка возвращается в исходное состояние

from kivy. app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.lang import Builder

KV = '''
ToggleButton:
    text: 'Кнопка'
    font_size: 50

'''

class MainApp (App):
    def build (self):
        # t_but = ToggleButton (text='Кнопка', font_size=50)
        # return t_but
        return Builder.load_string(KV)

MainApp().run()