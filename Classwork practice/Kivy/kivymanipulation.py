from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MyApp(MDApp):
    def build(self):
        return MDLabel(text="Enter Your Name: ",halign="center",theme_text_color="Error")
MyApp().run()