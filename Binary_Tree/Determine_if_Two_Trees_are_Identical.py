'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self,root1, root2):
        # Code here

        """ Aproach 1 """
        if not root1 and not root2:
            return True

        if not root1 or not root2 or root1.data != root2.data:
            return False

        return (self.isIdentical(root1.left, root2.left) and
                self.isIdentical(root1.right, root2.right))



        '''Aproach 2'''

        tree1 = []
        tree2 = []

        def preorder1(root):
            if not root:
                return
            tree1.append(root.data)
            preorder1(root.left)
            preorder1(root.right)
        preorder1(root1)

        def preorder2(root):
            if not root:
                return
            tree2.append(root.data)
            preorder2(root.left)
            preorder2(root.right)
        preorder2(root2)

        return tree1 == tree2