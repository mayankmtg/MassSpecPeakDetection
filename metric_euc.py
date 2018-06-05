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

if(len(sys.argv)<3):
	print("python metric_euc.py csv_file.csv duplicate_file.csv")
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
# print("Distance Based")
# distance_matrix=eucd.cdist(vec_array, vec_array)
# print(distance_matrix.shape)
# minimum=np.max(distance_matrix, axis=0)
print("Correlation Based")
tup_duplicates=[]
count=0
for i in range(len(line_array)):
	for j in range(i+1,len(line_array)):
		if(abs(line_array[i][3]-line_array[j][3])<=mzdiff and abs(line_array[i][4]-line_array[j][4])<=rtdiff ):
			first_corr=pearsonr(vec_array[i],vec_array[j])[0]
			if(first_corr>=corrthresh):
				# print(line_array[i][1],line_array[j][1])
				count+=1
				tup_duplicates.append((i,j))
print(count)
# indices=np.argwhere(distance_matrix < 3000)
# print(indices)
# print(len(indices))


print("cvs-writing")


table_labels.remove('label')
table_labels.remove('isotopeLabel')
table_labels.remove('compound')
table_labels.remove('compoundId')
table_labels.remove('formula')
dell=","


write_flag=0
with open(sys.argv[2], 'w') as f:
	f.write('duplicate_id,'+dell.join(table_labels)+'\n')
	ind=1
	for t in tup_duplicates:
		f.write(str(ind)+','+dell.join(map(str,line_array[t[0]]))+'\n')
		f.write(str(ind)+','+dell.join(map(str,line_array[t[1]]))+'\n')
		ind+=1

