# -*- coding: utf-8 -*-
"""
Benjamin H Pepper
BHPepper@gmail.com
linkedin.com/in/BHPepper
"""

import numpy as np
#import importlib 

import spam_functions
import spam_nested_cv


dat = spam_functions.get_spam_dat()
dat = dat.dropna()

X = dat.drop(57, axis=1)
y = np.array(dat[57])

#importlib.reload(spam_functions)
res_nn = spam_nested_cv.nested_cv(spam_functions.nn_mod, X, y, spam_functions.nn_score, 
                                  spam_functions.nn_outer_perf, cv_k1 = 4, seed = 1)
np.mean(res_nn['Perf'])
