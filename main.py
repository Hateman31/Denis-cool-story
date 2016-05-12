import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock

class Game(FloatLayout):
	def update(self,dt):
		self.background.x -= 0.5

		if self.background.right<=0:
			self.background.x = self.width
	
class GameApp(App):
	def build(self):
		game = Game()
		Clock.schedule_interval(game.update, 1/110)
		return game


if __name__ == '__main__':
	GameApp().run()

