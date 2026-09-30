#!/usr/bin/env python
# coding: utf-8

# In[22]:


emp_data={"name":"Archana",
          "Age":"19",
          "Address":"Sangli",
          "mobile":9528454
         }
print(emp_data)


# In[23]:


emp_data["Address"]="Pune"
print(emp_data)


# In[24]:


emp_data.keys()


# In[26]:


emp_data.pop("Age")


# In[27]:


emp_data.values()


# In[28]:


emp_data.get("mobile")


# In[29]:


emp_data["roll no."]=38
print(emp_data)


# In[31]:


d={"Student 1":
  {
      "name":"Archana",
      "Age":"19",
      "Address":"Sangli",
      "roll no.":38
  },
  "Student 2":
  {
      "name":"Riya",
      "Age":"19",
      "Address":"Sangli",
      "roll no.":17
  },
  "Student 3":
  {
      "name":"Shrutika",
      "Age":"18",
      "Address":"Sangli",
      "roll no.":7
  }
  }
print(d)


# In[ ]:




