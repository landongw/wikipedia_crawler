""" A web crawler to find a link path between two articles on wikipedia.org """

import wikipedia
import networkx as nx

START_TERM = "LaunchCode"
START_PAGE = wikipedia.page(START_TERM)
START_LINKS = START_PAGE.links
END_TERM = "Facebook"
START_NODE = {'parent': 0, 'links': [START_PAGE.links]}
# print(current_page['links'])

# start page parent?

# create storage (array or dict) for page nodes, parent nodes, child nodes

# counter for level

# get links from start page
# print(len(START_LINKS))
# print(START_LINKS)

# for each link
#      create new page variable




# THE NETWORK
# create the graph
G = nx.Graph()
# START_LINKS = ['Zoellner Quartet', 'Zürich', 'Élie Metchnikoff']  # this is to bypas the large list for testing purposes, remove

G.add_node(START_TERM)
G.add_nodes_from(START_LINKS)

# create edges
edge_list = []
for link in START_LINKS:
    new_tuple = (START_TERM, link)
    edge_list.append(tuple(new_tuple))
G.add_edges_from(edge_list)

print('Connected components: ', list(nx.connected_components(G)))
print('Nodes: ', list(nx.nodes(G)))


nx.clustering(G)
