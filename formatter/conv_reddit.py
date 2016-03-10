# python conv_reddit.py stopword_file reddit_pickle_files
# converting reddit pickle files to input files required for further processing
# files created : 
# vocab1.txt : question vocab
# vocab2.txt : word vocab
# input_sc.txt : question word count data; (q_id word_id count)
# aux_data : question aux data; (link_Id name reply)

import operator
import sys
import pickle
import re
from sets import Set
from collections import Counter
from wordnet_modules import *
import multiprocessing
from joblib import Parallel, delayed

stopwords=Set()
vocab=Set()
vocab_map={}

# expanding question vocab by adding disambiguated synonyms
def processQuestion(q):
	output_dict={}
	q_proccessed=re.sub(r'[^a-zA-Z0-9 ]',r'',q.lower())
	l=Counter(q_proccessed.strip().split())
	for word,count in l.iteritems():
		if(word in stopwords):
			continue
		output_dict[vocab_map[word]]=count

	# Finding wsd sysnset for words in sentence and adding their lemmas
	for word,lemma in get_disambiguated_synonym(q_proccessed):
		if(lemma in vocab):
			output_dict[vocab_map[lemma]]=l[word]
	
	print "Done"
	return output_dict

def main():
	global stopwords,vocab,vocab_map
	slist=open(sys.argv[1],"r")
	for line in slist:
		stopwords.add(line.strip().lower())
	print "Number of stopwords : ",len(stopwords)
	questions=[]
	questions_aux_data=[]
	for i in range(2,len(sys.argv)):
		obj=pickle.load( open( sys.argv[i], "rb" ) )
		for j in range(len(obj)):
			questions_aux_data.append( obj[j]["link_id"] + " " + obj[j]["name"] + " " + str(1 if obj[j]['reply'] != 'None' else 0 ) )
			questions.append(obj[j]['body'].replace("\n"," "))
			vocab|=Set(re.sub(r'[^a-zA-Z0-9 ]',r'',obj[j]['body'].replace("\n"," ").lower()).strip().split())
	print "vocab size : ",len(vocab)
	vocab=vocab.difference(stopwords)
	print "vocab size after removing stopwords : ",len(vocab)
	print "Number of questions : ",len(questions)
	vocab_list=list(vocab)

	counter=0
	for word in vocab_list:
		vocab_map[word]=counter
		counter+=1

	output_dict={}

	num_cores = multiprocessing.cpu_count()
	outupt_q_map = Parallel(n_jobs=num_cores, verbose=2)(delayed(processQuestion)(q) for q in questions)
	q_count=0
	for q_map in outupt_q_map:
		output_dict[q_count]=q_map
		q_count+=1


	v1=open("vocab1.txt","w") # question vocab
	v2=open("vocab2.txt","w") # word vocab
	v3=open("aux_data.txt","w") # question aux data
	output_file=open("input_sc.txt","w") # question word count data
	for word in vocab_list:
		v2.write(word+"\n")
	for q in questions:
		v1.write(q.encode("UTF-8")+"\n")
	for aux_info in questions_aux_data:
		v3.write(aux_info+"\n")
	for key,value in output_dict.iteritems():
		for word,count in value.iteritems():
			output_file.write(str(key)+" "+str(word)+" "+str(count)+"\n")

	v1.close()
	v2.close()
	v3.close()
	output_file.close()				

if __name__=="__main__":
	main()			
