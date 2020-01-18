#!/usr/bin/env python
# coding: utf-8

# In[12]:


class Footballer():
    def __init__(self, decade, country):
        self.decade = decade
        self.country = country
        
class Legends(Footballer):
    def __init__(self, decade, country, goals):
        super().__init__(decade, country)
        self.goals = goals
            
Ronaldo = Legends("10s","portugal",750)
Messi = Footballer("10s","argentina")

print(Ronaldo.goals)


# In[ ]:





# In[ ]:




