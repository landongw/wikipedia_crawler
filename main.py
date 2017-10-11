""" A web crawler to find a link path between two articles on wikipedia.org """

import time
start_time = time.time()
import wikipedia
import networkx as nx
from networkx.algorithms import approximation
import matplotlib.pyplot as plt


START_TERM = "LaunchCode"
END_TERM = "The Wealth of Nations"
START_PAGE = wikipedia.page(START_TERM)  # get start page
START_LINKS = sorted(START_PAGE.links)  # get links from start page
edge_list = []  # iterable list for edges

G = nx.Graph()  # create the graph # create storage (array or dict) for page nodes, parent nodes, child nodes
G.add_node(START_TERM)  # create start node
G.add_nodes_from(START_LINKS)  # create child nodes

# glevel = 1  # counter for level

for link in START_LINKS:  # for each link create new page node and edge
    new_tuple = (START_TERM, link)
    edge_list.append(tuple(new_tuple))
    NEW_PAGE = wikipedia.page(link)  # get start page
    NEW_LINKS = sorted(NEW_PAGE.links)
    G.add_nodes_from(NEW_LINKS)  # create child nodes
    for new_link in NEW_LINKS:
        G.add_edge(new_link, link)
G.add_edges_from(edge_list)  # create edges


# adj_articles = sorted(G.adjacency_list())
# sp = dict(nx.all_pairs_shortest_path(G))
PATH_BOOL = nx.has_path(G, START_TERM, END_TERM)  # True if a path exists
SHORT_PATH = nx.shortest_path(G, START_TERM, END_TERM)  # Shortest path
# SIM_PATH = nx.all_simple_paths(G, START_TERM, END_TERM, 5)


# print('ADJACENT ARTICLES: ', adj_articles)
# print('ALL NODES: ', list(nx.nodes(G)))
print(PATH_BOOL)
print('NUMBER OF NODES: ', G.number_of_nodes())
print('NUMBER OF EDGES: ', G.number_of_edges())
# print('ALL PATHS: ', len(list(SIM_PATH)))
print('SHORTEST PATH: ', SHORT_PATH)


# #####
# ######  DRAW THE TEST GRAPH WITH DUMMY DATA
# #####

# G = nx.petersen_graph()
# plt.subplot(121)

# nx.draw(G, with_labels=True, font_weight='bold')
# plt.subplot(122)

# nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
# plt.show()

# nx.clustering(G)

print("TIME: %s seconds" % (time.time() - start_time))

