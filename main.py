import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock

class Game(BoxLayout):
	def update(self,dt):
		self.background.pos[0] -= 0.5
		
		if self.background.pos[0]<=0:
			self.background.pos[0] = self.width
	
class GameApp(App):
	def build(self):
		game = Game()
		Clock.schedule_interval(game.update, 2)
		return game


if __name__ == '__main__':
	GameApp().run()

