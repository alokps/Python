
class Sample:

    def __init__(self):
        self.stack_list = []

    def push_value(self, value):
        self.stack_list.append(value)

    def is_empty(self):
        return self.stack_list == []

    def pop_value(self):
        return self.stack_list.pop()

    def print_stack_value(self):
        for x in self.stack_list:
            print(x)


if __name__ == '__main__':
    instance = Sample()
    print(instance.is_empty())
    instance.push_value(10)
    instance.push_value(20)
    instance.push_value(30)
    print(instance.pop_value())
    instance.print_stack_value()
