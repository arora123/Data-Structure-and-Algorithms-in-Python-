"""
Creating a singly linked list of data points
having methods for insert_at_begining and insert_at_end
"""

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
class LinkedList:       
    def __init__(self):
        self.head = None
         
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
          
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            
            itr.next = Node(data, None)
            
            
    def print(self):
        if self.head is None:
            print('Empty Linked List')
        else:
            itr = self.head 
            llstr = ''
          
            while itr:
                llstr += str(itr.data) + '--->'
                itr = itr.next          
            print(llstr)
          

          
if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_at_begining(1)
    l1.insert_at_begining(32)
    l1.insert_at_end(43)
    l1.insert_at_end(56)
    l1.print()          
    
# Either use print statement to see the values or use debugger
# Use debugger to watch the steps & print value of l1.head.data and  
# l1.head.next.data 

#__________________________________________________________________

