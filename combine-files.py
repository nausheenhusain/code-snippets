import shutil
import glob

def combine_files():
	"""
	import csv files from one directory into one csv, keeps header from first file
	"""

	path = r'/Users/Desktop/data/'
	allFiles = glob.glob(path + "/*.csv")
	with open('/Users/Desktop/data/all-data.csv', 'wb') as outfile:
		for i, fname in enumerate(allFiles):
			with open(fname, 'rb') as infile:
				if i != 0:
					# Throw away header on all but first file
					infile.readline()
				# Block copy rest of file from input to output without parsing
				shutil.copyfileobj(infile, outfile)
				print(fname + " has been imported.")

combine_files()