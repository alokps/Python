from Node.Node import Node


class DoublyLinkList(Node):

    def __init__(self):
        self.root_node = Node(50, None, None)

    def insert_node(self, value=0):
        root = self.root_node
        while root.__getattribute__('next_node') is not None:
            root = root.__getattribute__('next_node')
        temp = Node(value)
        root.__setattr__('next_node', temp)
        temp.__setattr__('prev_node', root)

    def display_forward_nodes(self):
        temp = self.root_node
        result = []
        while temp.__getattribute__('next_node') is not None:
            result.append(temp.__getattribute__('data'))
            temp = temp.__getattribute__('next_node')
        result.append(temp.__getattribute__('data'))
        return result
