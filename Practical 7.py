#1.Write a python program to create a linked list & display its elements
class Node:
    def __int__(self,data):
        self.data=data
        self.next=None

#Create Node
n1=Node(10)
n2=Node(20)
n3=Node(30)

#Connect Nodes
n1.next=n2
n2.next=n3

#Display Linked List
current=n1
while current:
    print(current.data)
    current=current.next

#Insert Node in Linked List
#Question : Insert a new node at the begining of a linked list.
class Node:
    def __int__(self,data):
        self.data=data
        self.next=None
head =Node(20)
head.next=Node(30)

#Insert new node
new_node=Node(10)
new_node.next=head
head=new_node

#Display
current= head
while current:
    print(current.data)
    current=current.next
#Insert Node at the End
class Node:
    def __int__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next=Node(20)
new_node=Node(30)
current = head
while current.next:
    current =current.next
current.next=new_node
current=head
while current:
    print(current.data)
    current = current.next

#Delete a node containing a given value
class Node:
    def __int__(self,data):
        self.data = data
        self.next=None
head = Node(10)
head.next=Node(20)
head.next.next=Node(30)

#delete 20
head.next=head.next.next
current= head
while current:
    print(current.data)
    current=current.next

#Search an Element in Linked List
class Node:
    def __int__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
search=int(input("Enter value to search :"))
current=head
found=False
while current:
    if current.data==search:
        found=True
        break
    current=current.next
if found:
    print("Element found")
else:
    print("Element not found")
    #practical7.2
#Stack
# 1. Stack Using List


stack = []
stack.append(10)
stack.append(20)
stack.append(30)


print("Stack:", stack)
print("Deleted:", stack.pop())
print("Stack after deletion:", stack)


# 2. Stack Using Menu
stack = []

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        stack.append(value)

    elif choice == 2:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Deleted:", stack.pop())

    elif choice == 3:
        print("Stack:", stack)

    elif choice == 4:
        break

    else:
        print("Invalid choice")


# 3. Stack Using Linked List
class Node:
   def __init__(self, data):
       self.data = data
       self.next = None
stack = None
# Push 10
new_node = Node(10)
new_node.next = stack
stack = new_node

# Push 20
new_node = Node(20)
new_node.next = stack
stack = new_node


# Display
current = stack


while current:
   print(current.data)
   current = current.next


#Queue


# 1. Queue Using List


queue = []


queue.append(10)
queue.append(20)
queue.append(30)
print("Queue:", queue)
print("Deleted:", queue.pop(0))
print("Queue after deletion:", queue)


# 2. Queue Using Menu


queue = []


while True:
   print("\n1. Insert")
   print("2. Delete")
   print("3. Display")
   print("4. Exit")


   choice = int(input("Enter choice: "))


   if choice == 1:
       value = int(input("Enter value: "))
       queue.append(value)


   elif choice == 2:
       if len(queue) == 0:
           print("Queue is empty")
       else:
           print("Deleted:", queue.pop(0))


   elif choice == 3:
       print("Queue:", queue)


   elif choice == 4:
       break


   else:
       print("Invalid choice")


# 3. Queue Using Linked List


from collections import deque


queue = deque()


queue.append(10)
queue.append(20)
queue.append(30)


print("Queue:", queue)


queue.popleft()


print("After deletion:", queue)


#Circular Queue
from collections import deque


queue = deque(maxlen=3)


queue.append(10)
queue.append(20)
queue.append(30)


print(queue)


queue.append(40)


print(queue)






#Binary tree


# 1. Create a Simple Binary Tree


class Node:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None




root = Node(10)


root.left = Node(20)
root.right = Node(30)


print("Root:", root.data)
print("Left:", root.left.data)
print("Right:", root.right.data)


# 2. Tree Traversal - Inorde
class Node:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None




def inorder(root):
   if root:
       inorder(root.left)
       print(root.data)
       inorder(root.right)




root = Node(10)


root.left = Node(20)
root.right = Node(30)


inorder(root)
