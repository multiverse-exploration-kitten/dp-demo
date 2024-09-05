from typing import List


class Solution:
    def __init__(self):
        self.num_nodes = 0
        self.adjacency_list = []
        self.subtree_size = []
        self.subtree_distance_sum = []
        self.result = []

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Returns the sum of distances of all nodes in a tree.
        """
        self.initialize_tree(n, edges)
        self.calculate_subtree_sizes_and_distances(0, -1)
        self.calculate_result(0, -1, 0)
        return self.result

    def initialize_tree(self, num_nodes, edges):
        """
        Initializes the adjacency list and related lists for the tree.
        """
        self.num_nodes = num_nodes
        self.adjacency_list = [[] for _ in range(self.num_nodes)]
        self.subtree_size = [0] * self.num_nodes
        self.subtree_distance_sum = [0] * self.num_nodes
        self.result = [0] * self.num_nodes

        for edge in edges:
            self.adjacency_list[edge[0]].append(edge[1])
            self.adjacency_list[edge[1]].append(edge[0])

    def calculate_subtree_sizes_and_distances(self, current_node, parent_node):
        """
        First DFS to calculate subtree sizes and distance sums for each node.
        """
        for neighbor in self.adjacency_list[current_node]:
            if neighbor != parent_node:
                self.calculate_subtree_sizes_and_distances(neighbor, current_node)
                self.subtree_size[current_node] += self.subtree_size[neighbor]
                self.subtree_distance_sum[current_node] += (
                    self.subtree_distance_sum[neighbor] + self.subtree_size[neighbor]
                )
        self.subtree_size[current_node] += 1

    def calculate_result(self, current_node, parent_node, parent_contribution):
        """
        Second DFS to calculate the result for each node based on the contributions
        from the parent node and the subtree distance sums.
        """
        self.result[current_node] = (
            self.subtree_distance_sum[current_node]
            + parent_contribution
            + (self.num_nodes - self.subtree_size[current_node])
        )

        for neighbor in self.adjacency_list[current_node]:
            if neighbor != parent_node:
                new_parent_contribution = (
                    self.result[current_node]
                    - self.subtree_distance_sum[neighbor]
                    - self.subtree_size[neighbor]
                )
                self.calculate_result(neighbor, current_node, new_parent_contribution)
