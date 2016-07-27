from kivy.uix.image import Image
from kivy.vector import Vector as vector

class Background(Image):
	def __init__(self,view_h = None,**kwargs):
		super(Background,self).__init__(**kwargs)
		self.size_hint = (None,None)
		self.allow_stretch = True
		scale = view_h/self.texture_size[1]
		self.size = vector(self.texture_size)*scale
		
if __name__ == '__main__':
	from kivy.app import App
	from kivy.uix.boxlayout import BoxLayout
	from kivy.uix.widget import Widget
	from kivy.core.window import Window
	
	class Test(Widget):
		def __init__(self,**kwargs):
			super(Test,self).__init__(**kwargs)
			background = Background(
				view_h = Window.height,
				source = 'images/street1.png',
			)
			self.add_widget(background)		
			
	class StreetApp(App):
		def build(self):
			game = Test()
			
			return game
	
	StreetApp().run()
