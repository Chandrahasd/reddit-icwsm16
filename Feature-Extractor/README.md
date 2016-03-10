Feature Extractor
=================


It throws some light on the computation of different features that were tested for correlation with response rate


### Temporal Features
- ```temporal_features.py``` : it requires comment, its index from the start along with the start time, end time and the length of the IamA.


### Redundancy Features
- ```redundancy_features.py``` : Since for redundancy, we need to check with all the questions posted before a given question. It requires a list of questions posted before a given question along with a given question
- Also note that to better estimate the similarities, it utilizes glove vectors, a precomputed version of 20 nearest neighbours of every word can be found in data/util


### Syntax Features 
- ```syntax_features.py``` : the syntactic complexity of questions is captured by a bunch of syntax features
- it requires dependency tree of the questions, for which we use the Stanford CoreNLP package. A python wrapper can be found here : https://github.com/dasmith/stanford-corenlp-python
- We have pre-computed the parse trees of each comment and we use it directly, the dump can be found in a zipped file in ../data/


### Politeness Features
- ```politeness_score.py``` : the idea of computing the politeness is borrowed from the following paper
	

	A computational approach to politeness with application to social factors.  	
	Cristian Danescu-Niculescu-Mizil, Moritz Sudhof, Dan Jurafsky, Jure Leskovec, Christopher Potts.  
	Proceedings of ACL, 2013.
