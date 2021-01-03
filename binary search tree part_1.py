"""
Binary Search Tree with insert, in order, pre order, post order traversal,
search, find_min and find_max methods
"""
class BSTNode:
    def __init__(self, data): # at max 2 children
        self.data = data
        self.left = None
        self.right = None
        
    def insert_data(self, data):
        if data == self.data:
            return # No duplicate allowed
        if data < self.data: # add in left sub-tree
            if self.left:
                self.left.insert_data(data)
            else:
                self.left = BSTNode(data)
        if data > self.data: # add in right sub-tree
            if self.right:
                self.right.insert_data(data)
            else:
                self.right = BSTNode(data)
                
    def in_order_traversal(self): #left, base node, right
        elements = []
        
        if self.left:
            elements += self.left.in_order_traversal()
                
        elements.append(self.data)
        
        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
    
    def post_order_traversal(self): # left, right, base node
        elements = []
        
        if self.left:
            elements += self.left.post_order_traversal()
        
        if self.right:
            elements += self.right.post_order_traversal()
            
        elements.append(self.data)
        
        return elements
    
    def pre_order_traversal(self): # Base Node, left subtree, right subtree
        elements = [self.data]
        
        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
    
    def search(self, value):
        if value == self.data:
            print("Value is found")
        
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                print("Value is not found")
                
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                print("Value is not found")
                
    def find_max(self):
        if self.right == None:
            max = self.data
        else:
            return self.right.find_max()
            
        return max
    
    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()
            
            
    
def buildTree(elements):
    '''
    Parameters
    ----------
    elements : iterable such as list/tuple
        DESCRIPTION: Takes first element of the list as root node and add children using BST 

    Returns
    -------
    root : Binary Search Tree Node Object
    '''
    print("building tree with elements: ", elements)
    root = BSTNode(elements[0])
    
    for i in range(1, len(elements)):
        root.insert_data(elements[i])
        
    return root


if __name__ == '__main__':
    
    # Example_1
    lst = [10, 22, 14, 20, 25, 30, 16, 16, 30]
    num_tree = buildTree(lst)
    print("In Order Traversal: ", num_tree.in_order_traversal())
    print("\n", "Post Order Traversal: ", num_tree.post_order_traversal())
    print("\n", "Pre Order Traversal: ", num_tree.pre_order_traversal())
    # Verify Here: https://yongdanielliang.github.io/animation/web/BST.html
    num_tree.search(20)
    num_tree.search(-10)
    print(num_tree.find_max())
    print(num_tree.find_min())
    
    #Example_2
    # my_courses = ["R", "Python", "Machine Learning", "Statistics", "Excel"]
    # course_tree = buildTree(my_courses)
    # print(course_tree.in_order_traversal())
    # course_tree.search("Machine Learning")
    # course_tree.search("Big Data")
            
