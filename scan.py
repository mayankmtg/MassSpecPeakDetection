from xml.dom import minidom
class scan():
	def __init__(self, scan_data):
		self.num=scan_data.attributes['num'].value
		self.msLevel=scan_data.attributes['msLevel'].value
		self.peaksCount=scan_data.attributes['peaksCount'].value
		self.polarity=scan_data.attributes['polarity'].value
		self.scanType=scan_data.attributes['scanType'].value
		self.filterLine=scan_data.attributes['filterLine'].value
		self.retentionTime=scan_data.attributes['retentionTime'].value
		self.lowMz=scan_data.attributes['lowMz'].value
		self.highMz=scan_data.attributes['highMz'].value
		self.basePeakMz=scan_data.attributes['basePeakMz'].value
		self.basePeakIntensity=scan_data.attributes['basePeakIntensity'].value
		self.totIonCurrent=scan_data.attributes['totIonCurrent'].value
		self.peaks=None
		print("Scan "+self.num+" loaded")
	def setPeakPairs(self,peaks):
		self.peaks=peaks
		print("Peaks")
