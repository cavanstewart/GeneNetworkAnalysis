import pandas as pd 
import numpy as np 
import networkx as nx 
import os 
import sys 
import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure

DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, '{}/../preprocessing'.format(DIR))

import preprocess

def visualize():
	data = preprocess.load_data()
	G = preprocess.get_threshold_graph(data, threshold=0.0028)
	results = pd.read_csv('{}/louvain_results.csv'.format(DIR))
	partition = dict(zip(results.iloc[:,0], results.moduleColor))
	# community colors
	cmap = ['blue', 'black', 'pink', 'red', 'brown', 'grey', 'green', 'yellow', 'greenyellow', 'magenta']
	pos = nx.spring_layout(G)
	count = 0
	for com in set(partition.values()):
		list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]
		nx.draw_networkx_nodes(G, pos, list_nodes, node_size=20, node_color=cmap[count])
		count += 1
	nx.draw_networkx_edges(G, pos, alpha=0.03)
	plt.show()
	return None