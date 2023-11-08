import functools
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder

#Window.size = (500, 400)
Builder.load_file("calc.kv")

class MyLayout(Widget):
	def clear_end(self):
		data = self.ids.calc_input.text
		self.ids.calc_input.text = data[:-1]
		
		if len(data[:-1]) == 0:
			self.ids.calc_input.text ="0"
		
		
	def clear(self):
		self.ids.calc_input.text ="0"
		
	def print_val(self, button):
		if self.ids.calc_input.text == "0":
			self.ids.calc_input.text = ""
			
		self.ids.calc_input.text += button
		
	def equal(self):
		self.ids.calc_input.text = str(eval(self.ids.calc_input.text))
		
	def dot(self):
		self.ids.calc_input.text += "."
		
		

class CalcApp(App):
	def build(self):
		return MyLayout()
		
		
if __name__ == "__main__":
	CalcApp().run()