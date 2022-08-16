#!/usr/bin/env python
# coding: utf-8

# In[1]:


#second largest number in an array
mylist = [29,25,38,45,67]
mylist.sort(reverse = True) #using sort function

print(mylist)

print(mylist[1]) #printing the element in the index 1 position


# In[4]:


#second largest number in an array
mylist = [29,25,38,45,67]
mylist.sort(reverse = False) #using sort function

print(mylist)

print(mylist[-2]) #printing the element in the index position -2(from back to front)


# In[5]:


mylist=[29,25,38,45,67]
mylist.remove(max(mylist)) #removing the maximum element
print(mylist)
print(max(mylist))#printing the next maximum element


# In[4]:



a=[1,2,3,7,98,100]

#function declaration --> passing parameter as b
def second_max(b):           
    #to keep track of entire list -->declare first max in the list =>b
    first_max=max(b[0],b[1]) 
    # -->declaring second max in the list => b
    sec_max=min(b[0],b[1])   
            
    #since the first two elements are already in the list, the range varies from position 2 to end of the list(length)
    for i in range(2,len(b)):
        #it check the list value with first max value
        if b[i]>first_max: 
            #reassigning the values when the "if condition" satisfies
            sec_max=first_max   
            first_max=b[i] 
        #it check the list value with second max value
        elif b[i] > sec_max:  
            #checking the "elif condition"
            sec_max=b[i]        
    return sec_max
    
print(second_max(a))


# In[ ]:




