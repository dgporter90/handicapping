# Modifying original file to find trends in combined data sets with machine learning
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

# Ask for file path
#filepath = raw_input("Enter file path:")
#filepath = filepath.replace(" ","")
filepath = "/Users/DavidPorter/Desktop/HorseRacing/DataFiles/combined.csv"

# Check if file path is correct
if os.path.isfile(filepath):
	print "Got it."
else:
	print "Path incorrect."
	sys.exit()

# Create empty array for results
results = []

# Open file and import into python
with open(filepath, "r") as f:
	reader = csv.reader(f)
	ppfile = list(reader)
ppfile = pandas.read_csv(filepath, sep = ",", low_memory = False, header=None)

print ppfile.shape
print 




