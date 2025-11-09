# Явное связывание визуального элемента с функцией отклика на действия пользователя 

from kivy. app import App
# from kivy. uix. button import Button
from kivy.lang import Builder

KV= '''
Button:
    text: 'Кнопка'
    size_hint: .5, .5
    pos_hint: {'center_x':.5, 'center_y':.5}
    on_press: app.press_button(root)  # обращение к функции приложения, которая находится в корневом модуле (root) ОБЯЗАТЕЛЬНО
    # аргумент root можно не указывать (тогда в ф-ции убрать instance)
'''

class MainApp(App):
    def build (self):
        # button = Button(text='Кнопка',
        #     size_hint= (.5,.5),
        #     pos_hint= {'center_x':.5, 'center_y':.5})
        # button.bind(on_press=self.press_button)   # НЕОБЯЗАТЕЛЬНО (неявное связывание)
        # return button
        return Builder.load_string(KV)

    def press_button (self, instance):
        print('Вы нажали на кнопку!')

MainApp().run()