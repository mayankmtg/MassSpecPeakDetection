from mzxmlReader import mzxmlReader as mzx
from scan import scan
import matplotlib.pyplot as plt

file_obj=mzx('samples/file1.mzXML')
xml_scans=file_obj.getScans()
scan_arr=[]

# scan arr contains all the scans of the class scan python
for s in xml_scans:
	scan_obj=scan(s)
	peaks=s.getElementsByTagName('peaks')
	peak=peaks[0]
	encoded_string=peak.firstChild.nodeValue
	inms_pair=file_obj.decode64(encoded_string)
	scan_obj.setPeakPairs(inms_pair)
	scan_arr.append(scan_obj)

print("Scans Loaded")
in_mz_rt=[]
for s in scan_arr:
	for p in s.peaks:
		newTup=(p[0], p[1], s.retentionTime)
		in_mz_rt.append(newTup)
in_mz_rt=sorted(in_mz_rt, key=lambda x:x[1])



# x=[]
# y=[]

# for s in scan_arr:
# 	for p in s.peaks:
# 		x.append(s.retentionTime)
# 		y.append(p[1])
# plt.scatter(x,y)
# plt.show()


