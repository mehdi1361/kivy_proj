from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file("label.kv")
class MyLayout(Widget):
	def prees(self):
		name = self.ids.name_input.text
		
		self.ids.name_label.text = f"hello {name}"
		self.ids.name_input.text = ""
	

class MainApp(App):
	def build(self):
		return MyLayout()
		
if __name__ == "__main__":
	MainApp().run()