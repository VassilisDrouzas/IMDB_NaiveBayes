# -----------------------------------------NAIVE BAYES------------------------------------------------------------

import numpy as np
import random
import dataProcess

train_data=[]
test_data=[]
vocabulary=[]
array_train=[]
array_test=[]
pos_list=[]
neg_list=[]

n=100                    # Hyperparameter to be tested with different values
m=500                   # Hyperparameter to be tested with different values
maximum_data=12500      # Hyperparameter to be tested with different values

def gatherData(train_data,test_data,vocabulary):

   pos_folder=['data\\train\\pos\\','data\\test\\pos\\' ]
   neg_folder=['data\\train\\neg\\', 'data\\test\\neg\\' ]

  
   dataProcess.load(pos_folder[0],train_data,1,maximum_data)
   dataProcess.load(neg_folder[0],train_data,0,maximum_data)
   dataProcess.load(pos_folder[1],test_data,1,maximum_data)
   dataProcess.load(neg_folder[1],test_data,0,maximum_data)

   
   random.shuffle(train_data)                                     # We need to mix the data
   random.shuffle(test_data)



   vocabulary=dataProcess.getWordsFreqList(train_data)
   vocabulary=vocabulary[n:m]          #Keeps a smaller vocabulary(skipping words before index n (the first n-1), up until index m (m-n most frequent words))

   array_train=dataProcess.construct_0_1_array(train_data,vocabulary)
   array_test=dataProcess.construct_0_1_array(test_data,vocabulary)

   return array_train,array_test 



def calc_posterior_prob(pos_list,neg_list):


   diff=m-n

   for i in range (diff):
  
      total_pos_1=total_neg_1=positives=negatives=index=0                        # Initializing counters
      
      for review in train_data:
         

         if review[1]==1:                                                     #review[1] is the sign
            positives+=1
            if array_train[index][i]==1:                                   # Keep the positive words with 1
               total_pos_1+=1                      
        
         if review[1]==0:
            negatives+=1
            if array_train[index][i]==1:                                   #Keep the negative words with 1
               total_neg_1+=1
        
         index+=1

      positiveif1=total_pos_1/positives
      negativeif1=total_neg_1/negatives

      pos_list.append(positiveif1)
      neg_list.append(negativeif1)



def Bayes(array):

   
   
   pos_prob=[]
   neg_prob=[]
   i=0
   for elem in array:
      if elem==1:
         pos_prob.append(pos_list[i])
         neg_prob.append(neg_list[i])
      elif elem==0:
         pos_prob.append(1-pos_list[i])
         neg_prob.append(1-neg_list[i])
      i+=1

   pos_posibility=0.5
   neg_posibility=0.5
   positive_probability=pos_posibility * np.prod(pos_prob)                       #By-the-slides Bayes formula (the denominator is not needed 
   negative_probability=neg_posibility * np.prod(neg_prob)                       #because it is common for both probabilities.

   if (positive_probability >negative_probability):
      return "positive"
   else:
      return "negative"


def metrics_train(Bayes):

   true_positives=true_negatives=false_positives=false_negatives=index=0           #Initializing counters

   

   for i in array_train:
      if train_data[index][1]== 1 and Bayes(i)=="positive":
         true_positives+=1
         
      if train_data[index][1]==0 and Bayes(i)=="negative":
         true_negatives+=1
        
      if train_data[index][1]==0 and Bayes(i)=="positive":
         false_positives+=1
      if train_data[index][1]==1 and Bayes(i)=="negative":
         false_negatives+=1
      index+=1

   accuracy=(true_positives+true_negatives)/(true_positives+true_negatives+false_positives+false_negatives)
   precision=true_positives/ (true_positives+false_positives)
   recall=true_positives/ (true_positives+false_negatives)
   f1=2* ((precision*recall)/(precision+recall))      

   # These formulas obtained from https://vitalflux.com/accuracy-precision-recall-f1-score-python-example/
   

   return accuracy,precision,recall,f1



def metrics_test(Bayes):

   true_positives=true_negatives=false_positives=false_negatives=index=0           #Initializing counters

   for i in array_test:
      if test_data[index][1]== 1 and Bayes(i)=="positive":
         true_positives+=1
         
      elif test_data[index][1]==0 and Bayes(i)=="negative":
         true_negatives+=1
         
      elif test_data[index][1]==0 and Bayes(i)=="positive":
         
            false_positives+=1
      elif test_data[index][1]==1 and Bayes(i)=="negative":
            false_negatives+=1
      index+=1

   accuracy=(true_positives+true_negatives)/(true_positives+true_negatives+false_positives+false_negatives)
   precision=true_positives/ (true_positives+false_positives)
   recall=true_positives/ (true_positives+false_negatives)
   f1=2* ((precision*recall)/(precision+recall))      

   # These formulas obtained from https://vitalflux.com/accuracy-precision-recall-f1-score-python-example/

   return accuracy,precision,recall,f1

def print_results():

   
   train_results=metrics_train(Bayes)
   accuracy_train=train_results[0]
   precision_train=train_results[1]
   recall_train=train_results[2]
   f1_train=train_results[3]

   print ("---------------TRAIN DATA----------" )
   print("Accuracy : ", accuracy_train)
   print("Precision :",precision_train)
   print("Recall : ",recall_train )
   print("F1 : ", f1_train)

   test_results=metrics_test(Bayes)
   accuracy_test=test_results[0]
   precision_test=test_results[1]
   recall_test=test_results[2]
   f1_test=test_results[3]

   print()

   print ("---------------TEST DATA----------" )
   print("Accuracy : ", accuracy_test)
   print("Precision :",precision_test)
   print("Recall : ",recall_test )
   print("F1 : ", f1_test)
   
array_train,array_test=gatherData(train_data,test_data,vocabulary)
calc_posterior_prob(pos_list,neg_list)
print_results()



























    
  