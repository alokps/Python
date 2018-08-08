from Node.Node import Node


class LinkList(Node):

    def __init__(self):
        self.root_node = Node(10, None, None)
        self.counter = 1

    def insert_node_at_rear(self, value=0):
        temp = self.root_node
        while temp.get_next_node is not None:
            temp = temp.__getattribute__('next_node')
        temp.__setattr__('next_node', Node(value))
        self.counter += 1

    def remove_from_rear(self):
        temp = self.root_node

        while temp.get_next_node.get_next_node is not None:
            temp = temp.get_next_node

        temp.__delete__(temp.get_next_node)
        temp.__setattr__('next_node', None)

    def insert_node_at_front(self, value=0):
        temp = Node(value)
        temp.next_node = self.root_node
        self.root_node = temp
        self.counter += 1

    def remove_from_front(self):
        temp = self.root_node
        self.root_node = self.root_node.get_next_node
        del temp

    def insert_node_at_index(self, index, value=0):
        temp = 0
        temp_node = self.root_node
        if index >= self.counter:
            raise ValueError("Incorrect Index value")

        while temp != (index - 1):
            temp_node = temp_node.get_next_node
            temp += 1

        new_node = Node(value)
        new_node.next_node = temp_node.get_next_node
        temp_node.__setattr__('next_node', new_node)
        self.counter += 1

    def display_nodes(self):
        temp = self.root_node
        while temp.__getattribute__('next_node') is not None:
            print("The Value of Node is {}".format(temp.__getattribute__(
                'data')))
            temp = temp.__getattribute__('next_node')
        print("The Value of Node is {}".format(temp.__getattribute__(
            'data')))
