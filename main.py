import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Translate, PushMatrix, PopMatrix

from player import Player
from talking import Talking
from background import Background

class Game(Widget):
	def __init__(self):
		super(Game,self).__init__()

		start_xy = (5,40)
		self.player = Player(pos = start_xy)
		self.talking = Talking(self.player)
		
		self.street1 = Background(
			view_h= Window.height,
			source = 'images/street1.png'
			)
		
		self.street2 = Background(
			view_h= Window.height,
			source = 'images/street1.png',
			x = self.street1.right			
			)
			
		self.add_widget(self.street1)
		self.add_widget(self.street2)
		self.add_widget(self.talking)
		self.add_widget(self.player)
		
		#~ self.current = 
		
	def update(self,dt):
		
		#~ if self.player.right < 1264:
		if 1:
			self.player.update()
			self.talking.update(self.player)
			#~ if self.player.x>self.street2.x:
				#~ self.street.x += self.street.width*2
		self.set_focus(*self.player.center)
		
	def set_focus(self, x, y):
		self.area_set_focus(x, y)
		self.set_view()
			
	def area_set_focus(self,x,y):
		#~ if self.finish:
			#~ offset_max_x = self.finish - self.width
		#~ else:
			#~ offset_max_x = None
		offset_max_x = 1264 - self.width
		offset_max_y = self.player.height*1.5
		offset_min_x = offset_min_y = 0
		
		fx = x - self.width//2
		fy = y - offset_max_y
		
		#~ if offset_max_x and (fx > offset_max_x):
		    #~ fx = offset_max_x
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
	
	def on_touch_down(self,touch):
		if touch.button =='left':
			self.talking.hide()
			
class GameApp(App):
	def build(self):
		game = Game()
		Clock.schedule_interval(game.update, 1/15)
		return game


if __name__ == '__main__':
	GameApp().run()

