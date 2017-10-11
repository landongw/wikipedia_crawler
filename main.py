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
END_TERM = "Thomas Jefferson"
PATH_BOOL = False


def build_graph(start, stop):
    """ Builds the wiki graph """

    graph = nx.Graph()  # Instantiate graph
    depth = 1
    global PATH_BOOL
    child_name_list = []
    parent_name_list = []  # List of all nodes on current level

    if depth == 1:
        parent_page = wikipedia.page(start)  # get start page
        parent_name = start
        graph.add_node(start)  # add start node
        child_name_list = parent_page.links  # create list of child nodes
        graph.add_nodes_from(child_name_list)  # add child nodes to graph
        for child_name in child_name_list:  # add edges between start node and child nodes
            graph.add_edge(child_name, parent_name)

        print('NUMBER OF NODES MAPPED: ', graph.number_of_nodes())
        print('NUMBER OF EDGES MAPPED: ', graph.number_of_edges())
        print('DEPTH: ', depth)
        parent_name_list = child_name_list  # set start as list of previous iteration's children
        depth += 1

    while not PATH_BOOL:  # test for path
        depth += 1
        for parent_name2 in parent_name_list:
            try:
                parent_page = wikipedia.page(parent_name2)  # get parent page
                # parent_node = graph.add_node(parent_name)  # add start node
            except wikipedia.exceptions.PageError:  # skips if page doesn't exist
                print('PageError, continuing.')
                continue
            child_name_list = parent_page.links  # create list of child nodes
            graph.add_nodes_from(child_name_list)  # add child nodes to graph
            for child_name in child_name_list:  # add edges between start node and child nodes
                graph.add_edge(child_name, parent_name2)
            print('NUMBER OF NODES MAPPED: ', graph.number_of_nodes())
            print('NUMBER OF EDGES MAPPED: ', graph.number_of_edges())
            print('DEPTH: ', depth)
            if END_TERM in child_name_list:
                PATH_BOOL = True
        parent_name_list = child_name_list
    return graph

    # while not path_exists(graph, START_TERM, END_TERM):
    #     edge_list = []  # iterable list for edges

    #     if isinstance(start, list):
    #         for substart in start:
    #             start_page = wikipedia.page(substart)  # get start page
    #             start_links = sorted(start_page.links)  # get links from start page
    #             graph.add_nodes_from(start_links)  # create child nodes

    #             for link in start_links:  # for each link create new page node and edge
    #                 new_tuple = (substart, link)
    #                 edge_list.append(tuple(new_tuple))
    #                 try:
    #                     new_page = wikipedia.page(link)  # get start page
    #                 except wikipedia.exceptions.PageError:
    #                     print('PageError, continuing.')
    #                     continue
    #                 new_links = sorted(new_page.links)
    #                 graph.add_nodes_from(new_links)  # create child nodes
    #                 # for new_link in new_links:
    #                 #     new_tuple2 = (new_link, link)
    #                 #     edge_list.append(tuple(new_tuple2))
    #             graph.add_edges_from(edge_list)  # create edges
    #         start = new_links  # WORKING: This returns a list of links,  make start page into output of loop trough this list
    #         print('NUMBER OF NODES MAPPED: ', graph.number_of_nodes())
    #         print('NUMBER OF EDGES: ', graph.number_of_edges())
    #     else:
    #         start_page = wikipedia.page(start)  # get start page
    #         start_links = sorted(start_page.links)  # get links from start page
    #         graph.add_nodes_from(start_links)  # create child nodes

    #         for link in start_links:  # for each link create new page node and edge
    #             new_tuple = (start, link)
    #             # edge_list.append(tuple(new_tuple))
    #             new_page = wikipedia.page(link)  # get start page
    #             new_links = sorted(new_page.links)
    #             graph.add_nodes_from(new_links)  # create child nodes
    #             graph.add_edge(new_tuple)

    #             # for new_link in new_links:
    #             #     new_tuple2 = (new_link, link)
    #             #     edge_list.append(tuple(new_tuple2))
    #         # graph.add_edges_from(edge_list)  # create edges
    #         start = new_links  # WORKING: This returns a list of links,  make start page into output of loop trough this list
    #         print('NUMBER OF NODES MAPPED: ', graph.number_of_nodes())
    #         print('NUMBER OF EDGES: ', graph.number_of_edges())

    # global PATH_BOOL
    # PATH_BOOL = True
    # return graph


def path_exists(graph, start, end):
    """ Tests if path exists between start and end, returns Bool """

    test = nx.has_path(graph, start, end)
    if test is True:
        global PATH_BOOL
        PATH_BOOL = True
    else:
        return False


# def draw_test_graph():
#     """ Draw a test graph with dummy data """
#     #  TODO: make this into something useful

#     graph = nx.petersen_graph()

#     plt.subplot(121)

#     nx.draw(graph, with_labels=True, font_weight='bold')
#     plt.subplot(122)

#     nx.draw_shell(graph,
#                   nlist=[range(5, 10), range(5)],
#                   with_labels=True,
#                   font_weight='bold')
#     plt.show()


def main():
    """ Runs this file and prints output """

    graph = build_graph(START_TERM, END_TERM)

    # adj_articles = sorted(G.adjacency_list())
    # sp = dict(nx.all_pairs_shortest_path(G))
    # SIM_PATH = nx.all_simple_paths(G, START_TERM, END_TERM, 5)
    # print('ADJACENT ARTICLES: ', adj_articles)
    # print('ALL NODES: ', list(nx.nodes(G)))
    # print('NUMBER OF NODES MAPPED: ', G.number_of_nodes())
    # print('NUMBER OF EDGES: ', G.number_of_edges())
    # print('ALL PATHS: ', len(list(SIM_PATH)))

    if PATH_BOOL:
        short_path = nx.shortest_path(graph, START_TERM, END_TERM)  # Find shortest path
        print('SHORTEST PATH: ', short_path)
    else:
        print('NO PATH FOUND')
    print("TIME: %s seconds" % (time.time() - START_TIME))

if __name__ == "__main__":
    main()
