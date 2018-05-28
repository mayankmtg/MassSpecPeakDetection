from xml.dom import minidom
import base64
import struct
mydoc=minidom.parse('samples/file1.mzXML')
scans=mydoc.getElementsByTagName('scan')



def myDecode(encoded):
	mynr=base64.standard_b64decode(encoded)
	peaks_ints = []
	for i in range(0, len(mynr), 8):
		peak = struct.unpack('>f', mynr[i:i+4])
		inte = struct.unpack('>f', mynr[i+4:i+8])
		peaks_ints.append(tuple([peak[0], inte[0]]))
	return peaks_ints



for s in scans:
	print(s.attributes['num'].value),
	peaks=s.getElementsByTagName('peaks')
	peak=peaks[0]
	encoded=peak.firstChild.nodeValue
	decoded=myDecode(encoded)
	for d in decoded:
		print(d),
	print()


