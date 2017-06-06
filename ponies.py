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
filepath = "/Users/DavidPorter/Desktop/HorseRacing/DataFiles/PIM0520.csv"
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

# Horse Lasix today
def lasix(meds, i):
	if int(meds) == 1 or int(meds) == 3 or int(meds) == 4 or int(meds) == 5:
		results[i].append("YES LASIX")
	else:
		results[i].append("no lasix")

# Recent bullet workouts
def bullets(wo1, wo2, wo3, i):
	total = 0
	if wo1:
		if float(wo1) < 0:
			total += 1
	if wo2:
		if float(wo2) < 0:
			total += 1
	if wo3:
		if float(wo3) < 0:
			total += 1

	results[i].append(str(total) + " Bullets")


# Loop through array and perform calculations, append to results array
for i, line in enumerate(ppfile):
	results.append([ppfile[i][44]])

	winpct(ppfile[i][96], ppfile[i][97], i)
	lasix(ppfile[i][61], i)
	bullets(ppfile[i][113], ppfile[i][114], ppfile[i][115], i)

for i, line in enumerate(results):
	print results[i]

print


# Next up, start data analysis. Functions? Class? Think about best way to solve.
