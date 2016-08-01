import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Translate

from player import Player
from talking import Talking
from background import Background

class Game(Widget):
	def __init__(self):
		super(Game,self).__init__()

		start_xy = (5,40)
		self.player = Player(pos = start_xy)
		self.talking = Talking(self.player)
		
		self.lane = Background(
			view_h= Window.height,
			source = 'images/lane.png'
		)
		
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
		
		self.stopline = self.street1.right
		self.lane_status = 0
		
	def update(self,dt):
		
		if self.talking.phrase:
			delta = Window.width//2			
			delta += self.player.right
			
			#~ frame's right side == camera right side
			if delta >= self.street1.right:
				self.street2.x = self.street1.right
				self.stopline = self.street2.right
				
			#~ frame's right side == camera right side
			if delta >= self.street2.right:
				self.street1.x = self.street2.right
				self.stopline = self.street1.right

		else:
			if not self.lane_status:
				self.lane.x = self.stopline
				self.add_widget(self.lane,index = 2)
				self.lane_status = 1
				self.stopline = self.lane.right
			
		if self.player.right < self.stopline:
			self.player.update()
			self.talking.update(self.player)

		self.set_focus(*self.player.center)
		
	def set_focus(self, x, y):
		self.area_set_focus(x, y)
		self.set_view()
			
	def area_set_focus(self,x,y):
		offset_max_x = None
		if not self.talking.phrase:
			offset_max_x = self.stopline - self.width
		offset_max_y = self.player.height*1.5
		offset_min_x = offset_min_y = 0
		
		fx = x - self.width//2
		fy = y - offset_max_y
		
		if offset_max_x and (fx > offset_max_x):
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

