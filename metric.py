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
		# temp_array=temp_array[14:]
		line_array.append(map(float,temp_array))
line_array=np.array(line_array)
count=0
print("Row Count: ", len(line_array))
print("Correlation")
tup_duplicates=[]
for i in range(len(line_array)):
	for j in range(i+1,len(line_array)):
		v1=line_array[i][9:]
		v2=line_array[j][9:]
		first_corr=pearsonr(v1,v2)[0]
		if(first_corr>=corrthresh and abs(line_array[i][3]-line_array[j][3])<=mzdiff and abs(line_array[i][4]-line_array[j][4])<=rtdiff):
			count+=1
			tup_duplicates.append((i,j))
print("Number of duplicates: "),
print(count)
# print(len(tup_duplicates))
print("Percentage duplicates: "),
print(float(count)/float(len(line_array)))
print("cvs-writing")


table_labels.remove('label')
table_labels.remove('isotopeLabel')
table_labels.remove('compound')
table_labels.remove('compoundId')
table_labels.remove('formula')
dell=","


write_flag=0
with open('../csvFiles/duplicates.csv', 'w') as f:
	f.write('duplicate_id,'+dell.join(table_labels)+'\n')
	ind=1
	for t in tup_duplicates:
		f.write(str(ind)+','+dell.join(map(str,line_array[t[0]]))+'\n')
		f.write(str(ind)+','+dell.join(map(str,line_array[t[1]]))+'\n')
		ind+=1

