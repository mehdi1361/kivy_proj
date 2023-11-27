from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget


Builder.load_file("radio.kv")

class MyLayout(Widget):
    def checkbox_click(self, instance, active, topping):
        if active:
            self.ids.output_text.text = f"you select {topping}"



class MainApp(App):
    def build(self):
        return MyLayout()
    

if __name__ == "__main__":
    MainApp().run()
