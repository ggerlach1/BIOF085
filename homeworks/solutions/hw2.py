#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 08:35:21 2020

@author: abhijit
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = pd.read_csv('BIOF085/data/tips.csv')

sns.distplot(tips['total_bill'], hist=False)

sns.countplot(tips['day'])
sns.countplot(tips['size'])

sns.jointplot(data=tips, x='tip',y = 'total_bill')

sns.boxplot(data=tips, x='day', y= 'total_bill')

tips['ratio'] = tips['tip']/tips['total_bill']
sns.relplot(data=tips, x = 'ratio', y = 'size')

sns.relplot(data=tips, x = 'tip', y = 'total_bill', hue = 'day')

sns.relplot(data=tips, x = 'tip', y = 'total_bill', hue = 'size')

g = sns.FacetGrid(data=tips, col = 'day')
g.map(sns.barplot, 'tip', 'time')

g = sns.FacetGrid(data=tips, col = 'day', row='time')
g.map(sns.countplot, 'size')


# for python up to 3.7.9
diamonds = pd.read_csv('data/diamonds.csv.gz')
d2 = diamonds.sample(n = 1000, random_state=3)
g = sns.PairGrid(d2, diag_sharey=False)
g.map_lower(sns.kdeplot, colors='C0')
g.map_upper(sns.scatterplot)
g.map_diag(sns.distplot)


# for python 3.8+
diamonds = pd.read_csv('data/diamonds.csv.gz')                                                            
d2 = diamonds.sample(n = 1000, random_state=3)                                                            
g = sns.PairGrid(d2, diag_sharey=False)                                                                   
g.map_lower(sns.kdeplot, colors='C0')                                                                     
g.map_upper(sns.scatterplot)                                                                              
g.map_diag(sns.histplot, kde=True)  # this is the only line that is different                                                                       
plt.show() 