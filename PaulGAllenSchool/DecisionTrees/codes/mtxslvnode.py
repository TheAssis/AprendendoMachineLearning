# -*- coding: utf-8 -*-
"""MtxslvNode.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rdnK8dgSLafFyyg_M8PqkY3CoXu8AABV
"""

class MtxslvNode:
  """
  Attributes:
    attribute_to_test: Remember, the sample is ordered (list-like, 0 based). One
                       attribute happens after another.
                       So, if we want to test the first attribute, the variable
                       attribute_to_test should equal 0. 
    attribute_value: the attribute tested by the node should equal one of atribute_value,
                     so we keep iterating in the tree. List-like attribute                  
    child_pointers: the pointers for the children will depend on the dataset
                    attributes values. It will work list-like.   
    is_leaf: if the current node represents a leaf (i.e., it should return a 
             value for class prediction), True. If not, False.
    label: if the current node represents a leaf (it should predicts
           something), this is the class prediction. None, otherwise.             

  Methods:
    __init__(self): void constructor (do not set any class attribute).
    add_branch(self, attr_value, child_no): add branch to this node so that, if 
                                            some value matches attr_value, the 
                                            next node must be child_no
    turn_node_to_leaf(self, attr_2_test, attr_value, class_label):save what attribute must be tested
                                                                  (attr_2_test), what it should match (attr_value)
                                                                  and what should be returned (class_label)                                            
  """   

  def __init__(self):
     self.attribute_to_test = None
     self.attribute_value = []
     self.child_node = []
     self.is_leaf = False
     self.label = None
  
  def add_branch(self, attr_2_test, attr_value, child_no):
    if(attr_value == None):
      raise Exception('Attribute value cannot be None')
    elif(child_no == None):
      raise Exception('Child node cannot be None')
    else:  
      self.attribute_to_test = attr_2_test      
      self.attribute_value.append(attr_value)
      self.child_node.append(child_no)
      self.is_leaf = False
      self.label = None


  def turn_node_to_leaf(self, attr_2_test, attr_value, class_label):
    if(class_label == None):
      raise Exception('Class label cannot be None')
    elif(attr_value == None):
      raise Exception('Attribute value for testing cannot be None')
    elif(attr_2_test == None):
      raise Exception('No attribute to test')  
    else:
      self.is_leaf = True
      self.label = class_label
      self.attribute_value = [attr_value]
      self.attribute_to_test = attr_2_test