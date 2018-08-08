class Node:

    def __init__(self):
        self.data = 0
        self.prev_node = None
        self.next_node = None

    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def __delete__(self, instance):
        del instance

    @property
    def get_data(self):
        return self.data

    @property
    def get_prev_node(self):
        return self.prev_node

    @property
    def get_next_node(self):
        return self.next_node
