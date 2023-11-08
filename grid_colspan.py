import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyGrid(GridLayout):
	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs)
		self.cols = 1
		
		self.top_grid = GridLayout()
		self.top_grid.cols = 2
		
		self.top_grid.add_widget(Label(text="Name:"))		
		self.name = TextInput(multiline=False)
		self.top_grid.add_widget(self.name)
		
		self.top_grid.add_widget(Label(text="pizza:"))		
		self.pizza = TextInput(multiline=False)
		self.top_grid.add_widget(self.pizza)
		
		self.top_grid.add_widget(Label(text="Color:"))		
		self.color= TextInput(multiline=False)
		self.top_grid.add_widget(self.color)
		
		self.add_widget(self.top_grid)
		self.submit = Button(
			text="submit", 
			font_size=33
		)
		self.submit.bind(on_press=self.press)
		self.add_widget(self.submit)
		
	def press(self, instance):
		message = f"my name is {self.name.text} i love {self.pizza.text} and color is {self.color.text}"
		self.add_widget(
			Label(text=message)
		)
class MyApp(App):
	def build(self):
		return MyGrid()
		
MyApp().run()