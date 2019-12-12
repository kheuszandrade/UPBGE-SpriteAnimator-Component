##############################################
# Name: Sprite Animator                      #
# Description: Create animation with sprites #
# Author: Samuel Andrade                     #
# Version: 1.0                               #
##############################################
from bge import *
import time

class Timer():
	def __init__(self):
		self.LastTime = time.time()

	def GetTimer(self):
		return time.time() - self.LastTime

	def ResetTimer(self):
		self.LastTime = time.time()

class Animator(types.KX_PythonComponent):
	args = {
		"Mesh":"Mesh",
		"Init Delay": 0.0,
		"Frames": 0,
		"Duration": 0.0,
		"Time": 1.0,
		"Destroy In Last Frame": False,
		"Size":[1,1,1]
	}

	def start(self, args):
		self.mesh = args["Mesh"]
		self.init_delay = args["Init Delay"]
		self.frames = args["Frames"]
		self.duration = args["Duration"]
		self.time = args["Time"]
		self.destroy = args["Destroy In Last Frame"]
		self.size = args["Size"]
		self.timer = Timer()
		self.duration_timer = Timer()
		self.end_delay = False
		self.local_frame = 0

		self.object.localScale = self.size

	def update(self):
		if self.end_delay == False:
			if self.timer.GetTimer() >= self.init_delay:
				self.end_delay = True
		else:
			if self.duration == 0.0:
					self.Animate()
			else:
				if self.duration_timer.GetTimer() < self.duration:
						self.Animate()
				else:
					self.object.endObject()

	def Animate(self):
		if self.timer.GetTimer() >= self.time:
			self.object.replaceMesh(self.mesh+"_"+str(self.local_frame))
			self.local_frame += 1
			if self.local_frame > self.frames:
				if self.destroy == True:
					self.object.endObject()
				else:
					self.local_frame = 0
			self.timer.ResetTimer()