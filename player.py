from kivy.uix.image import Image

class Player(Image):
	def __init__(self,*kwargs):
		super(Player,self).__init__()
		self.step = [
			'atlas://images/player/step_1',
			'atlas://images/player/step_2'
		]
		box = Image(source = self.step[0])
		self.size = box.texture_size
		del box
		self.new_step()
		
	def new_step(self):
		self.source = self.step.pop(0)
		self.step.append(self.source)
		
	def update(self,keyCode=None):
		self.new_step()
		
		dx = 5
		#~ if keyCode != 'right':
			#~ dx *= -1
		self.x += dx
