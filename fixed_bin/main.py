from mzxmlReader import mzxmlReader as mzx
from scan import scan
from mzslice import mzslice
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
from scipy.signal import find_peaks_cwt

file_obj=mzx('../samples/file1.mzXML')
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

# print("Scans Loaded")
mz_in_rt=[]
for s in scan_arr:
	for p in s.peaks:
		newTup=[p[0], p[1], s.retentionTime]
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
		if(mz_in_rt[ind][0]>=slice_mz_min-0.025 and mz_in_rt[ind][0]<slice_mz_max+0.025):
			new_slice.insert(mz_in_rt[ind])
			ind+=1
		else:
			new_slice.sortBin()
			break
	slice_array.append(new_slice)
	break

slice_smooth=[]
for sl in slice_array:
	x=[]
	y=[]
	for t in sl.getBin():
		x.append(t[2])
		y.append(t[1])
	smoothing_win=len(x)/5
	if(smoothing_win%2==0):
		smoothing_win+=1
	print(len(x))
	print(len(y))
	print(smoothing_win)
	poly_order=3
	if(smoothing_win<=poly_order):
		poly_order=smoothing_win-1
	yhat=savgol_filter(y,smoothing_win,poly_order)
	bin_in=0
	for t in sl.getBin():
		sl.smooth_in(yhat[bin_in], bin_in)
		bin_in+=1

	plt.plot(x,y, 'r--')
	plt.plot(x,yhat,'r--', color='blue')
	plt.show()

for sl in slice_array:
	x=[]
	y=[]
	for t in sl.getBin():
		x.append(float(t[2].lstrip('PT').rstrip('S')))
		y.append(t[1])

	indices=find_peaks_cwt(y, np.arange(1,10))
	for i in indices:
		plt.axvline(x=x[i], color='blue')
	indices=find_peaks_cwt(y, np.arange(1,100))
	for i in indices:
		plt.axvline(x=x[i], color='green')
	indices=find_peaks_cwt(y, np.arange(1,200))
	for i in indices:
		plt.axvline(x=x[i], color='red')
	plt.plot(x,y, 'r--')
	plt.show()

