#!/usr/bin/python

import os
from fnmatch import fnmatch
import pandas as pd
import re

path_ = "/home/al/DriveAl/Publications/2015/phd-thesis/tex"

# Get tex files
files_ = []
for path, subdirs, files in os.walk(path_):
    for name in files:
        if fnmatch(name, "*.tex"):
            files_.append(os.path.join(path, name))
files_.sort()

# For each file search the todos
todos = pd.DataFrame(columns=["file", "section", "todo"], dtype="S30")
i = 0
for file_ in files_:
    file = open(file_)
    file_name = file_.split("/")[-1].split(".")[0]
    section = file_name
    lines = file.readlines()

    for line in lines:
        if "section{" in line:
            section = line.translate(None, '\t\t\n').split("{")[-1][:-1]
        if "todo{" in line:
            todos.loc[i] = file_name, section, line.translate(None, '\t\t\n').split("{")[-1][:-1]
            i += 1

print todos.to_string()