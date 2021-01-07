# Data-Structure-and-Algorithms-in-Python-
This Repository contains codes for Data Structure and Algorithms implementation in Python with some interesting use cases and exercises inspired by codebasics 

linked list part1.py 

Creating a singly linked list of muliple data points such as employee name, age, etc.

linked list part2.py

Creating a singly linked list of data points having methods for insert_at_begining and 

linked list part3.py

Creating a singly linked list of data points with method for insert_at_begining, insert_at_end and insert_list


tree data structure part_1.py

1. Create a general Tree for a website with methods for
	--> Insert/add_child
	--> get_level for preety printing
	--> print_tree for printing complete tree
	--> print tree upto a certain level


tree data structure part_2.py

1. Create a general Tree for an organization chart with two atrributes/inputs (name & designation) and methods for
	--> Insert/add_child
	--> get_level for pretty printing
	--> print_tree for printing complete tree
	--> print tree upto a certain level
	--> level order traversal a certain level
	
	
binary serach tree part_1.py

1. Create a Binary Search Tree with methods for
	--> Insert method
	--> In-Order, Pre-Order and Post-Order Reversal
	--> Search method
	--> Find Max and Find Min Functions

2. For the list of elements [10, 22, 14, 20, 25, 30, 16, 16, 30], create a binary search tree and answer the following.
	--> In Order Traversal of elements
	--> Pre Order Traversal of elements
	--> Post Order Traversal of elements
	--> Verify your answers by using simulations here: https://yongdanielliang.github.io/animation/web/BST.html
	--> Maximum number from the abouve list
	--> Minimum number from the above list

3. In the list of courses ["R", "Python", "Machine Learning", "Statistics", "Excel"], search for "Machine Learning" and "Big Data" using binary search tree

binary search tree part2.py
Added a method to delete element from tree data structure

 Three posssibilities:
	--> 1. if the value to be deleted is a leaf node [node with no child]
		Then you need to delete left/right subtree of it's (own) parent
	--> 2. if the value to be deleted is a node with only one child
		Then you need to delete the node and replace it with it's child
	--> 3. if the value to be deleted has two children [it's tricky]
		Then 
		   a) find a right subtree and find it's minimun value
		     copy it's value to that node (which is to be deleted) and remove duplicate
or
		   b) find maximum from left subtree andd copy it's value to that node and remove duplicate





