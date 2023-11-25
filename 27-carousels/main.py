from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file("carousel.kv")

class MyLayout(Widget):
    pass

class MainApp(App):
    def build(self):
        return MyLayout()
    

if __name__ == "__main__":
    MainApp().run()