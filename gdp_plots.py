import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt
import sys
import glob

# load data and transpose so that country names are
# the columns and their gdp data becomes the rows

# read data into a pandas dataframe and transpose
#filename = "gapminder_gdp_oceania.csv"
#filename = sys.argv[1] #first parameter after scriptname

def parse_arguments():
	"""Parses the user command line argument and returns file list
	
	Inputs: 
	------
		Nothing
	Returns:
	--------
		file_list: list of file names
	"""
	if len(sys.argv) == 1:
		#no arguments supplied
		print("arguments required")
		print("Usage: gdp_plot.py <filenames>")
		print("Options: -a: plot all data in the current dir.")
		exit()

	if sys.argv[1] == '-a' :
		file_list = glob.glob("*gdp*.csv")
		if len(file_list) == 0:
			print("No data files found *gdp*.csv in current dir.")
			exit()
	else:
		file_list = sys.argv[1:]

	return file_list

def create_plots(filename):
	"""Plot data
	Inputs:
	-------
		file name of data
	Returns:
	--------
		Nothing (creates plot on screen)
	"""
	data = pandas.read_csv(filename, index_col = 
'country').T

	# create a plot the transposed data
	ax = data.plot(title=filename)

	# axes labels
	ax.set_xlabel('Year')
	ax.set_ylabel('GDP Per Capita')

	# set axes ticks
	ax.set_xticks(range(len(data.index)))
	ax.set_xticklabels(data.index,rotation=45)

	# display the plot
	plt.show()

def main():
	file_list = parse_arguments()
	for filename in file_list:
		create_plots(filename)

main()
