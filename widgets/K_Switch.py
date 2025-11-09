# кнопка – выключатель.
# При этом имитируется механический выключатель, который либо включается, либо выключается.
# Виджет Switch имеет два положения включено (on) – выключено (off)

from kivy. app import App
from kivy. uix. switch import Switch
from kivy.lang import Builder

KV = '''
Switch:
    # active: True
    active: False
    
# – active – состояние выключателя (по умолчанию имеет значение False)
# – on_touch_down – событие (касание выключателя);
# – on_touch_up – событие (выключатель отпущен);
# – on_touch_move – событие (касание выключателя с перемещением)
'''

class MainApp (App):
    def build (self):
        # sw = Switch (active=True)
        # return sw
        return Builder.load_string(KV)


MainApp().run()