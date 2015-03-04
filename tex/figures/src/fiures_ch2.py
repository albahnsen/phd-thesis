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
# ch2_fig1 Classification example
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

f, ax1 = plt.subplots(1, 1, figsize=(4, 2.5))
df_temp = df.loc[df.Y == 1]
ax1.scatter(df_temp["sepal_length"], df_temp["sepal_width"], c=col_pal[2], label="Positive")
df_temp = df.loc[df.Y == 0]
ax1.scatter(df_temp["sepal_length"], df_temp["sepal_width"], c=col_pal[0], label="Negative")
ax1.plot([4, 7.8], [2.1, 5], '--', c="black")
ax1.set_xlabel('Feature 1', fontsize=8)
ax1.set_ylabel('Feature 2', fontsize=8)
ax1.set_ylim(2, 4.5)
ax1.set_xlim(4, 7.5)
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=8)
ax1.tick_params(axis='both', which='major', labelsize=8)
plt.savefig(path+'ch2_fig1.eps', format='eps', dpi=1000, bbox_inches='tight')#, pad_inches=0)
plt.show()

# Cross table
TP = df.Y.sum() - 5
FP = 4
FN = 5
TN = df.shape[0] - TP - FP - FN

print TP, FP, FN, TN