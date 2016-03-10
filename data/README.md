Data
====


This file describes details about the dataset used in the following paper
	
	Discovering Response-Eliciting Factors in Social Question Answering
	Danish, Yogesh Dahiya and Partha Talukdar
	Proceedings of ICWSM 2016


### Where is the data located?
- the data can be found at 

### How to make sense of the data?
- the paper analysed different AMA threads across four different domains : actors, directors, authors, politicians.
- at the data location you would find four corresponding folders - authors, actors, politics and directors
- each such folder contains 50 data files, each one corresponding to one of the 50 most popular celebrities in each domain


### I see a file by the name of t3_1p32dl, how to interpret this and other such files?
- ```t3_ip32dl``` is a unique identifier (aka link_id) of the full AMA by one particular celebrity. 
- for any such id, one can easily review the whole thread by just by excluding the ```t3_``` part and using ```1p32dl``` like https://www.reddit.com/r/IAmA/comments/1p32dl


### What is contained in each such file?
- each such file contains all the top-level questions (one in each line) asked to the celebrity
- each question (one in each line) is stored in the json format


### What are the details about each question that are available?
- there is a lot of information about each question that is available, the following keys are in particular important
	- ```author``` : author of the comment
	- ```parent_id``` : id of the parent comment. If it is a top-level comment, the parent_id will be the original post by the original poster (OP)
	- ```body```, ```created_utc```, ```link_id``` represnet the body, the time of creation and the unique identifier
	- ```retrieved_on``` : denotes the time of retrieval, updates and deletions after the time are not accomodated. 


### What if I have more questions?
- feel free to reach out to Danish (danish037@gmail.com).
