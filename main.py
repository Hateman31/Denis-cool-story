import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Translate, PushMatrix, PopMatrix
from player import Player

class Game(Widget):
	step = [
		'atlas://images/player/step_1',
		'atlas://images/player/step_2'
		]
	def __init__(self):
		super(Game,self).__init__()
		#~ self.player = self.ids.player
		self.player = Player()
		self.add_widget(self.player)
		
	def update(self,dt):
		
		#~ self.player.update(keyCode)
		if self.player.right < 1264:
			self.player.update()
		self.set_focus(*self.player.center)
		
	def set_focus(self, x, y):
		self.area_set_focus(x, y)
		self.set_view()
			
	def area_set_focus(self,x,y):
		offset_max_x = 1264 - self.width
		offset_max_y = self.player.height*1.5
		offset_min_x = offset_min_y = 0
		
		fx = x - self.width//2
		fy = y - offset_max_y
		
		if fx > offset_max_x:
		    fx = offset_max_x
		if fx < offset_min_x:
		    fx = offset_min_x
		
		if fy > offset_max_y:
		    fy = offset_max_y
		if fy < offset_min_y:
		    fy = offset_min_y
		
		self.delta_x = int(fx)
		self.delta_y = int(fy)

	def set_view(self):
		fx, fy = self.delta_x,self.delta_y
		self.canvas.before.clear()
		with self.canvas.before:
			Translate(-fx, -fy)

class GameApp(App):
	def build(self):
		game = Game()
		Clock.schedule_interval(game.update, 1/25)
		return game


if __name__ == '__main__':
	GameApp().run()

