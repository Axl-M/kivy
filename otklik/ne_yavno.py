# Неявное связывание визуального элемента с функцией отклика на действия пользователя
from kivy.app import App
from kivy.uix. button import Button
# from kivy.lang import Builder

class Basic_Class(App):
    def build (self):
        button = Button(text='Кнопка',
            size_hint= (.5,.5),
            pos_hint= {'center_x':.5, 'center_y':.5})
        return button

    # обработчик нажатия в файле.kv ссылается на эту ф-цию
    def press_button(self):
        print('Вы нажали на кнопку!')

My_App = Basic_Class()
My_App.run()