from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('main.kv')

class MyLayout(Widget):
    def press(self):
        print("hello world")

class MainApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == "__main__":
    MainApp().run()