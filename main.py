""" A naive crawler to find the shortest path between two wikipedia articles. """

import time
import wikipedia
import networkx as nx

START_TIME = time.time()
START_TERM = "LaunchCode"
END_TERM = "Facebook"
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
            if stop in child_name_list:  # tests if path exists
                PATH_BOOL = True
        parent_name_list = child_name_list  # sets the parent_name_list to the old children before the next loop
    return graph


def path_exists(graph, start, end):
    """ Tests if path exists between start and end, returns Bool """

    test = nx.has_path(graph, start, end)
    if test is True:
        global PATH_BOOL
        PATH_BOOL = True
    else:
        return False


def main():
    """ Runs this file and prints output """

    graph = build_graph(START_TERM, END_TERM)

    if PATH_BOOL:
        short_path = nx.shortest_path(graph, START_TERM, END_TERM)  # Find shortest path
        print('SHORTEST PATH: ', short_path)
    else:
        print('NO PATH FOUND')
    print("TIME: %s seconds" % (time.time() - START_TIME))

if __name__ == "__main__":
    main()
