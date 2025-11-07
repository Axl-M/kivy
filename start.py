from kivy.config import Config
Config.set("graphics", "width", "500")
Config.set("graphics", "height", "400")
# Отключаем режим масштабирования окна
Config.set("graphics", "resizable", "0")

from kivymd.app import MDApp
from kivymd.uix.button import (MDIconButton, MDFloatingActionButton,
                               MDFlatButton, MDRaisedButton, MDFloatingActionButtonSpeedDial)

class FirstMDApp(MDApp):
    # если хотим темную тему
    def build(self):
        self.theme_cls.theme_style = "Dark"
        # return MDIconButton(icon="phone",
        #                     md_bg_color=(1, 0, 0, 1),
        #                     icon_size=50,
        #                     pos_hint={"center_x": 0.5, "center_y": 0.5})

        # return MDFloatingActionButton(icon="plus",
        #                               md_bg_color=(0, 1, 0.7, 0.7),
        #                               icon_color=(0, 0, 0, 1),
        #                               pos=(75, 75))

        # return MDFlatButton(text="Hello World!",
        #                     # font_name="Radiotechnika_0",
        #                     font_size=40,
        #                     md_bg_color=(1, 1, 1, 1),
        #                     theme_text_color="Custom",
        #                     text_color=(0, 0, 0, 1),
        #                     x=10,
        #                     y=50)

        # return MDRaisedButton(text="Hello World!",
        #                       size_hint=(0.3, 0.3),
        #                       pos_hint={"center_x": 0.5, "center_y": 0.5},
        #                       shadow_color=(1, 0, 0, 1))

        return MDFloatingActionButtonSpeedDial(icon="chart-areaspline",
                                               root_button_anim=True,
                                               data={'Line': 'chart-line',
                                                     'Bar': 'chart-bar',
                                                     'Pie': 'chart-pie'})


FirstMDApp().run()
