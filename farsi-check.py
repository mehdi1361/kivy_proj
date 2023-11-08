from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from kivy import Config
from kivy.uix.label import Label
from kivy.uix.widget import Widget
import arabic_reshaper
from bidi.algorithm import get_display

class MainApp(App):
    def build(self):
        reshaped_text = arabic_reshaper.reshape("فارسی")
        bidi_text = get_display(reshaped_text)
        
        return Label(text= bidi_text, font_size=30)

if __name__ == "__main__":
    MainApp().run()