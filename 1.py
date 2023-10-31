#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
print(stopwords.words('english'))


# In[2]:


document = """This is a sample sentence, showing off the stop words filtration."""


# In[3]:


words = word_tokenize(document)
print(words)


# In[4]:


stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]
print(filtered_words)


# In[5]:


stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]
print(stemmed_words)


# In[6]:


preprocessed_text = ' '.join(stemmed_words)
print("Original Text:",document)
print("\nPreprocessed Text:",preprocessed_text)

