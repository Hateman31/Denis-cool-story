from kivy.uix.image import Image

class Player(Image):
	def __init__(self,**kwargs):
		super(Player,self).__init__()
		#~ self.step = [
		#~ 'atlas://images/player/step_1',
		#~ 'atlas://images/player/step_2'
		#~ ]
		self.step = [
			'atlas://images/player/step_1',
			'atlas://images/player/step_2',
			'atlas://images/player/step_3',
			'atlas://images/player/step_4',
			'atlas://images/player/step_5',
			'atlas://images/player/step_6'
		]
		#~ box = Image(source=self.step[0])
		#~ self.size = box.texture_size
		#~ del box
		self.new_step()
		
	def new_step(self):
		#~ for x in self.step[:3]:
			#~ self.source = x
			#~ self.size = self.texture_size

		self.source = self.step.pop(0)
		self.size = self.texture_size
		self.step.append(self.source)
		
	def update(self,keyCode=None):
		
		dx = 5
		#~ if keyCode != 'right':
			#~ dx *= -1
		self.x += dx
		self.new_step()
	
		
