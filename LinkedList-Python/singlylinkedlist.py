class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def traverse(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def findmintraverse(head):
    current = head
    min_value = current.data
    while current is not None:
        if min_value > current.data:
            min_value = current.data
        current = current.next
    return min_value

def insertafter(head,data,after_node):
    new_node = Node(data)
    
    while head is not None:
        if head.data == after_node:
            new_node.next = head.next
            head.next = new_node
            return "successfully inserted"
        head = head.next

def deleteafter(head,after_node):
    current = head
    while current is not None:
        if current.data == after_node and current.next is not None:
            current.next = current.next.next
            return "successfully deleted"
        current = current.next

def delete_node(head, data):
    if head is None:
        return None
    if head.data == data:
        return head.next
    current = head
    while current.next is not None:
        if current.next.data == data:
            current.next = current.next.next
            return head
        current = current.next
    return head

def insertatbeginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node


node = Node(1)
node.next = Node(2)
node.next.next = Node(3)


traverse(node)
print("Minimum value in the list:", findmintraverse(node))

print("Inserting 4 after 2:",insertafter(node, 4, 2))
traverse(node)
print("Deleting node after 2:", deleteafter(node, 2))
traverse(node)
print("Inserting 0 at the beginning:")
node = insertatbeginning(node, 0)
traverse(node)