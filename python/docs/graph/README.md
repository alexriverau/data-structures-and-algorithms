# Graph

Graph implementation and testing.

## Challenge

* Implement a Graph represented as an adjacency list. Include the following methods:

  * add node:
    * Arguments: value
    * Returns the added node
    * Adds a node to the graph

  * add edge:
    * Arguments: 2 nodes to be connected by the edge, weight (optional)
    * Returns nothing
    * Adds a new edge between two nodes in the graph
    * If specified, assign a weight to the edge
    * Both nodes should already be in the graph

  * get nodes
    * Arguments: none
    * Returns all the nodes in the graph as a collection (set, list, or similar)
    * Empty collection returned if there are no nodes

  * get neighbors
    * Arguments: node
    * Returns a collection of edges connected to the given node
      * Include the weight of the connection in the returned collection
    * Empty collection returned if there are no nodes

  * size
    * Arguments: none
    * Returns the total number of nodes in the graph
    * 0 if there are none

## Testing

* **run:** pytest tests/data_structures/test_graph.py
* [test_graph.py](/Users/Alex/projects/data-structures-and-algorithms/python/tests/data_structures/test_graph.py)
