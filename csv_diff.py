import numpy as np
from scipy.stats.stats import pearsonr
import sys

print("Difference Parameters")
mzdiff=0
rtdiff=0
corrthresh=0.99
print("Median MZ Diff: "+ str(mzdiff))
print("Median RT Diff: "+ str(rtdiff))
print("Correlation Threshold: "+ str(corrthresh))
if(len(sys.argv)<3):
	print("python csv_diff.csv file1.csv file2.csv")
	sys.exit(0)

print("Programs gives the differences in file 2 with respect to file 1")
file1=sys.argv[1]
file2=sys.argv[2]


line_array1=[]
vec_array1=[]
with open(file1) as f:
	first=0
	for line in f:
		line=line.rstrip('\n')
		if(first==0):
			first=1
			table_labels=line.split(',')
			print("Removing Blanks")
			continue
		temp_array=line.split(',')
		t=5
		while(t!=0):
			temp_array.remove('')
			t-=1
		line_array1.append(map(float,temp_array))
		temp_array=temp_array[9:]
		vec_array1.append(map(float,temp_array))

line_array2=[]
vec_array2=[]
with open(file2) as f:
	first=0
	for line in f:
		line=line.rstrip('\n')
		if(first==0):
			first=1
			table_labels=line.split(',')
			print("Removing Blanks")
			continue
		temp_array=line.split(',')
		t=5
		while(t!=0):
			temp_array.remove('')
			t-=1
		line_array2.append(map(float,temp_array))
		temp_array=temp_array[9:]
		vec_array2.append(map(float,temp_array))

line_array1=np.array(line_array1)
line_array2=np.array(line_array2)
vec_array1=np.array(vec_array1)
vec_array2=np.array(vec_array2)
print(vec_array1.shape)
print(vec_array2.shape)
reported_difference=[]
for i in range(len(line_array2)):
	flag=0
	for j in range(len(line_array1)):
		if(abs(line_array1[j][3]-line_array2[i][3])<=mzdiff and abs(line_array1[j][4]-line_array2[i][4])<=rtdiff):
			first_corr=pearsonr(vec_array2[i],vec_array1[j])[0]
			if(first_corr==1):
				flag=1
	if(flag==0):
		reported_difference.append(line_array2[i])

print(len(reported_difference))
# for diff in reported_difference:
# 	print(diff)




