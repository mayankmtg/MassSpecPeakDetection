from mzxmlReader import mzxmlReader as mzx
from scan import scan
from mzslice import mzslice
import matplotlib.pyplot as plt
import numpy as np
from scipy import sparse
# from scipy.sparse.linalg import spsolve
from scipy.signal import savgol_filter
# from peakdetect import peakdetect
from scipy.signal import find_peaks_cwt

file_obj=mzx('../samples/file1.mzXML')
xml_scans=file_obj.getScans()
scan_arr=[]

def baselineShift(y, lam, p, niter=10):
	L=len(y)
	D=sparse.csc_matrix(np.diff(np.eye(L),2))
	w=np.ones(L)
	for i in xrange(niter):
		W=sparse.spdiags(w,0,L,L)
		Z=W+lam*D.dot(D.transpose())
		mxmx=np.array(w*y)
		print(Z.shape, mxmx.shape)
		z=sparse.linalg.spsolve(Z,w*y)
		w=p*(y>z)+(1-p)*(y<z)
	return z



def validSlice(sl):
	if(len(sl.getBin())<50):
		return False
	return True

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

looper=np.arange(minmz[0], maxmz[0], 0.2)
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
	# break

slice_smooth=[]
slice_array=[sl for sl in slice_array if validSlice(sl)]
for sl in slice_array:
	# x=[]
	# y=[]
	# for t in sl.getBin():
	# 	x.append(t[2])
	# 	y.append(t[1])
	curr_bin=sl.getBin();
	smoothing_win=len(curr_bin)/5
	if(smoothing_win<3):
		continue
	if(smoothing_win%2==0):
		smoothing_win+=1
	# print(len(x))
	# print(len(y))
	# print(smoothing_win)
	yhat=savgol_filter(curr_bin[:,1],smoothing_win,2)
	# yhat=curr_bin[:,1]
	sl.setSmoothWin(smoothing_win)
	bin_in=0
	for t in sl.getBin():
		sl.smooth_in(yhat[bin_in], bin_in)
		bin_in+=1

	# plt.plot(x,y, 'r--')
	# plt.plot(x,yhat,'r--', color='blue')
	# plt.show()
print("Baseline Correction")
for sl in slice_array:
	x=[]
	y=[]
	for t in sl.getBin():
		x.append(float(t[2].lstrip('PT').rstrip('S')))
		y.append(float(t[1]))

	z=baselineShift(y,1000,0.01,sl.smooth_win)
	# indices=find_peaks_cwt(y, np.arange(1,10))
	# for i in indices:
	# 	plt.axvline(x=x[i], color='blue')
	indices=find_peaks_cwt(y, np.arange(1,10))
	# indices=peakdetect(y,lookahead=10)
	for i in indices:
		plt.axvline(x=x[i], color='orange')
	# indices=find_peaks_cwt(y, np.arange(1,200))
	# for i in indices:
	# 	plt.axvline(x=x[i], color='red')
	plt.plot(x,y, 'r--')
	plt.plot(x,z,'r--', color='green')
	plt.show()

