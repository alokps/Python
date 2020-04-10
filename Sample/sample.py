
class Sample(object):

    def __init__(self):
        self._stack_list = list()

    def push_value(self, value):
        self._stack_list.append(value)

    def is_empty(self):
        return self._stack_list == []

    def pop_value(self):
        return self._stack_list.pop()

    def print_stack_value(self):
        for x in self._stack_list:
            print(x)


if __name__ == '__main__':
    instance = Sample()
    print(instance.is_empty())
    instance.push_value(10)
    instance.push_value(20)
    instance.push_value(30)
    print(instance.pop_value())
    instance.print_stack_value()
