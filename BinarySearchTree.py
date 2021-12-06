class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper( self.root,new_val)

    def insert_helper(self, root, new_val):
        if root is None:
            return Node(new_val)
        if new_val > root.value:
            return self.insert_helper( root.right, new_val)
        else :
            return self.insert_helper( root.left , new_val)

    def search(self, find_val):
        return self.search_helper( self.root, find_val)
    def search_helper( self, root, find_val):
        if root :
            if root.value == find_val:
                return True
            elif find_val > root.value :
                return self.search_helper( root.right , find_val)
            else:
                return self.search_helper( root.left , find_val)
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))