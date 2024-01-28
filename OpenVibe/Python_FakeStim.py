import os
import numpy as np
import time

start_event_ids = [33024, 769, 780]  # IDs of the three events
end_event_id = 800  # ID of the end event
epoch_duration = 2.0

class MyOVBox(OVBox):
	def __init__(self):
		OVBox.__init__(self)
		
	def initialize(self):
		print('Initialize Script') 
		class_1 = OpenViBE_stimulation[self.setting['Class1']]
		class_2 = OpenViBE_stimulation[self.setting['Class2']]
		class_3 = OpenViBE_stimulation[self.setting['Class3']]
		self.output[0].append(OVStimulationHeader(0., 0.))
		self.class_cycle = [class_1, class_2, class_3, class_2]
		self.prev_time = 0
		print(class_1)
		return
		
	def process(self):
		for chunkIdx in range( len(self.input[0]) ):
			chunk = self.input[0].pop()
			if(type(chunk) == OVStimulationSet):
				if len(chunk) > 0:
					stim=chunk.pop()
					ct = self.getCurrentTime()
					print('Received stim : ', self.class_cycle[0], 'stamped at', stim.date, 's, current Time : ', ct)
					stimSet = OVStimulationSet(ct, (ct+1.)/(ct - self.prev_time))
					stimSet.append(OVStimulation(self.class_cycle[0], self.getCurrentTime(), 0.2))
					self.output[0].append(stimSet)
					self.class_cycle.append(self.class_cycle.pop(0))
					self.prev_time = ct
		return
		
	def uninitialize(self):
		print('Uninitialize Script') 
		end = self.getCurrentTime()
		self.output[0].append(OVStimulationEnd(end, end))
		return

box = MyOVBox()
