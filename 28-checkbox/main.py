from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget


Builder.load_file("checkbox.kv")

class MyLayout(Widget):
    tops = []
    def checkbox_click(self, instance, active, topping):
        if active == True:
            MyLayout.tops.append(topping)
            self.ids.output_text.text = f"you select {','.join(MyLayout.tops)}"
        else:
            MyLayout.tops.remove(topping)
            self.ids.output_text.text = f"you select {','.join(MyLayout.tops)}"



class MainApp(App):
    def build(self):
        return MyLayout()
    

if __name__ == "__main__":
    MainApp().run()
