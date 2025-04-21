from kivymd.uix.textfield import MDTextField
from kivymd.app import MDApp       
from kivy.uix.relativelayout import RelativeLayout
from kivymd.uix.label import MDLabel,MDIcon 
from kivymd.uix.button import MDRaisedButton,MDRoundFlatButton 
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList,OneLineListItem,ThreeLineListItem
from kivymd.uix.scrollview import MDScrollView

class MyApp(MDApp):
    def build(self):
        myscroll=MDScrollView()
        mylist=MDList()
        item1=ThreeLineListItem(text="Uzbekistan",secondary_text="Samarkand Region",tertiary_text="Samarkand city")
        item2=ThreeLineListItem(text="Uzbekistan",secondary_text="Samarkand Region",tertiary_text="Samarkand Bukhara")
        
        
        mylist.add_widget(item1)
        mylist.add_widget(item2)
        myscroll.add_widget(mylist)
        
        return myscroll
    
MyApp().run()