#!/usr/bin/env python
# coding: utf-8

# In[1]:


documents = {
    1: "The quick brown fox jumped over the lazy dog.",
    2: "The lazy dog slept in the sun.",
}


# In[2]:


import re

def tokenize(text):
    words = re.findall(r'\w+', text.lower())
    return set(words)


tokenized_documents = {doc_id: tokenize(text) for doc_id, text in documents.items()}
tokenized_documents


# In[3]:


inverted_index = {}

for doc_id, words in tokenized_documents.items():
    for word in words:
        if word not in inverted_index:
            inverted_index[word] = [doc_id]
        else:
            inverted_index[word].append(doc_id)

inverted_index


# In[4]:


def retrieve_documents(query):
    query_words = tokenize(query)
    matching_doc_ids = set()

    for word in query_words:
        if word in inverted_index:
            matching_doc_ids.update(inverted_index[word])

    if matching_doc_ids:
        matching_documents = {doc_id: documents[doc_id] for doc_id in matching_doc_ids}
        return matching_documents
    else:
        return None


query = "Sun is very bright Today"
retrieved_docs = retrieve_documents(query)

if retrieved_docs:
    for doc_id, doc_text in retrieved_docs.items():
        print(f"Document {doc_id}: {doc_text}")
else:
    print("No matching documents found.")

