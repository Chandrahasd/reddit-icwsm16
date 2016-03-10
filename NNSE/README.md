NNSE
====

#### Requirement:
- SPAMS: http://spams-devel.gforge.inria.fr/

#### Usage
- ```spams_DL.py``` : finds sparse non negative embeddings
	- Input:

			-f input vector file(format: each line contain id and space seperated embedding)
			-d dimension of output embeddings
			-l regularization parameter
	- Output:

			out_nnse_embed.txt : Output embedding(format: same as input)
			out_nnse_dic.txt : learned dictionary

	- run ```python2.6 spams_DL.py [-h] -f VECTOR_FILEPATH -d K [-l LAMBDA]```


- ```reduce_dimension.py``` : Dimensionality reduction using SVD
	- ```python reduce_dimension.py input_file_name out_file_name final_dimension```
	- Input format: input matrix in sparse format(each line contain row_id col_id value)

