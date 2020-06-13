#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def my_choice():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        choice = input().lower()
         
        if choice in 'encrypt e decrypt d'.split():
            return choice
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d"')

