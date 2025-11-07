import kivy.app
import kivy.uix.label


class MainApp(kivy.app.App):
    def build(self):
        return kivy.uix.label.Label(text="Привет от Kivy!")

app = MainApp(title="Первое приложение на Kivy")

app.run()
