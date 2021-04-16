#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np

DATA = pd.read_csv("question_philoit.csv", usecols = ["id","content"])
DATA.colums = ["label","tweet"]

DATA.head()


# In[8]:


import ast

def convert_text_list(texts):
    texts = ast.literal_eval(texts)
    return [text for text in texts]

DATA["content_list"] = DATA["content"].apply(convert_text_list)


print(DATA["content_list"][90])

print("\ntype : ", type(DATA["content_list"][90]))


# In[ ]:




