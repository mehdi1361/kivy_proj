from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder


Builder.load_file('round.kv')

class MyLayout(Widget):
    pass


class MainApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyLayout()

if __name__ == "__main__":
    MainApp().run()
