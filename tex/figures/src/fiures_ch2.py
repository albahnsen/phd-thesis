__author__ = 'al'

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets

path = "/home/al/DriveAl/Publications/2015/phd-thesis/tex/figures/"
col_pal = sns.color_palette()

############################################################################
# ch2_fig1 - ch2_fig2 Classification example
############################################################################

# from  http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
# http://stackoverflow.com/questions/24297097/is-there-a-way-to-make-matplotlib-scatter-plot-marker-or-color-according-to-a-di

df = sns.load_dataset("iris")
df["Y"] = 0
df.Y[df.species == "setosa"] = 1
df = df[["sepal_length","sepal_width","Y"]]

# Manually create some errors
df.sepal_length[(df.sepal_length >7.5)] -= 2
df.Y.iloc[[90,105,149,61,66,88,98]] = 1
df.Y.iloc[[48,10]] = 0
df = df.drop_duplicates()

def base_fig():
    f, ax1 = plt.subplots(1, 1, figsize=(4, 2.5))
    df_temp = df.loc[df.Y == 1]
    ax1.scatter(df_temp["sepal_length"], df_temp["sepal_width"], c=col_pal[2], label="Positive")
    df_temp = df.loc[df.Y == 0]
    ax1.scatter(df_temp["sepal_length"], df_temp["sepal_width"], c=col_pal[0], label="Negative")
    ax1.set_xlabel('Feature 1', fontsize=8)
    ax1.set_ylabel('Feature 2', fontsize=8)
    ax1.set_ylim(2, 4.5)
    ax1.set_xlim(4, 7.5)
    ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=8)
    ax1.tick_params(axis='both', which='major', labelsize=8)
    return f, ax1

# ch2_fig1a
f, ax1 = base_fig()
plt.savefig(path+'ch2_fig1a.eps', format='eps', dpi=1000, bbox_inches='tight')#, pad_inches=0)
plt.show()

# ch2_fig1b
f, ax1 = base_fig()
ax1.plot([4, 7.8], [2.1, 5], '--', c="black")
plt.savefig(path+'ch2_fig1b.eps', format='eps', dpi=1000, bbox_inches='tight')#, pad_inches=0)
plt.show()
# Cross table 1
TP = df.Y.sum() - 5
FP = 4
FN = 5
TN = df.shape[0] - TP - FP - FN
print TP, FP, FN, TN

# ch2_fig2
f, ax1 = base_fig()
# create step classifier
b = (5-2.1) / (7.8-4)
a = 2.1 - b*4
ax1.plot([4.7, 5.63], [b*4.7+a, b*5.63+a], '--', c="black")
ax1.plot([4.7, 4.7], [b*4.7+a, 0], '--', c="black")
ax1.plot([5.63, 5.63], [b*5.63+a, b*5.63+a+0.55], '--', c="black")
ax1.plot([5.63, 7.5], [b*5.63+a+0.55, b*5.63+a+0.55], '--', c="black")
plt.savefig(path+'ch2_fig2.eps', format='eps', dpi=1000, bbox_inches='tight')#, pad_inches=0)
plt.show()

# Cross table 2
TP = df.Y.sum() - 4
FP = 2
FN = 4
TN = df.shape[0] - TP - FP - FN
print TP, FP, FN, TN




