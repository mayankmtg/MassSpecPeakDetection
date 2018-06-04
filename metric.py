import numpy as np
from scipy.stats.stats import pearsonr
line_array=[]
print("Parameters:")
mzdiff=0.01
rtdiff=0.1
corrthresh=0.99
print("Median MZ Diff: "+ str(mzdiff))
print("Median RT Diff: "+ str(rtdiff))
print("Correlation Threshold: "+ str(corrthresh))

with open('../csvFiles/test0.csv') as f:
	first=0
	for line in f:
		if(first==0):
			first=1
			print("Removing Blanks")
			continue
		line=line.rstrip('\n')
		temp_array=line.split(',')
		t=5
		while(t!=0):
			temp_array.remove('')
			t-=1
		# temp_array=temp_array[14:]
		line_array.append(map(float,temp_array))
line_array=np.array(line_array)
count=0
print("Row Count: ", len(line_array))
print("Correlation")
for i in range(len(line_array)):
	for j in range(i+1,len(line_array)):
		v1=line_array[i][9:]
		v2=line_array[j][9:]
		first_corr=pearsonr(v1,v2)[0]
		if(first_corr>=corrthresh and abs(line_array[i][3]-line_array[j][3])<=mzdiff and abs(line_array[i][4]-line_array[j][4])<=rtdiff):
			count+=1
print("Number of duplicates: "),
print(count)
print("Percentage duplicates: "),
print(float(count)/float(len(line_array)))