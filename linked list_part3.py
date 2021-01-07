
"""
Creating a singly linked list of data points
with method for insert_at_begining, insert_at_end and insert_list
"""

class Node:
    def __init__(self, data, next1):
        self.data = data
        self.next1 = next1
        
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
            while itr.next1:
                itr = itr.next1
            
            itr.next1 = Node(data, None)
            
    def insert_list(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

            
    def print(self):
        if self.head is None:
            print('Empty Linked List')
        else:
            itr = self.head 
            llstr = ''
          
            while itr:
                llstr += str(itr.data) + '--->'
                itr = itr.next1          
            print(llstr)
          

          
if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_at_begining(1)
    l1.insert_at_begining(32)
    l1.insert_at_end(43)
    l1.insert_at_end(56)
    l1.print()  
    l1.insert_list(['text1', 'text2', 3, '4'])
    l1.print()           
    
    
#__________________________________________________________________

