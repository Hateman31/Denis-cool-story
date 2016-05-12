import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock

class Game(BoxLayout):
	pass
	
class GameApp(App):
	def build(self):
		game = Game()
		return game


if __name__ == '__main__':
	GameApp().run()

