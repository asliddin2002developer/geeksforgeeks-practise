'''
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):


'''
Aproach #1:
    Time Complexity: O(n)
    Space Complexity: O(n)
'''
if not root:
    return []

queue = [root]
res = []

while queue:
    level = []

    for _ in range(len(queue)):
        node = queue.pop(0)
        level.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    res.append(level[0])
return res

'''
Aproach #2:
    Time Complexity: O(n)
    Space Complexity: O(n)
'''
#Function to get the left view of the binary tree.
def leftViewUtil(result, node,level):
    global max_level

    #if root is null, we simply return.
    if (node == None):
        return

    #if this is the first node of its level then it is in the left view.
    if (max_level < level):
        #storing data of current node in list.
        result.append(node.data)
        max_level = level

    #calling function recursively for left and right subtrees of current node.
    leftViewUtil(result,node.left, level+1);
    leftViewUtil(result,node.right, level+1);


#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    global max_level
    max_level = 0
    result = []
    leftViewUtil(result,root,1);
    #returning the list.
    return result
