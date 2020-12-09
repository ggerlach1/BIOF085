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

##f-strings


dat = pd.DataFrame({'animal':['dog', 'lion','elephant','kangaroo'],
    'country': ['USA','Nigeria','Thailand', 'Australia'],
    'do': ['do','do not', 'do','do not']})

for i in list(dat.index):
    animal = dat.loc[i]['animal']
    country = dat.loc[i]['country']
    do = dat.loc[i]['do']
    print(f"There are lots of {animal} in {country}. We hope you {do} see them in person some day")

## RegEX
import re
txt = "The rain in Spain"
print(re.search("^The.*Spain$", txt) is not None)

