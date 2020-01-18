#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Footballer():
    def __init__(self,country,goals_under_20):
        self.country = country
        self.goals_under_20 = goals_under_20
    def goals(self):
        self.goals_under_20 = (self.goals_under_20 * 35)
        
Pele = Footballer('Brazil',20)


# In[2]:


print(Pele.__dict__)


# In[3]:


Pele.goals()


# In[4]:


print(Pele.goals_under_20)


# In[ ]:




