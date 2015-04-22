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
    ax1.scatter(df_temp["sepal_length"], df_temp["sepal_width"], c=col_pal[2], label="Positive",edgecolors='none')
    df_temp = df.loc[df.Y == 0]
    ax1.scatter(df_temp["sepal_length"], df_temp["sepal_width"], c=col_pal[0], label="Negative",edgecolors='none')
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



# ch3_fig1 # Class dependent
f, ax1 = base_fig()
# create step classifier
b = (5-2.1) / (7.8-4)
a = 2.1 - b*4
ax1.plot([5.15, 5.63], [b*5.15+a, b*5.63+a], '--', c="black")
ax1.plot([5.15, 5.15], [b*5.15+a, 0], '--', c="black")
ax1.plot([5.63, 5.63], [b*5.63+a, b*5.63+a+0.55], '--', c="black")
ax1.plot([5.63, 7.5], [b*5.63+a+0.55, b*5.63+a+0.55], '--', c="black")
plt.savefig(path+'ch3_fig1.eps', format='eps', dpi=1000, bbox_inches='tight')#, pad_inches=0)
plt.show()

# Cross table 3
TP = df.Y.sum() - 3
FP = 6
FN = 3
TN = df.shape[0] - TP - FP - FN
err = (FP+FN)*1.0 / (TP+TN+FP+FN)
rec = TP*1.0/(TP+FN)
pre = TP*1.0/(TP+FP)
f1 = 2.0*(rec*pre)/(rec+pre)
print TP, FP, FN, TN, err, rec, pre, f1
print .2*6+1.8*3


# ch3_fig2 # Example-dependent cost-sensitive

def base_fig2():
    #colors
    color_red = []
    color_red.append(sns.color_palette(sns.light_palette(col_pal[2], reverse=True))[2])
    color_red.append(col_pal[2])
    color_red.append(sns.color_palette(sns.dark_palette(col_pal[2], reverse=True))[2])
    color_blue = []
    color_blue.append(sns.color_palette(sns.light_palette(col_pal[0], reverse=True))[3])
    color_blue.append(col_pal[0])
    color_blue.append(sns.color_palette(sns.dark_palette(col_pal[0], reverse=True))[3])
    # sns.palplot(sns.light_palette(col_pal[0], reverse=True))

    sns.color_palette(sns.light_palette(col_pal[2]))

    #identify lower left corner
    df_cost_dark = df.loc[(df["sepal_length"] < 5.25) & (df["sepal_width"] < 2.8)]
    np.random.seed(5467815)
    temp_rand = np.random.rand(df.loc[~((df["sepal_length"] < 5.25) & (df["sepal_width"] < 2.8))].shape[0])
    df_cost_normal = df.loc[~((df["sepal_length"] < 5.25) & (df["sepal_width"] < 2.8))].loc[temp_rand<=0.7]
    df_cost_light = df.loc[~((df["sepal_length"] < 5.25) & (df["sepal_width"] < 2.8))].iloc[temp_rand>0.7]

    f, ax1 = plt.subplots(1, 1, figsize=(4, 2.5))
    # First medium cost (df_cost3)
    df_temp = df_cost_normal.loc[df.Y == 1]
    ax1.scatter(df_temp["sepal_length"], df_temp["sepal_width"], c=col_pal[2], label="Positive",edgecolors='none')
    df_temp = df_cost_normal.loc[df.Y == 0]
    ax1.scatter(df_temp["sepal_length"], df_temp["sepal_width"], c=col_pal[0], label="Negative",edgecolors='none')
    # Cost dark
    df_temp = df_cost_dark.loc[df.Y == 1]
    ax1.scatter(df_temp["sepal_length"], df_temp["sepal_width"], c=color_red[2],edgecolors='none')
    df_temp = df_cost_dark.loc[df.Y == 0]
    ax1.scatter(df_temp["sepal_length"], df_temp["sepal_width"], c=color_blue[2],edgecolors='none')
    # Cost light
    df_temp = df_cost_light.loc[df.Y == 1]
    ax1.scatter(df_temp["sepal_length"], df_temp["sepal_width"], c=color_red[0],edgecolors='none')
    df_temp = df_cost_light.loc[df.Y == 0]
    ax1.scatter(df_temp["sepal_length"], df_temp["sepal_width"], c=color_blue[0],edgecolors='none')

    ax1.set_xlabel('Feature 1', fontsize=8)
    ax1.set_ylabel('Feature 2', fontsize=8)
    ax1.set_ylim(2, 4.5)
    ax1.set_xlim(4, 7.5)
    ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=8)
    ax1.tick_params(axis='both', which='major', labelsize=8)
    return f, ax1

f, ax1 = base_fig2()
plt.savefig(path+'ch3_fig2.eps', format='eps', dpi=1000, bbox_inches='tight')#, pad_inches=0)
plt.show()


# ch3_fig3 # example dependetn cost-sensitive algorithm
f, ax1 = base_fig2()
# create step classifier
b = (5-2.1) / (7.8-4)
a = 2.1 - b*4
ax1.plot([5.15, 8], [b*5.15+a, b*8+a], '--', c="black")
ax1.plot([5.15, 5.15], [b*5.15+a, 2.35], '--', c="black")
ax1.plot([5.0, 5.15], [2.35, 2.35], '--', c="black")
ax1.plot([5.0, 5.0], [b*5.0+a, 2.35], '--', c="black")
ax1.plot([4.7, 5.0], [b*4.7+a, b*5.0+a], '--', c="black")
ax1.plot([4.7, 4.7], [b*4.7+a, 0], '--', c="black")

plt.savefig(path+'ch3_fig3.eps', format='eps', dpi=1000, bbox_inches='tight')#, pad_inches=0)
plt.show()

# Cross table 3
TP = df.Y.sum() - 3
FP = 4
FN = 3
TN = df.shape[0] - TP - FP - FN
err = (FP+FN)*1.0 / (TP+TN+FP+FN)
rec = TP*1.0/(TP+FN)
pre = TP*1.0/(TP+FP)
f1 = 2.0*(rec*pre)/(rec+pre)
print TP, FP, FN, TN, err, rec, pre, f1
print .2*6+1.8*3

# Savings all examples
FP_light    =   [2, 1, 1, 2]
FP_normal   =   [2, 1, 1, 2]
FP_dark     =   [0, 0, 4, 0]

FN_light    =   [1, 1, 1, 1]
FN_normal   =   [2, 2, 2, 2]
FN_dark     =   [2, 1, 0, 0]

costs_FP = [0.1, 0.5, 5]
costs_FN = [1, 2, 10]

cost_0 = 23*costs_FP[0] + 44*costs_FP[1] + 5*costs_FP[2]
for i in range(4):
    costt_ = FP_light[i]*costs_FP[0] + FP_normal[i]*costs_FP[1]+ FP_dark[i]*costs_FP[2] +FN_light[i]*costs_FN[0] + FN_normal[i]*costs_FN[1]+ FN_dark[i]*costs_FN[2]
    print i, costt_, (cost_0 - costt_) / cost_0