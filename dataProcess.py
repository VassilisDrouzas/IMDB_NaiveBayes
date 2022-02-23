
import os



def load(directory,list,sign,max):

    
    files=os.listdir(directory)
    max_files=files[1:max]                                                                 # Read only "max" number of data
    for file in max_files:
        
        f=open(directory +file,"r",encoding="utf8")
        all_words=f.read()
        
        list.append((all_words,sign))                               #Append a tuple (words,sign) to the list.This way, we will know if the reviews are actually positive or negative
        f.close()
        
           
    
    
  

def getWordsFreqList(directory):                                                            #returns the list of the frequency of the words

    words_dict={}
    for review in directory:
       
       words=review[0].split()
       for word in words:
           word=word.lower()
           
           if word in words_dict:
               words_dict[word]+=1
           else:
                words_dict[word]=1
       

    freq_list=[]
    for i,j in sorted (words_dict.items(),key=element_1,reverse=True):
       freq_list.append(i)
    
  
    return freq_list                                     #return the frequency list

def element_1(x):
    return x[1]

def construct_0_1_array(data,list):                     #Construct the 0-1 array.
    
    i=0
    final=[[]]

    for text in data:
        words=text[0].split()                                  
        
        
        for word in list:
            if (words.__contains__(word)):
                final[i].append(1)
            else:
                final[i].append(0)
        i+=1
        final.append([])
    final.pop()                #Omit the final character
    return final
    
   





            





