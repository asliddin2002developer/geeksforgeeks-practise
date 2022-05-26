# User function Template for python3

class Solution:

    # Function to return the level order traversal of a tree.
    def levelOrder(self, root):
        # Code here
        queue = []
        res = []

        if root is None:
            return
        queue.append(root)

        while len(queue) > 0:
            node = queue.pop(0)
            res.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res



