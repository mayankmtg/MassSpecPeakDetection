from mzxmlReader import mzxmlReader as mzx
from scan import scan

file_obj=mzx('samples/file1.mzXML')
xml_scans=file_obj.getScans()
scan_arr=[]

for s in xml_scans:
	scan_obj=scan(s)
	peaks=s.getElementsByTagName('peaks')
	peak=peaks[0]
	encoded_string=peak.firstChild.nodeValue
	inms_pair=file_obj.decode64(encoded_string)
	scan_obj.setPeakPairs(inms_pair)
	scan_arr.append(scan_obj)

print(len(scan_arr))