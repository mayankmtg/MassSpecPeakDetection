class mzslice():
	def __init__(self, mz_min, mz_max):
		self.mz_min=mz_min
		self.mz_max=mz_max
		self.bin=[]
	
	def insert(self, tup):
		self.bin.append(tup)

	def getBinSize(self):
		return len(self.bin)