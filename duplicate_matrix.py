import numpy as np
import scipy.spatial.distance as eucd
from scipy.stats.stats import pearsonr
import sys

line_array=[]
vec_array=[]
print("Parameters:")
mzdiff=0.01
rtdiff=0.1
corrthresh=0.99
print("Median MZ Diff: "+ str(mzdiff))
print("Median RT Diff: "+ str(rtdiff))
print("Correlation Threshold: "+ str(corrthresh))
table_labels=0

if(len(sys.argv)<2):
	print("python metric_euc.py csv_file.csv")
	sys.exit(1)

with open(sys.argv[1]) as f:
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
		line_array.append(map(float,temp_array))
		temp_array=temp_array[9:]
		vec_array.append(map(float,temp_array))

line_array=np.array(line_array)
vec_array=np.array(vec_array)

print("Row Count: ", len(line_array))
print("Correlation Matrix Based")
nvec=len(line_array)
correlation_matrix=np.zeros((nvec,nvec))
for i in range(0,nvec):
	correlation_matrix[i][i]=1

# for i in range(nvec):
# 	for j in range(nvec):
# 		print(correlation_matrix[i][j]),
# 	print('\n')

for i in range(nvec):
	for j in range(i+1,nvec):
		if(abs(line_array[i][3]-line_array[j][3])<=mzdiff and abs(line_array[i][4]-line_array[j][4])<=rtdiff ):
			first_corr=pearsonr(vec_array[i],vec_array[j])[0]
			if(first_corr>=corrthresh):
				# print(line_array[i][1],line_array[j][1])
				correlation_matrix[i][j]=1
				correlation_matrix[j][i]=1
			else:
				correlation_matrix[i][j]=0
				correlation_matrix[j][i]=0


for i in range(nvec):
	for j in range(nvec):
		if i!=j and correlation_matrix[i][j]==1:
			correlation_matrix[i][j]=0
			correlation_matrix[j][i]=0
			correlation_matrix[j][j]=0
count=0
for i in range(nvec):
	if(correlation_matrix[i][i]==1):
		# print(line_array[i][1])
		count+=1
print(count)