from LinkList.DoublyLinkList import DoublyLinkList
from LinkList.LinkList import LinkList


# class TestClass(object):
#
#     def test_singly_list(self):
#         instance1 = LinkList()
#         instance1.insert_node(20)
#         instance1.display_nodes()
#
#     def test_doubly_list(self):
#         instance2 = DoublyLinkList()
#         instance2.insert_node(60)
#         assert 50 in instance2.display_forward_nodes()


if __name__ == '__main__':
    instance2 = DoublyLinkList()
    instance2.insert_node(60)
    assert 50 in instance2.display_forward_nodes()