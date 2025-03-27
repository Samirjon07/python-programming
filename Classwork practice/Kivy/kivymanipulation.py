from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon


class MyApp(MDApp):
    def build(self):
        l1=MDLabel(text="Enter Your Name: ",halign="center",theme_text_color="Error")
        l2=MDIcon(icon="android",halign="center",theme_text_color="Error")
        return l1
MyApp().run()