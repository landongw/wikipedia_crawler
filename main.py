""" A web crawler to find a link path between two articles on wikipedia.org """

import wikipedia
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import approximation

START_TERM = "LaunchCode"
START_PAGE = wikipedia.page(START_TERM)  # get start page
START_LINKS = sorted(START_PAGE.links)  # get links from start page
# START_LINKS = ['Zoellner Quartet', 'Zürich', 'Élie Metchnikoff']  # this is to bypas the large list for testing purposes, remove
END_TERM = "Facebook"
# START_NODE = {'parent': 0, 'links': [START_PAGE.links]}
# print(current_page['links'])

G = nx.Graph()  # create the graph # create storage (array or dict) for page nodes, parent nodes, child nodes

edge_list = []  # iterable list for edges
glevel = 1  # counter for level

G.add_node(START_TERM, level=0) # create start node
G.add_nodes_from(START_LINKS, level=glevel)  # create child nodes

for link in START_LINKS:  # for each link create new page node and edge
    new_tuple = (START_TERM, link)
    edge_list.append(tuple(new_tuple))
    NEW_PAGE = wikipedia.page(link)  # get start page
    NEW_LINKS = sorted(NEW_PAGE.links)
    G.add_nodes_from(NEW_LINKS, level=glevel + 1)  # create child nodes
    for new_link in NEW_LINKS:
        G.add_edge(new_link, link)
G.add_edges_from(edge_list)  # create edges
glevel += 1
adj_articles = sorted(G.adjacency_list())
print('Adjacent Articles: ', adj_articles)



# for link in adj_articles:  # iterate through level 1
#     START_TERM = link
#     START_PAGE = wikipedia.page(START_TERM)
#     START_LINKS = sorted(START_PAGE.links)
#     G.add_nodes_from(START_LINKS, level=glevel)  # create child nodes

#     new_tuple = (START_TERM, link)
#     edge_list.append(tuple(new_tuple))
# G.add_edges_from(edge_list)
# glevel += 1
# adj_articles = sorted(G.adjacency_list()[1])
# print('Adjacent Articles 2: ', adj_articles)


# for link in adj_articles:  # iterate through level 2
#     START_TERM = link
#     START_PAGE = wikipedia.page(START_TERM)
#     START_LINKS = sorted(START_PAGE.links)

#     new_tuple = (START_TERM, link)
#     edge_list.append(tuple(new_tuple))
# G.add_edges_from(edge_list)
# glevel += 1



print('ALL NODES: ', list(nx.nodes(G)))
# sp = dict(nx.all_pairs_shortest_path(G))
sp2 = nx.has_path(G, "LaunchCode", "Facebook")  # TODO HOW DOES ONE IDENTIFY A NODE ??
print(sp2)  
print('NUMBER OF NODES: ', G.number_of_nodes())
print('NUMBER OF EDGES: ', G.number_of_edges())



# #DRAW THE TEST GRAPH WITH DUMMY DATA
# G = nx.petersen_graph()
# plt.subplot(121)

# nx.draw(G, with_labels=True, font_weight='bold')
# plt.subplot(122)

# nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
# plt.show()



nx.clustering(G)
