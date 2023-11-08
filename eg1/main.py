import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivyir import IrLabel

class MyApp(App):
	def build(self,**kwargs):
		return IrLabel(text="hello world سلان")
		
MyApp().run()