from kivymd.uix.textfield import MDTextField
from kivymd.app import MDApp       
from kivy.uix.relativelayout import RelativeLayout
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.button import MDRaisedButton,MDRoundFlatButton 
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList,OneLineListItem,ThreeLineListItem,OneLineIconListItem
from kivymd.uix.scrollview import MDScrollView
from kivy.lang.builder import Builder

x="""
ScrollView:
    MDList:
        ThreeLineIconListItem:
            text: "Uzbekistan" 
            secondary_text: "Samarkand Region"
            tertiary_text: "Samarkand city" 
            IconLeftWidget: 
                icon: "account"
            
        ThreeLineIconListItem:
            text: "Uzbekistan" 
            secondary_text: "Bukhara Region"
            tertiary_text: "Bukhara" 
            IconLeftWidget: 
                icon: "account"
            
        ThreeLineIconListItem:
            text: "Uzbekistan" 
            secondary_text: "Qashqadarya Region"
            tertiary_text: "Qarshi" 
            IconLeftWidget: 
                icon: "account"
            """
            
class MyApp(MDApp):
    def build(self):
        a=Builder.load_string(x)
        
        return a
MyApp().run()