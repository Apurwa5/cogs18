#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def translated(choice,message): 
    if choice == 'e':
        new_message=''
        alpha = ' abcdefghijklmnopqrstuvwxyz!?,.'
        
        for item in message:
            if item in alpha:
                item_index=alpha.index(item)
                new_letter_index = item_index + 4  
                new_message = new_message + alpha[new_letter_index]
            
            else:
                item=item
    else:
        new_message = ''
        alpha = ' abcdefghijklmnopqrstuvwxyz!?,.'
        
        for item in message:
            if item in alpha:
                item_index=alpha.index(item)
                new_letter_index = item_index - 4    
                new_message = new_message + alpha[new_letter_index]
        else:
            item=item
        
    return new_message

