#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 16:04:09 2020

@author: gabygerlach
"""


import numpy as np
import pandas as pd
#import sklearn
import matplotlib.pyplot as plt
import seaborn as sns 

### CODE from you tube videos 
diamonds = pd.read_csv('data/diamonds.csv.gz')

y=diamonds.pop('price')

d1 =diamonds.select_dtypes(include='number')
d2 = diamonds.select_dtypes(exclude = 'number')

from sklearn.preprocessing import scale

bl = pd.DataFrame(scale(d1))
bl.columns = d1.columns

d1=bl

d2 = pd.get_dummies(d2)

pd.crosstab(diamonds['cut'], d2['cut_Good'])

X = pd.concat([d1, d2], axis =1)

ind = list(X.index)
rng = np.random.RandomState(25)
rng.shuffle(ind)
X_train, y_train= X.loc[ind[:40000]], y[ind[:40000]]
X_test, y_test = X.loc[ind[40000:]], y[ind[40000:]]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

lm=LinearRegression()
dt = DecisionTreeRegressor()
rf = RandomForestRegressor()

lm.fit(X_train, y_train)
dt.fit(X_train, y_train)
rf.fit(X_train, y_train)

from sklearn.metrics import mean_squared_error, r2_score

r2_score(y_train, lm.predict(X_train))
r2_score(y_train, dt.predict(X_train))
r2_score(y_train, rf.predict(X_train))

np.sqrt(mean_squared_error(y_train, lm.predict(X_train)))
np.sqrt(mean_squared_error(y_train, dt.predict(X_train)))
np.sqrt(mean_squared_error(y_train, rf.predict(X_train)))

perf = pd.DataFrame({"orig": y_train,
                     'lm': lm.predict(X_train),
                     'dt': dt.predict(X_train),
                     'rf': rf.predict(X_train)})

sns.relplot(data =pd.melt(perf, id_vars='orig'),
            x= 'orig', y= 'value', hue= 'variable', alpha = 0.3)

sns.relplot(data = perf, x = 'orig', y = 'dt')
sns.relplot(data = perf, x = 'orig', y = 'rf')


from sklearn.model_selection import cross_val_score

cv_score1 = cross_val_score(lm, X_train, y_train, cv=5)
cv_score2 = cross_val_score(dt, X_train, y_train, cv=5)
cv_score3 = cross_val_score(rf, X_train, y_train, cv=5)

np.mean(cv_score1)
np.mean(cv_score2)
np.mean(cv_score3)

r2_score(y_test, lm.predict(X_test))
r2_score(y_test, dt.predict(X_test))
r2_score(y_test, rf.predict(X_test))


from sklearn.model_selection import GridSearchCV

## Assignments 


#data munging 

fmri = sns.load_dataset('fmri')
fmri_no_subject = fmri.drop('subject', axis =1)

categoricals = fmri_no_subject.select_dtypes(exclude = 'number')
dummies = pd.get_dummies(categoricals)
numbers = fmri_no_subject.select_dtypes(include='number')
y=fmri_no_subject.pop('signal')
X = pd.concat([numbers, dummies], axis =1)


### data spliting

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

## fit the model

dt = DecisionTreeRegressor()
rf = RandomForestRegressor()

dt.fit(X_train, y_train)
rf.fit(X_train, y_train)

## model performance


r2_score(y_train, dt.predict(X_train))
r2_score(y_train, rf.predict(X_train))


np.sqrt(mean_squared_error(y_train, dt.predict(X_train)))
np.sqrt(mean_squared_error(y_train, rf.predict(X_train)))

##cross validation

cv_score2 = cross_val_score(dt, X_train, y_train, cv=5)
cv_score3 = cross_val_score(rf, X_train, y_train, cv=5)

r2_score(y_test, dt.predict(X_test))
r2_score(y_test, rf.predict(X_test))


perf = pd.DataFrame({"orig": y_train,
                     'dt': dt.predict(X_train),
                     'rf': rf.predict(X_train)})

sns.relplot(data =pd.melt(perf, id_vars='orig'),
            x= 'orig', y= 'value', hue= 'variable', alpha = 0.3)

