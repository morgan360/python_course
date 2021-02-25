#!/usr/bin/env python
# coding: utf-8

# This is used as an example of creating and importing modules.

# In[ ]:


# Morgan's library module
print("Imported my module")
test = 'Test String'

def find_index(to_search, target):
    '''Find the index of the value in a sequence. Return the index if found otherwise return o'''
    for i, value in enumerate(to_search):
        if value == target:
            return i #returns the index value
    return -1

