from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        self.title = "Приложение на Kivy.     made by AxL"
        self.icon = "py.ico" # "my.jpeg"
        label = Label(text="Привет от Kivy и Python!")
        return label

if __name__ == "__main__":
    app = MainApp()
    app.run()