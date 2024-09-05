# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rob(self, root):
        rob_result, no_rob_result = self.rob_subtree(root)
        return rob_result

    def rob_subtree(self, root):
        if not root:
            return 0, 0

        rob_left, no_rob_left = self.rob_subtree(root.left)
        rob_right, no_rob_right = self.rob_subtree(root.right)

        rob_current = no_rob_left + no_rob_right + root.val
        no_rob_current = rob_left + rob_right

        return max(rob_current, no_rob_current), no_rob_current
