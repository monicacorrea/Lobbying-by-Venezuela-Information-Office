#!/usr/bin/env python
# coding: utf-8

# In[240]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("LobbystsRepresentingVenezuelaUS.csv")

df.sort_values(by='TotalAmount', ascending=True)



TotalAmountData   = df ['TotalAmount'].tolist() #Y Axis



plt.plot(yearList, TotalAmountData,   label = 'Amount Spent US$',  marker='o', linewidth=3)

plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Amount Spent (US$)', fontsize=12, fontweight='bold')


plt.legend(["Amount Spent (US$)"],
           bbox_to_anchor = (1.05, 0.6))

plt.xticks(yearList)
plt.yticks(TotalAmountData)
plt.suptitle("Lobbyist representing \n Venezuela Information Office\n", fontsize=18, y=1.08, fontweight='bold', 
             color='blue' )
plt.title('Hired Firm: Segundo Mercado-Llorens', loc='center', fontsize=13, color='black')


plt.style.use('fivethirtyeight')


plt.show()


# In[ ]:





# In[ ]:




