#python2.6 spams_DL.py -f vector_file -d dict_size -l regul_constant
#spams wrapper for finding Non-Negative Sparse Embedding
import sys
import argparse
import numpy as np
import spams

def lasso_nn(Y,D):
	# lambda1 controls sparsity, numThreads=-1 if you want to use all cores
	params = {'lambda1' : 0.007,'numThreads' : -1 , 'mode' : spams.PENALTY,'pos':True}
	alpha=spams.lasso(np.asfortranarray(Y,dtype=np.float32),D=np.asfortranarray(D,dtype=np.float32),**params)
	return alpha.todense()


def spamsTrainDL(Y,size):
	param = { 'K' : size, 'lambda1' : 0.007,'iter' : 4000,'posAlpha' : True}
	D = spams.trainDL(np.asfortranarray(Y,dtype=np.float32),**param)
	return D

def main():
	Y=None
	D=None
	doc_id = []

	k=None # dimension of vectors
	d=None # initial dimension of embeddings

	#parsing arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("-f",nargs=1,help="vector file",dest="vector_filepath",required=True)
	parser.add_argument("-d",nargs=1,help="Dictionary size",type=int,dest="K",required=True)
	parser.add_argument("-l",nargs=1,help="regularizer constant (default 0.007)",type=float,dest="lambda",required=False)

	p_args=parser.parse_args()
	args=vars(p_args)

	dict_size=args["K"][0]
	vector_filepath=args["vector_filepath"][0]
	regul_constant=0.007 if args["lambda"]==None else args["lambda"][0]


	''' Reading vector file '''
	dataY=[]
	vector_file=open(vector_filepath,'r+')
	for line in vector_file:
		t=line.strip().split()
		doc_id.append(t[0].lower())
		dataY.append([float(e) for e in t[1:]])

	d=len(dataY[0])
	Y=np.matrix(dataY).getT()
	print "Training dictionary for nnsc ..."
	D =spamsTrainDL(Y,dict_size)
	print "Running non-negative lasso on trainded dictionary ..."
	X =lasso_nn(Y,D)
	print "final approximation error : ",np.linalg.norm(Y-D*X)
	print "Dumping results ..."
	print "size of D : ",D.shape
	print "size of X : ",X.shape
	# dumping dictionary and embeddings
	embed_file=open("out_nnsc_embed.txt","w")
	dict_file=open("out_nnsc_dic.txt","w")
	for i in range(X.shape[1]):
		embed_file.write(doc_id[i]+ " " + " ".join([str(ele[0,0]) for ele in  X[:,i]]) + "\n" )
	for i in range(D.shape[1]):
		dict_file.write(str(i)+ " " + " ".join([str(ele) for ele in  D[:,i]]) + "\n" )

	embed_file.close()
if __name__=="__main__":
	main()
