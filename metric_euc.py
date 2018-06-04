import numpy as np
import scipy.spatial.distance as eucd

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
with open('../csvFiles/test0.csv') as f:
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
print("Distance Based")
distance_matrix=eucd.cdist(vec_array, vec_array)
print(distance_matrix.shape)
# minimum=np.max(distance_matrix, axis=0)

# count=0
# for i in range(len(distance_matrix)):
# 	for j in range(i+1,len(distance_matrix)):
# 		if(distance_matrix[i][j]<3000 and abs(line_array[i][3]-line_array[j][3])<=mzdiff and abs(line_array[i][4]-line_array[j][4])<=rtdiff ):
# 			print(line_array[i][1],line_array[j][1])
# 			count+=1
# print(count)
indices=np.argwhere(distance_matrix < 3000)
print(indices)
print(len(indices))
