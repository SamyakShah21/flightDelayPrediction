# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:54:40 2020

@author: Samyak
"""

import pandas as pd
import math
import numpy as np
from matplotlib import pyplot as plt
def autolabel(rects, xpos='center'):
    
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')
raw_data=pd.read_csv("FlightDelays.csv")
raw_data=np.array(raw_data)
raw_data_JFK=raw_data[raw_data[:,3]=='JFK'];
raw_data_JFK_delayed=raw_data_JFK[raw_data_JFK[:,12]=='delayed']
raw_data_LGA=raw_data[raw_data[:,3]=='LGA'];
raw_data_LGA_delayed=raw_data_LGA[raw_data_LGA[:,12]=='delayed']
raw_data_EWR=raw_data[raw_data[:,3]=='EWR'];
raw_data_EWR_delayed=raw_data_EWR[raw_data_EWR[:,12]=='delayed']
y_all=np.array([np.shape(raw_data_JFK)[0],np.shape(raw_data_LGA)[0],np.shape(raw_data_EWR)[0]])
y_delayed=np.array([np.shape(raw_data_JFK_delayed)[0],np.shape(raw_data_LGA_delayed)[0],np.shape(raw_data_EWR_delayed)[0]])

#%% Bar graph single and double
width=0.4
fig, ax = plt.subplots()
rects1 = ax.bar(np.arange(3) - width/2, y_all, width,
                label='All flights')
rects2 = ax.bar(np.arange(3) + width/2, y_delayed, width,
                label='Delayed flights')
ax.set_ylabel('No. of Flights')
ax.set_title('Airport of Origin')
ax.set_xticks(np.arange(3))
ax.set_xticklabels(('JFK','LGA','EWR'))
ax.legend(loc="best")
plt.grid()

autolabel(rects1, "left")
autolabel(rects2, "right")
fig.tight_layout()

plt.show()
for i in range(3):
    print('Fraction of flights from {} delayed is {:.03f}'.format(np.array(['JFK','LGA','EWR'])[i],y_delayed[i]/y_all[i]));
raw_data_DCA=raw_data[raw_data[:,7]=='DCA'];
raw_data_DCA_delayed=raw_data_DCA[raw_data_DCA[:,12]=='delayed']
raw_data_IAD=raw_data[raw_data[:,7]=='IAD'];
raw_data_IAD_delayed=raw_data_IAD[raw_data_IAD[:,12]=='delayed']
raw_data_BWI=raw_data[raw_data[:,7]=='BWI'];
raw_data_BWI_delayed=raw_data_BWI[raw_data_BWI[:,12]=='delayed']
y_all=np.array([np.shape(raw_data_DCA)[0],np.shape(raw_data_IAD)[0],np.shape(raw_data_BWI)[0]])
y_delayed=np.array([np.shape(raw_data_DCA_delayed)[0],np.shape(raw_data_IAD_delayed)[0],np.shape(raw_data_BWI_delayed)[0]])

fig, ax = plt.subplots()
rects1 = ax.bar(np.arange(3) - width/2, y_all, width,
                label='All flights')
rects2 = ax.bar(np.arange(3) + width/2, y_delayed, width,
                label='Delayed flights')
ax.set_ylabel('No. of Flights')
ax.set_title('Airport of Destination')
ax.set_xticks(np.arange(3))
ax.set_xticklabels(('DCA','IAD','BWI'))
ax.legend(loc="best")
plt.grid()


autolabel(rects1, "left")
autolabel(rects2, "right")
fig.tight_layout()
plt.show()
for i in range(3):
    print('Fraction of flights to {} delayed is {:.03f}'.format(np.array(['DCA','IAD','BWI'])[i],y_delayed[i]/y_all[i]));
    
delay=np.zeros(7)
all_flights=np.zeros(7)
for i in range(7):
    all_flights[i]=np.shape(raw_data[raw_data[:,9]==(i+1)])[0]
    delay[i]=np.shape(raw_data[(raw_data[:,9]==(i+1))&(raw_data[:,12]=='delayed')])[0]
fig, ax = plt.subplots()
rects1 = ax.bar(np.arange(7) - width/2, all_flights, width,
                label='All flights')
rects2 = ax.bar(np.arange(7) + width/2, delay, width,
                label='Delayed flights')
ax.set_ylabel('No. of Flights')
ax.set_title('Days of the Week')
ax.set_xticks(np.arange(7))
ax.set_xticklabels(('Mon','Tue','Wed','Thu','Fri','Sat','Sun'))
ax.legend(loc="best")
plt.grid()


autolabel(rects1, "left")
autolabel(rects2, "right")
fig.tight_layout()
plt.show()
for i in range(7):
    print('Fraction of flights on {} delayed is {:.03f}'
          .format(np.array(['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])[i],delay[i]/all_flights[i]));
         

all_hour=np.zeros(16)
delay=np.zeros(16)
for i in range(2201):
    all_hour[math.floor(raw_data[i,0]/100)-6]=all_hour[math.floor(raw_data[i,0]/100)-6]+1
    if raw_data[i,12]=='delayed':
        delay[math.floor(raw_data[i,0]/100)-6]=delay[math.floor(raw_data[i,0]/100)-6]+1
fig, ax = plt.subplots()
rects1 = ax.bar(np.arange(16), all_hour, width,
                label='All Flights')

ax.set_ylabel('All flights')
ax.set_title('Departure time in hrs')
ax.set_xticks(np.arange(16))
ax.set_xticklabels(np.arange(16)+6)
plt.grid()


autolabel(rects1, "left")
fig.tight_layout()
plt.show()


fig, ax = plt.subplots()
rects1 = ax.bar(np.arange(16), delay, width,
                label='Delayed Flights')

ax.set_ylabel('No. of delayed flights')
ax.set_title('Departure time in hrs')
ax.set_xticks(np.arange(16))
ax.set_xticklabels(np.arange(16)+6)
plt.grid()
autolabel(rects1, "left")
fig.tight_layout()
plt.show()

for i in range(16):
    print('Fraction of flights between {}00 hrs and {}00 hrs delayed is {:.03f}'
          .format(i+6,i+7,delay[i]/all_hour[i]));
plt.plot(raw_data[:,10], raw_data[:,9], 'ro')
plt.plot(raw_data[:,10], raw_data[:,9], 'b-')
plt.xlabel("Date of the month January")
plt.ylabel("Day code- Mon=1.... Sun=7")
plt.show()


#%% HEAT MAP
raw_data_DCA_JFK=raw_data_DCA[raw_data_DCA[:,3]=='JFK'];
raw_data_DCA_delayed_JFK=raw_data_DCA_JFK[raw_data_DCA_JFK[:,12]=='delayed']
raw_data_DCA_LGA=raw_data_DCA[raw_data_DCA[:,3]=='LGA'];
raw_data_DCA_delayed_LGA=raw_data_DCA_LGA[raw_data_DCA_LGA[:,12]=='delayed']
raw_data_DCA_EWR=raw_data_DCA[raw_data_DCA[:,3]=='EWR'];
raw_data_DCA_delayed_EWR=raw_data_DCA_EWR[raw_data_DCA_EWR[:,12]=='delayed']

raw_data_IAD_JFK=raw_data_IAD[raw_data_IAD[:,3]=='JFK'];
raw_data_IAD_delayed_JFK=raw_data_IAD_JFK[raw_data_IAD_JFK[:,12]=='delayed']
raw_data_IAD_LGA=raw_data_IAD[raw_data_IAD[:,3]=='LGA'];
raw_data_IAD_delayed_LGA=raw_data_IAD_LGA[raw_data_IAD_LGA[:,12]=='delayed']
raw_data_IAD_EWR=raw_data_IAD[raw_data_IAD[:,3]=='EWR'];
raw_data_IAD_delayed_EWR=raw_data_IAD_EWR[raw_data_IAD_EWR[:,12]=='delayed']

raw_data_BWI_JFK=raw_data_BWI[raw_data_BWI[:,3]=='JFK'];
raw_data_BWI_delayed_JFK=raw_data_BWI_JFK[raw_data_BWI_JFK[:,12]=='delayed']
raw_data_BWI_LGA=raw_data_BWI[raw_data_BWI[:,3]=='LGA'];
raw_data_BWI_delayed_LGA=raw_data_BWI_LGA[raw_data_BWI_LGA[:,12]=='delayed']
raw_data_BWI_EWR=raw_data_BWI[raw_data_BWI[:,3]=='EWR'];
raw_data_BWI_delayed_EWR=raw_data_BWI_EWR[raw_data_BWI_EWR[:,12]=='delayed']

origin = ['JFK','LGA','EWR']
desti = ['DCA','IAD','BWI']

matrix_para=np.array([[np.shape(raw_data_DCA_delayed_JFK)[0]/np.shape(raw_data_DCA_JFK)[0],
                       np.shape(raw_data_DCA_delayed_LGA)[0]/np.shape(raw_data_DCA_LGA)[0],
                       np.shape(raw_data_DCA_delayed_EWR)[0]/np.shape(raw_data_DCA_EWR)[0]],
                      [np.shape(raw_data_IAD_delayed_JFK)[0]/np.shape(raw_data_IAD_JFK)[0]
                      ,np.shape(raw_data_IAD_delayed_LGA)[0]/np.shape(raw_data_IAD_LGA)[0],
                      np.shape(raw_data_IAD_delayed_EWR)[0]/np.shape(raw_data_IAD_EWR)[0]],
                       [np.shape(raw_data_BWI_delayed_JFK)[0]/np.shape(raw_data_BWI_JFK)[0],
                        0,np.shape(raw_data_BWI_delayed_EWR)[0]/np.shape(raw_data_BWI_EWR)[0]]])



fig, ax = plt.subplots()
im = ax.imshow(matrix_para)
plt.colorbar(im)

ax.set_xticks(np.arange(len(origin)))
ax.set_yticks(np.arange(len(desti)))

ax.set_xticklabels(origin)
ax.set_yticklabels(desti)
plt.xlabel("Destination Airport")
plt.ylabel("Origin Airport")
# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")


for i in range(len(origin)):
    for j in range(len(desti)):
        text = ax.text(j, i, round(matrix_para[i, j],3),
                       ha="center", va="center", color="w")

ax.set_title("Fraction of flights delayed")
fig.tight_layout()
plt.show()

origin = ['JFK','LGA','EWR']
desti = ['DCA','IAD','BWI']

matrix_para=np.array([[213,214,199],[228,229,213],[184,185,169]])



fig, ax = plt.subplots()
im = ax.imshow(matrix_para)
plt.colorbar(im)

ax.set_xticks(np.arange(len(origin)))
ax.set_yticks(np.arange(len(desti)))

ax.set_xticklabels(origin)
ax.set_yticklabels(desti)
plt.xlabel("Destination Airport")
plt.ylabel("Origin Airport")
# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")


for i in range(len(origin)):
    for j in range(len(desti)):
        text = ax.text(j, i, round(matrix_para[i, j],3),
                       ha="center", va="center", color="w")

ax.set_title("Distance between the airports (in miles)")
fig.tight_layout()
plt.show()
print("To see how distance between airports relate to delays")

#%% PIE
airline=np.array(['DH','OH','DL','MQ','UA','US','RU','CO',])
raw_data_delayed=raw_data[raw_data[:,12]=='delayed']
delay_airline=np.zeros(8)
airline_each=np.zeros(8)
for i in range(8):
    delay_airline[i]=np.shape(raw_data_delayed[raw_data_delayed[:,1]==airline[i]])[0]
    airline_each[i]=np.shape(raw_data[raw_data[:,1]==airline[i]])[0]
explode = np.zeros(len(airline))

fig1, ax1 = plt.subplots()
ax1.pie(delay_airline, explode=explode, labels=airline, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  
plt.legend()
plt.title("Delayed flights by airline")
plt.show()

fig1, ax1 = plt.subplots()
ax1.pie(airline_each, explode=explode, labels=airline, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  
plt.legend()
plt.title("Flights by airline")
plt.show()

raw_data_weather_1=np.shape(raw_data[raw_data[:,8]==1])[0]
raw_data_weather_0=np.shape(raw_data[raw_data[:,8]==0])[0]
raw_data_weather_1_d=np.shape(raw_data[(raw_data[:,12]=='delayed')&(raw_data[:,8]==1)])[0]
raw_data_weather_0_d=np.shape(raw_data[(raw_data[:,12]=='delayed')&(raw_data[:,8]==0)])[0]

fig1, ax1 = plt.subplots()
ax1.pie(np.array([raw_data_weather_1-raw_data_weather_1_d,raw_data_weather_1_d]), 
        explode=np.zeros(2), labels=np.array(['Undelayed filghts','Delayed flights']), autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  
plt.legend()
plt.title("% delayed flights when weather=1")
plt.show()


fig1, ax1 = plt.subplots()
ax1.pie(np.array([raw_data_weather_0-raw_data_weather_0_d,raw_data_weather_0_d]), 
        explode=np.zeros(2), labels=np.array(['Undelayed filghts','Delayed flights']), autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  
plt.legend()
plt.title("% delayed flights when weather=0")
plt.show()

#%% Box Plot

a=raw_data[:,2]-raw_data[:,0]
for i in range(len(a)-2):
    if a[i]<-1000 or a[i]>1000:
        a=np.delete(a,i)
fig2, ax2 = plt.subplots()
ax2.set_title('Difference between real departure and scheduled departure')

plt.ylabel("Positive is delay, negative is early take-off")
ax2.boxplot(a)
plt.show()