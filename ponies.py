# Import libraries for analysis
import math
import numpy
import scipy
import csv
import sys
import os
import pandas
import sklearn

# Checking python version
print(sys.version_info)

# Create empty PP array
ppfile = []
results = []

# Ask for file path
#filepath = raw_input("Enter file path:")
filepath = "/Users/DavidPorter/Desktop/HorseRacing/DataFiles/CDX0506.csv"
filepath = filepath.replace(" ","")

# Check if file path is correct
if os.path.isfile(filepath):
	print "Got it."
else:
	print "Path incorrect."
	sys.exit()

# Open file and import into ppfile array
with open(filepath, "r") as f:
	reader = csv.reader(f)
	ppfile = list(reader)

# Defining some horse functions

# Calculates win percentage and appends to array
def winpct(starts, wins, i):

	if int(starts) == 0:
		results[i].append("Maiden")
	else:
		results[i].append(float(wins)/float(starts)*100)

# Loop through array and perform calculations, append to results array
for i, line in enumerate(ppfile):
	results.append([ppfile[i][44]])

	winpct(ppfile[i][96],ppfile[i][97],i)


print results
print

# Next up, start data analysis. Functions? Class? Think about best way to solve.
