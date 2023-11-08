from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget

Builder.load_file("float.kv")

class MainLayout(Widget):
	pass
	
	
class MainApp(App):
	def build(self):
		Window.clearcolor = (1,1,1,1)
		return MainLayout()
		
		
if __name__ == "__main__":
		MainApp().run()
		