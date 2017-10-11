""" A naive crawler to find the shortest path between two wikipedia articles.

    DISCLAIMER: CURRENTLY ONLY GOES THREE LEVELS DEEP
    TODO: Make deeper

"""

import time
import wikipedia
import networkx as nx
# from networkx.algorithms import approximation
import matplotlib.pyplot as plt

START_TIME = time.time()
START_TERM = "LaunchCode"
END_TERM = "The Wealth of Nations"


def build_graph(start):
    """ Builds the wiki graph """
    #  TODO: make into recursive loop?

    start_page = wikipedia.page(start)  # get start page
    start_links = sorted(start_page.links)  # get links from start page
    graph = nx.Graph()  # Instantiate graph
    graph.add_node(START_TERM)  # create start node
    graph.add_nodes_from(start_links)  # create child nodes
    edge_list = []  # iterable list for edges

    for link in start_links:  # for each link create new page node and edge
        new_tuple = (START_TERM, link)
        edge_list.append(tuple(new_tuple))
        new_page = wikipedia.page(link)  # get start page
        new_links = sorted(new_page.links)
        graph.add_nodes_from(new_links)  # create child nodes
        for new_link in new_links:
            new_tuple2 = (new_link, link)
            edge_list.append(tuple(new_tuple2))
    graph.add_edges_from(edge_list)  # create edges
    return graph


def draw_test_graph():
    """ Draw a test graph with dummy data """
    #  TODO: make this into something useful

    graph = nx.petersen_graph()

    plt.subplot(121)

    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.subplot(122)

    nx.draw_shell(graph,
                  nlist=[range(5, 10), range(5)],
                  with_labels=True,
                  font_weight='bold')
    plt.show()


def main():
    """ Runs this file and prints output """

    graph = build_graph(START_TERM)
    path_exists = nx.has_path(graph, START_TERM, END_TERM)  # True if exists
    short_path = nx.shortest_path(graph, START_TERM, END_TERM)  # Shortest path

    # adj_articles = sorted(G.adjacency_list())
    # sp = dict(nx.all_pairs_shortest_path(G))
    # SIM_PATH = nx.all_simple_paths(G, START_TERM, END_TERM, 5)
    # print('ADJACENT ARTICLES: ', adj_articles)
    # print('ALL NODES: ', list(nx.nodes(G)))
    # print('NUMBER OF NODES MAPPED: ', G.number_of_nodes())
    # print('NUMBER OF EDGES: ', G.number_of_edges())
    # print('ALL PATHS: ', len(list(SIM_PATH)))

    if path_exists:
        print('SHORTEST PATH: ', short_path)
    else:
        print('NO PATH FOUND')
    print("TIME: %s seconds" % (time.time() - START_TIME))

if __name__ == "__main__":
    main()
