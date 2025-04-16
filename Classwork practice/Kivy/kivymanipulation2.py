from kivymd.uix.textfield import MDTextField
from kivymd.app import MDApp       
from kivy.uix.relativelayout import RelativeLayout
from kivymd.uix.label import MDLabel,MDIcon 
from kivymd.uix.button import MDRaisedButton,MDRoundFlatButton 
from kivy.uix.screen import Screen
from kivy.uix.dialog import MDDialog


class MyApp(MDApp):
    def build(self):    
        lo=RelativeLayout()
        text_field =MDTextField(hint_text="Enter Your Name:",helper_text="Please!",icon_right="account",multiline=False, pos_hint={"center_x":0.5,"center_y":0.9})
        lo.add_widget(text_field)
        
        password_field =MDTextField(hint_text="Enter Your Password:",helper_text="Please!",password=True, icon_right="lock",multiline=False, pos_hint={"center_x":0.5,"center_y":0.8})
        lo.add_widget(password_field)
        
        signin_button = MDRaisedButton(text="Sign in",pos_hint={"center_x":0.5,"center_y":0.7},on_press=self.click)
        
        
        
        lo.add_widget(signin_button)
    
        return lo   
    def click(self,instance):
            print("You clicked me")
        #signin_button.bind(on_press=self.click)
    
    
MyApp().run()