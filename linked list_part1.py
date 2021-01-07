'''
Creating a singly linked list of 
muliple data points such as employee name, age, etc.
'''

class Employee:
    def __init__(self, name, age, next):
        self.name = name
        self.age = age
        self.next = next
        
class LinkedList:       
    def __init__(self):
        self.head = None
         
    def insert_at_begining(self, name, age):
        node = Employee(name, age, self.head)
        self.head = node
          
    def print(self):
        if self.head is None:
            print('Empty Linked List')
        else:
            itr = self.head 
            llstr = ''
          
            while itr:
                llstr += 'Name: ' + str(itr.name)+' & age:'+ str(itr.age) + '--->'
                # +str(itr.next)
                itr = itr.next          
            print(llstr)
          

          
if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_at_begining('Prakhar', 32)
    l1.insert_at_begining(age=35, name='girish')
    l1.insert_at_begining(36, 'Naomi')
    l1.insert_at_begining('Pragya',24)
    
    l1.print()  