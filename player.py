from kivy.uix.image import Image

class Player(Image):
	step = [
			'atlas://images/player/step_1',
			'atlas://images/player/step_2',
			'atlas://images/player/step_3',
			'atlas://images/player/step_4',
			'atlas://images/player/step_5',
			'atlas://images/player/step_6'
		]

	def __init__(self,**kwargs):
		super(Player,self).__init__(**kwargs)
		self.new_step()
		
	def new_step(self):

		self.source = self.step.pop(0)
		self.size = self.texture_size
		self.step.append(self.source)
		
	def update(self,keyCode=None):
		
		dx = 5
		#~ if keyCode != 'right':
			#~ dx *= -1
		#~ self.x += dx
		self.x += self.width*0.25
		self.new_step()
	
		
