from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MainApp(MDApp):
    def build(self):
        self.title = "Приложение на KivyMD     by AxL"
        self.icon = "my.jpeg"
        label = MDLabel(text="Привет от KivyMD!", halign="center")
        return label

app = MainApp(title="Первое приложение на KivyMD")
app.run()

