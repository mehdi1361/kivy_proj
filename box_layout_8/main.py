from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('box.kv')

class MyLayout(Widget):
	pass
	
class MainApp(App):
	def build(self):
		return MyLayout()
		
MainApp().run()