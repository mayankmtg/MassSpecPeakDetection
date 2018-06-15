import numpy as np
class mzslice():
	def __init__(self, mz_min, mz_max):
		self.mz_min=mz_min
		self.mz_max=mz_max
		self.bin=[]
		self.bin_np=[]
	
	def insert(self, tup):
		self.bin.append(tup)
	def getBinSize(self):
		return len(self.bin)
	def getBin(self):
		return np.array(self.bin)
	def sortBin(self):
		# Time wise sort the bin
		self.bin=sorted(self.bin, key=lambda x:x[2])
	def smooth_in(self,intensity,bin_in):
		self.bin[bin_in][1]=intensity
		
