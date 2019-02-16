import numpy as np


class Node():
    def __init__(self,
                 value = None,
                 row = None,
                 column = None,
                 left = None,
                 right = None,
                 up = None,
                 down = None,
                 parent = None,
                 distance_from_dest = None,
                 distance_from_source = np.inf,
                 num_nodes_before_this_node = None):
        self.value = value
        self.row = row
        self.column = column
        self.parent = parent
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.distance_from_dest = distance_from_dest
        self.distance_from_source = distance_from_source
        self.num_nodes_before_this_node = num_nodes_before_this_node

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return self.__dict__ != other.__dict__

    # def cmp(self, a, b):
    #     return (a > b) - (a < b)

    def __lt__(self, other):
        selfPriority = self.distance_from_source + self.distance_from_dest
        otherPriority = other.distance_from_source + other.distance_from_dest
        return selfPriority < otherPriority

    def get_heuristic(self):
        return (self.distance_from_source + self.distance_from_dest)

    def get_children(self, node, algorithm):
        if algorithm == 'dfs':
            return [node.left, node.up, node.down, node.right]
        else:
            return [node.right, node.down, node.up, node.left]