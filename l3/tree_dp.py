class Solution:
    def pre_order(self, node):
        if node is None:
            return
        # process
        curr_node_val = node.val
        # res = min(self.pre_order(node.left) + self.pre_order(node.right), curr_node_val)
        res = (
            min(self.pre_order(node.left) + self.pre_order(node.right)) + curr_node_val
        )
        return res


def some_process(node, val) -> int:
    pass


def in_order(node):
    if node is None:
        return
    in_order(node.left)
    # process
    print(node.val)
    in_order(node.right)


def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    # process
    print(node.val)
