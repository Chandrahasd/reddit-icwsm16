# python reduce_dimension.py input_file_name out_file_name final_dimension
# input file format : each line contains (doc_id word_id count)
import scipy.sparse as ssp
import scipy.sparse.linalg as ssl
import sys

data_file=open(sys.argv[1],'r+')
output_file=open(sys.argv[2],'w')
final_dimension = int(sys.argv[3])

row_ids=[]
col_ids=[]
data=[]
for line in data_file:
	t=line.strip().split()
	row_ids.append(int(t[0]))
	col_ids.append(int(t[1]))
	data.append(float(t[2]))

Y=ssp.csc_matrix((data,(row_ids,col_ids)), shape=(max(row_ids)+1,max(col_ids)+1))
u=ssl.svds(Y,k=final_dimension,return_singular_vectors="u")
counter=0
for singular_vector in u[0]:
	output_file.write(str(counter)+" "+" ".join([str(ele) for ele in singular_vector ] )+"\n")
	counter+=1

data_file.close()
output_file.close()
