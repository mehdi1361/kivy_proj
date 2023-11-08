from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file("btn.kv")

class MyLayout(Widget):
	pass
	
class MainApp(App):
	def build(self):
		Window.clearcolor = (1,1,1,1)
		return MyLayout()
		
if __name__ == "__main__":
	MainApp().run()