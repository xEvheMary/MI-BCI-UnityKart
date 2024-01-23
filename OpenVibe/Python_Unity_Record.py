import os
import numpy as np
import time

start_event_ids = [33024, 769, 780]  # IDs of the three start events
end_event_id = 800  # ID of the end event
epoch_duration = 2.0

class MyOVBox(OVBox):
	def __init__(self):
		OVBox.__init__(self)
		
	def initialize(self):
		print('Initialize Script') 
		self.output[0].append(OVStimulationHeader(0., 0.))
		return
		
	def process(self):
		for chunkIdx in range( len(self.input[0]) ):
			chunk = self.input[0].pop()
			if(type(chunk) == OVStimulationSet):
				for stimIdx in range(len(chunk)):
					stim=chunk.pop()
					print('Received stim : ', stim.identifier, 'stamped at', stim.date, 's, current Time : ', self.getCurrentTime())	
				stimSet = OVStimulationSet(self.getCurrentTime(), self.getCurrentTime()+1./self.getClock())
				stimSet.append(OVStimulation(stim.identifier, self.getCurrentTime(), 0.2))
				self.output[0].append(stimSet)
		return
		
	def uninitialize(self):
		print('Uninitialize Script') 
		end = self.getCurrentTime()
		self.output[0].append(OVStimulationEnd(end, end))
		return

box = MyOVBox()
