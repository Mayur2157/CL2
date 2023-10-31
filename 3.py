#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pgmpy')


# In[3]:


import numpy as np
import pandas as pd
import csv
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination


# In[5]:


heartDisease = pd.read_csv('heart.csv')
heartDisease = heartDisease.replace('?',np.nan)


# In[6]:


print('Sample instances from the dataset are given below')
print(heartDisease.head())


# In[7]:


print('\n Attributes and datatypes')
print(heartDisease.dtypes)


# In[11]:


model= BayesianModel([('age','target'),('sex','target'),('exang','target'),('cp','target'),('target','restecg'),('target','chol')])
print('\nLearning CPD using Maximum likelihood estimators')
model.fit(heartDisease,estimator=MaximumLikelihoodEstimator)


# In[12]:


print('\n Inferencing with Bayesian Network:')
HeartDiseasetest_infer = VariableElimination(model)
print('\n 1. Probability of HeartDisease given evidence= restecg')
q1=HeartDiseasetest_infer.query(variables=['target'],evidence={'restecg':1})
print(q1)


# In[13]:


print('\n 2. Probability of HeartDisease given evidence= cp ')
q2=HeartDiseasetest_infer.query(variables=['target'],evidence={'cp':2})
print(q2)

