"""
Tree Data Structure for website [A tree of height 3]
"""
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    
    
    def print_tree(self):
        # print("Level: " + str(self.get_level()))
        space = ' '* self.get_level()*5
        prefix = space + str(self.get_level()) + "|--->"
        print(prefix + self.data)        
        if self.children:
            for child in self.children:
                child.print_tree()
        
        
def website_tree():
    root = TreeNode("Learner's World")
    
    home = TreeNode("Home")
    root.add_child(home)
    
            
    my_courses = TreeNode("My Courses")
    
    self_paced =  TreeNode("Self-Paced")
    my_courses.add_child(self_paced)
    
    self_paced.add_child(TreeNode("Statistics for Data Science"))
    self_paced.add_child(TreeNode("R for Data Science"))
    
        
    online = TreeNode("Live Online Course")
    my_courses.add_child(online)

    online.add_child(TreeNode("Statistics for Data Science"))
    online.add_child(TreeNode("Excel for Analytics"))    
    online.add_child(TreeNode("Python for Data Science"))
    online.add_child(TreeNode("Machine Learning Fundamentals"))
    
    root.add_child(my_courses)
    root.print_tree()

if __name__ == '__main__':
    website_tree()

