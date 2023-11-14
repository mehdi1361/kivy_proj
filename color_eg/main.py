import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('color.kv')

class MyGridLayout(Widget):
	name = ObjectProperty()
	pizza = ObjectProperty()
	color = ObjectProperty()
	result = ObjectProperty()
	
	def press(self):
		message = f"my name is {self.name.text} i love {self.pizza.text} and color is {self.color.text}"
		self.result.text = message
		
class MainApp(App):
	def build(self):
		return MyGridLayout()
MainApp().run()