#!/usr/bin/python

import networkx as nx

"""
Helpful resources:
NetworkX - Great python library for working with graphs
  https://networkx.org/documentation/stable/tutorial.html

Summary of graph terms and alogorithms:
  https://towardsdatascience.com/10-graph-algorithms-visually-explained-e57faa1336f3
"""

# Detect Loops from Graphs


def loop_detector_working(graph):
    try:
        cycles = nx.find_cycle(graph)
        if cycles:
            return True
    except nx.exception.NetworkXNoCycle:
        return False
    return False


def loop_detector(graph):
    if not graph:
        return False
    for edge in nx.dfs_edges(graph):
        current_node, next_node = edge
        print("outer edge: ", edge)
        for inner_edge in nx.dfs_edges(graph, next_node):
            print(f"  inner edge for {current_node}", inner_edge)
            if current_node == inner_edge[1]:  # next_next_node
                return True
    return False


def p1():
    tests = []
    tests.append(nx.DiGraph())
    tests[-1].add_edges_from([(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)])

    tests.append(nx.DiGraph())
    tests[-1].add_edges_from([(0, 1), (0, 2), (1, 2), (2, 3)])

    tests.append(nx.DiGraph())
    tests[-1].add_edges_from([])

    for test_input in tests:
        print("\n" + "#"*40)
        print("input", test_input.edges)
        correct_result = loop_detector_working(test_input)
        my_result = loop_detector(test_input)

        print("Loop? correct: ", correct_result, " my: ", my_result)
        if correct_result != my_result:
            print("!"*20, " ERROR ", "!"*20)


if __name__ == "__main__":
    p1()
