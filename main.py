from mzxmlReader import mzxmlReader as mzx
from scan import scan
from mzslice import mzslice
import matplotlib.pyplot as plt
import numpy as np

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
mz_in_rt=[]
for s in scan_arr:
	for p in s.peaks:
		newTup=(p[0], p[1], s.retentionTime)
		mz_in_rt.append(newTup)
# TODO: Check for the order of intensity and mz
mz_in_rt=sorted(mz_in_rt, key=lambda x:x[0])



# x=[]
# y=[]

# for s in scan_arr:
# 	for p in s.peaks:
# 		x.append(s.retentionTime)
# 		y.append(p[1])
# plt.scatter(x,y)
# plt.show()
minmz=min(mz_in_rt, key=lambda x:x[0])
maxmz=max(mz_in_rt, key=lambda x:x[0])
minin=min(mz_in_rt, key=lambda x:x[1])
maxin=max(mz_in_rt, key=lambda x:x[1])
minrt=min(mz_in_rt, key=lambda x:x[2])
maxrt=max(mz_in_rt, key=lambda x:x[2])

looper=np.arange(minmz[0], maxmz[0], 0.1)
slice_array=[]
ind=0
for l in range(1, len(looper)):
	slice_mz_min=looper[l-1]
	slice_mz_max=looper[l]
	new_slice=mzslice(slice_mz_min, slice_mz_max)
	while(True):
		if(mz_in_rt[ind][0]>=slice_mz_min and mz_in_rt[ind][0]<slice_mz_max):
			new_slice.insert(mz_in_rt[ind])
			ind+=1
		else:
			break
	slice_array.append(new_slice)




