from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.vector import Vector

class Talking(Widget):
	def __init__(self, target,**kwargs):
		super(Talking,self).__init__()
		
		#~ add talk bubble
		self.shape = Image(source='images/talk.png')
		self.shape.size = Vector(self.shape.texture_size)*0.7	
		
		#~ add label		
		self.label = Label()
		self.label.color=[.1,.45,.55,1]
		self.label.size = self.label.texture_size
		self.label.text_size = self.width*1.8,None
		self.label.font_size=23
		
		
		#~ create text
		with open('speech.txt') as f:
			self.phrase = f.readlines()
		self.label.text = self.phrase.pop(0)
		
		self.count = 0

	def update(self,target):
		self.shape.pos = target.x+33,target.top
		self.label.center = self.shape.center

		self.count +=1
		if self.count == 14:
			self.show()
			self.count = 4
	
	def show(self):
		if self.phrase:
			self.label.text = self.phrase.pop(0)
		self.add_widget(self.shape)
		self.add_widget(self.label)
	
	def hide(self):
		self.remove_widget(self.shape)
		self.remove_widget(self.label)
	
	def new_phrase(self):
		self.hide()
		
