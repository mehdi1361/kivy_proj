from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file("slider.kv")


class MyLayout(Widget):
    def slide_it(self, *args):
        print(args[1])
        self.slide_text.text = str(int(args[1]))
        self.ids.slider_label.font_size = int(args[1]) * 10

class MainApp(App):
    def build(self):
        return MyLayout()
    

if __name__ == "__main__":
    MainApp().run()