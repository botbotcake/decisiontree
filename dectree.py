# -*- coding: utf-8 -*-
"""dectree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12RLS8rQq5mc1iob73LWImnwZC57a1X9i
"""

import pandas as pd
import math
from collections import defaultdict
#from google.colab import files
#uploaded = files.upload()

data = pd.read_excel("income.xlsx")
data

cols =list(data.columns)

print("The classes of",data.columns[-1],"are :",data[cols[-1]].unique())

classes = dict(data[cols[-1]].value_counts())
prob = dict()
print("Their Respective Counts Are:\n",classes)
print("Their Respective Probabilities Are:")
for i in classes.copy():
  prob[i] = classes[i]/data.shape[0]
print(prob)

print("Calculating H(D) of the class labels\n")
h_din = 0
for i in classes.copy():
  h_din = h_din+prob[i]*math.log10(1/prob[i])
print("Thus the entropy of the set is: ",h_din)

print("Calculating the Gain for each attribute")

probmain = dict()
hdeach= defaultdict(dict)
gain = dict()
for i in range(len(cols)-1):
  hdeach[cols[i]] = dict()
  for j in range(len(data[cols[i]].unique())):
    probmain[cols[i]] = {}
    probmain[cols[i]] = data[cols[i]].value_counts()/data.shape[0]
    count = 0
    hdeach[cols[i]][data[cols[i]].unique()[j]]=0
    for l in classes.copy():
      for k in range(data.shape[0]):
        if data.at[k,cols[i]]==data[cols[i]].unique()[j] and data.at[k,cols[-1]]==l:
          count+=1
      if count!=0:
        hdeach[cols[i]][data[cols[i]].unique()[j]]+=(count/(data[cols[i]].value_counts()[data[cols[i]].unique()[j]]))*math.log((data[cols[i]].value_counts()[data[cols[i]].unique()[j]])/count)
      else:
        hdeach[cols[i]][data[cols[i]].unique()[j]]+=0
      
print(probmain)
print(hdeach)

gain = dict()
for i in range(len(cols)-1):
  print("Gain For attribute", cols[i])
  gain[cols[i]]=0.0
  for k in hdeach[cols[i]].copy():
      # print("probmain =",j,k,probmain[j][k],"hdeach =",hdeach[j][k] )
    gain[cols[i]]=gain[cols[i]]+probmain[cols[i]][k]*hdeach[cols[i]][k]
  gain[cols[i]]=h_din-gain[cols[i]]
print(gain)

maxim = 0
for j in gain.copy():
  if maxim <= gain[j]:
    maxim = gain[j]
    key = j
print("The splitting attribute is: ",key)

