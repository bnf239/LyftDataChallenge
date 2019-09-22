#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


from matplotlib import pyplot as plt


# In[3]:


plt.rcParams['figure.figsize']=(20,11)
plt.rcParams['figure.dpi']=300


# In[4]:


from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets


# In[5]:


overall_analysis = pd.read_csv('overall_info.csv')


# In[6]:


overall_analysis


# In[7]:


output_data = pd.read_csv('output.csv')


# In[8]:


output_data


# In[9]:


plt.plot(output_data.AVERAGE_DISTANCE,'ro',color="red",label="Average Distance Per Driver")
benchmark = overall_analysis.Average_Distance
plt.plot([0., 900], [benchmark, benchmark], "k-",color="blue",linewidth=5.0,label='Average Distance')
plt.title("Average Distance (In Miles) Per Driver", fontsize=20)
plt.xlabel('Drivers')
plt.ylabel('Distance (Miles)')
leg = plt.legend()
plt.savefig("AverageDistance.png")
plt.show()


# In[10]:


plt.plot(output_data.AVERAGE_DURATION,'ro',label="Average Duration Working Per Driver")
benchmark = overall_analysis.Average_Duration_Working
plt.plot( [0,900],[benchmark, benchmark], "k-",color="blue",linewidth=5.0,label='Average Duration Working')
plt.title("Average Time Working (In Minutes) Per Driver", fontsize=20)
plt.xlabel('Drivers')
plt.ylabel('Duration (Minutes)')
leg = plt.legend()
plt.savefig("Average Duration Working.png")
plt.show()


# In[11]:


plt.plot(output_data.AVERAGE_PRIMETIME,'ro',label = 'Average PrimeTime Per Driver')
benchmark = overall_analysis.Average_Primetime
plt.plot( [0,900],[benchmark, benchmark], "k-",color="blue",linewidth=5.0,label='Average PrimeTime')
plt.title("Average PrimeTime Per Driver", fontsize=20)
plt.xlabel('Drivers')
plt.ylabel('PrimeTime (%)')
leg = plt.legend()
plt.savefig("Average PrimeTime.png")
plt.show()


# In[12]:


plt.plot(output_data.NUM_CUSTOMERS,'ro',label = "Number of Customers Per Driver")
benchmark = overall_analysis.Average_Num_Customers
plt.plot( [0,900],[benchmark, benchmark], "k-",color="blue",linewidth=5.0,label='Average Number of Customers')
plt.title("Number of Customers Per Driver", fontsize=20)
plt.xlabel('Drivers')
plt.ylabel('Customers')
leg = plt.legend()
plt.savefig("Number of Customers.png")
plt.show()


# In[15]:


plt.plot(output_data.TOTAL_REVENUE,'ro',label = "Total Revenue Per Driver")
benchmark = overall_analysis.Average_Revenue
benchmark2 = overall_analysis.Driver_Average_LifeTime_Value
plt.plot( [0,900],[benchmark, benchmark], "k--",color="blue",linewidth=2.0,label='Average Total Revenue') 
plt.plot( [0,900],[benchmark2, benchmark2], "k--",color="green",linewidth=2.0,label='Driver Average Lifetime Value') 
plt.title("Total Revenue Per Driver", fontsize=20)
plt.xlabel('Drivers')
plt.ylabel('Revenue ($)')
leg = plt.legend()
plt.savefig("Revenue.png")
plt.show()


# In[16]:


plt.plot(output_data.REVENUE_PER_DAY,'ro',label = "Revenue Per Day Per Driver")
benchmark = overall_analysis.Average_Revenue_Per_Day
plt.plot( [0,900],[benchmark, benchmark], "k-",color="blue", linewidth=5.0,label='Average Revenue Per Day')
plt.title("Revenue Per Day  Per Driver", fontsize=20)
plt.xlabel('Drivers')
plt.ylabel('Revenue ($)')
leg = plt.legend()
plt.savefig("Revenue Per Day Per Driver.png")
plt.show()


# In[17]:


plt.plot(output_data.TIME_AT_COMPANY_IN_DAYS,'ro',label = "Duration at Lyft Per Driver")
benchmark = overall_analysis.Average_Time_At_Lyft
plt.plot( [0,900],[benchmark, benchmark], "k-",color="blue",linewidth=5.0,label='Average Duration at Lyft')
plt.title("Duration At Lyft (In Days) Per Driver", fontsize=20)
plt.xlabel('Drivers')
plt.ylabel('Duration at Company (Days)')
leg = plt.legend()
plt.savefig("Duration at Company.png")
plt.show()


# In[18]:


print("Data Visualization by Begum Ferdous & Lisa Ye")


# In[ ]:




