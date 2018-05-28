from xml.dom import minidom
import base64
import struct

class mzxmlReader():

	def __init__(self, filename):
		self.mydoc=minidom.parse(filename)

	def getScans(self):
		scans=self.mydoc.getElementsByTagName('scan')
		return scans

	def decode64(self,encoded_string):
		mynr=base64.standard_b64decode(encoded_string)
		peaks_ints = []
		for i in range(0, len(mynr), 8):
			peak = struct.unpack('>f', mynr[i:i+4])
			inte = struct.unpack('>f', mynr[i+4:i+8])
			peaks_ints.append(tuple([peak[0], inte[0]]))
		return peaks_ints

