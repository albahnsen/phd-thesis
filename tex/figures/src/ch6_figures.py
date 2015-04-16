__author__ = 'al'



import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model

path = "/home/al/DriveAl/Publications/2015/phd-thesis/tex/figures/"
col_pal = sns.color_palette()

############################################################################
# ch6_fig1 - logit function
############################################################################

# from  http://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic.html
# http://commons.wikimedia.org/wiki/File:Logistic-curve.svg

f, ax1 = plt.subplots(1, 1, figsize=(4, 2.5))
x = np.arange(-6, 6, 0.1)
y = np.exp(x) / (1+np.exp(x))
ax1.plot(x, y)
ax1.set_xlim(-6, 6)
ax1.set_yticks([0, 0.5, 1])
ax1.tick_params(axis='both', which='major', labelsize=8)
plt.savefig(path+'ch6_fig1.eps', format='eps', dpi=1000, bbox_inches='tight')#, pad_inches=0)
plt.show()
