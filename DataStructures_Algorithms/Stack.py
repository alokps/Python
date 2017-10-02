
class Stack:

    def __init__(self):
        self.stack_list = []

    @property
    def is_empty(self):
        return self.stack_list == []

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        self.stack_list.pop()

    @property
    def stack_length(self):
        return len(self.stack_list)

    @property
    def stack_top(self):
        return self.stack_list[0]
