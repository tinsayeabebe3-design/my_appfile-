#!/usr/bin/env python
# coding: utf-8

# In[1]:


txt = input("Enter your sentence: ")
txt = txt.split("_")
new_list = []
for text in txt:
    lower_txt = text.lower()
    new_list.append(lower_txt)
new_sentence = ' '.join(new_list)
print(new_sentence)


# In[ ]:




