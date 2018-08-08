from Node.Node import Node


class CircularLinkList(Node):

    def __init__(self):
        self.root_node = Node(30)
        self._head = self.root_node
        self._tail = self.root_node

    def insert_node_at_front(self):
        pass

    def insert_node_at_rear(self, value):
        root = self.root_node
        while root.next_node != self._tail:
            root = root.next_node 
        temp = Node(value)
        self._tail = temp
        self._tail.next_node = self._head

    def display_nodes(self):
        root = self._head
        while root != self._tail:
            print(root.data)
            root = root.next_node
        print(root.data)
