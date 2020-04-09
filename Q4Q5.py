# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 11:49:14 2020

@author: Samyak Shah
"""

import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from matplotlib import pyplot as plt
import numpy as np

raw_data=pd.read_csv("FlightDelays.csv")
raw_data['CRS_DEP_TIME']=np.floor(raw_data['CRS_DEP_TIME']/100)
raw_data['DEP_TIME']=np.floor(raw_data['DEP_TIME']/100)
dummy_DEST=pd.get_dummies(raw_data['DEST'])
dummy_CARRIER=pd.get_dummies(raw_data['CARRIER'])
dummy_ORIGIN=pd.get_dummies(raw_data['ORIGIN'])
dummy_CRS_DEP_TIME=pd.get_dummies(raw_data['CRS_DEP_TIME'])
dummy_DEP_TIME=pd.get_dummies(raw_data['DEP_TIME'])
dummy_DAY=pd.get_dummies(raw_data['DAY_WEEK'])

raw_data=pd.concat([raw_data,dummy_CRS_DEP_TIME,dummy_CARRIER,dummy_DEP_TIME,
                    dummy_DEST,dummy_ORIGIN,dummy_DAY],axis=1)
raw_data=raw_data.drop(['CRS_DEP_TIME','CARRIER','DEP_TIME','DEST',
                        'FL_DATE','FL_NUM','ORIGIN','DAY_WEEK',
                        'DAY_OF_MONTH','TAIL_NUM'],axis=1)
raw_data=np.array(raw_data)
y=raw_data[:,2]
X=np.delete(raw_data,2,axis=1)
ones_array=np.array([np.ones(2201)])
X=np.concatenate((ones_array.T,X),axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=468)

sc_x = StandardScaler()
X_train = sc_x.fit_transform(X_train) 
X_test = sc_x.transform(X_test)

logmodel = LogisticRegression(max_iter=999)
logmodel.fit(X_train,y_train) 
predictions = logmodel.predict(X_test)
accuracy=np.sum([predictions==y_test])*100/881
model = LogisticRegression()
rfe = RFE(model, 1)
fit = rfe.fit(X_train, y_train)
print("Num Features: %s" % (fit.n_features_))
print("Selected Features: %s" % (fit.ranking_))
print(accuracy)


