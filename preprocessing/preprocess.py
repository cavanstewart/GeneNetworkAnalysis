import pandas as pd
import numpy as np 
import networkx as nx 
import os

DIR = os.path.dirname(os.path.abspath(__file__))

# load adj matrix data into numpy array

def load_data():
	mat = pd.read_csv('{}/../data/GeneticAdjacencyMatrix.csv'.format(DIR))
	mat.drop(columns=['Unnamed: 0'], inplace=True) # drop name col
	genetic = np.asarray(mat)
	return genetic



# get a networkx graph of our data with original weights
# input data is numpy array of adj matrix

def get_graph(data):
	G = nx.from_numpy_matrix(data, create_using=nx.MultiGraph)
	return(G)



# get a networkx graph of our data 
# with entry 1 if weight above threshold
# and 0 if weight below threshold
# input data is numpy array of adj matrix
# default threshold is mean weight of all entries

def get_threshold_graph(data, threshold = 0.007243366440534859):
	data = data > threshold # turn into array of 1s and 0s
	G = nx.from_numpy_matrix(data)
	return(G)






