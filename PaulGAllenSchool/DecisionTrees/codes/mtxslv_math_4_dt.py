# -*- coding: utf-8 -*-
"""mtxslv_math_4_DT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vBUNbM0XRMnczO_RWWySbiqmqlpTi1N5
"""

from scipy.stats import entropy
import numpy as np

def best_classifier_attribute(features, labels, copy_of_attr_2_test):
  """
    Given the set <features,labels>, return the best classifier attribute.
    This is done using the conditional entropy. Remember the attribute to 
    be chosen is that one which minimizes conditional entropy.

    I'll loosily base myself in hw1.pdf formulas in order to write down this code

    features and labels must be numpy array, copy_of_attr_2_test must be a list

    return the position (0-based) of minimal conditional entropy. If repeated, return the first
  """

  if( np.shape(features)[1] != len(copy_of_attr_2_test) ):
    raise Exception("Features' Attributes do not match Attributes vector given")
  
  # The list below is the same thing for Ĥ(D|A)
  entropy_dataset_given_attributes = []

  for i in range(np.shape(features)[1]):
    # for each attribute
    if(copy_of_attr_2_test[i]):
      # just compute next things if the attribute is testable (copy_of_attr_2_test[i] is True)
      #print("for attribute", i)
      all_possible_attribute_values = list(set(features[:,i]))    # what values attribute features[:,i] can have?
      #print(ai) remove later
      probability_A_equals_ai = [] # in this list I'll compute the probability attribute A can have value ai
      #print(np.shape(features[:,i])) remove later

      #print(probability_A_equals_ai) #remove later
      entropy_A_equals_ai = []
      
      for j in all_possible_attribute_values: 
        # the line below is the same thing as p_hat. p_hat(A==a_i|D) := |D[A==a_i]| / |D|
        probability_A_equals_ai.append(features[:,i].tolist().count(j)/np.shape(features[:,i])[0]) 
        # the line above computes the probability attribute features[:,i] can assume any of all_possible_attribute_values

        dataset_A_equals_ai = [] # dataset_A_equals_ai := { (x,l) existent in dataset | x[A] == a_i}
        for k in range(np.shape(features)[0]): # for each element of features[:,i]
          if(features[k,i] == j): # if a certain element in this column equals j 
            dataset_A_equals_ai.append(labels[k].tolist()) # then the label of that example should be appended in dataset_A_equals_ai
        
        #in the line below, turn dataset_A_equals_ai into a numpy array, then pass it to mtxslv_entropy() 
        entropy_A_equals_ai.append( mtxslv_entropy(np.array(dataset_A_equals_ai)) )
        # notice if A can be [1,2,3,4], entropy_A_equals_ai = [H(D[A==1]),H(D[A==2]),H(D[A==3]),H(D[A==4])]
        
      #  print("The attribute is equalling ",j) # remove later
      #  print("The label is")    # remove later
      #  print(dataset_A_equals_ai)# remove later
      #print(entropy_A_equals_ai)    # remove later
      #print(probability_A_equals_ai) # remove later

      entropy_dataset_given_attributes.append( np.dot(entropy_A_equals_ai,probability_A_equals_ai) )
    else:
      # if attribute is not testable, let's impute infinity conditional entropy, so the algorithm will never chose this one
      entropy_dataset_given_attributes.append( float('inf') )

  #print(entropy_dataset_given_attributes)  
    
  return np.argmin(entropy_dataset_given_attributes)

def mtxslv_entropy(labels,bas = 2):
  """
  Given <labels>, return the entropy of labels.
  I still don't know if we should keep features as a parameter
  """
  existent_classes = list(set(labels[:,0]))
  probability = []
  # calculate the statistics of each class (probability of each one)
  for i in existent_classes:
    probability.append(labels.tolist().count(i)/np.shape(labels[:,0])[0])
  
  return entropy(probability, base= bas)

def most_common_class(labels):
  """
    Given the set <features,labels>, return the most probable class (label).
    This is done using the statistic of each class, and returning the class 
    with high statistic.
  """
  existent_classes = list(set(labels[:,0]))
  probability = []
  # calculate the statistics of each class (probability of each one)
  for i in existent_classes:
    probability.append(labels.tolist().count(i)/np.shape(labels[:,0])[0])
  #turn probability list to numpy array so we can use np.argmax
  np_prob = np.array(probability)
  where_is_max_prob = np.argmax(np_prob)  
  return existent_classes[where_is_max_prob]

def mtxslv_get_subset(features,labels,attribute,attribute_value):
  """
    Given <features,labels>, attribute (the column of features, 0 based)
    and the value for this attribute (attribute_value), return the subset 
    where the attribute has attribute_value 
  """
  subset_features = []
  subset_labels = []
  if(not(attribute_value in set(features[:,attribute]))):
    raise Exception("Attribute Value does not exist in Assigned Attribute")
  else:
    for it in range(np.shape(features)[0]):
      if(features[it,attribute] == attribute_value):
        subset_features.append(features[it,:].tolist())
        subset_labels.append(labels[it,:].tolist())
  return np.array(subset_features),np.array(subset_labels)
