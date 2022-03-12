from collections.abc import Iterable


class Node:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

    def __repr__(self):
        return self.data


class DoublyLinkedList:
    def __init__(self, args=None):
        self.head = None
        if isinstance(args, DoublyLinkedList):
            print("Already of type LinkedList. Try different methods to get the data.")
        elif not (isinstance(args, Iterable)) and args is not None:
            self.append(args)
        elif isinstance(args, Iterable):
            if isinstance(args, DoublyLinkedList):
                print("Already of type LinkedList. Try different methods to get the data.")
            elif not (isinstance(args, DoublyLinkedList)):
                self.__insert_values__(args)

    def __repr__(self):
        curr_node = self.head
        linked_list_str_repr = 'None<==>'
        while curr_node.next:
            linked_list_str_repr += str(curr_node.data) + '<==>'
            curr_node = curr_node.next
        else:
            linked_list_str_repr += 'None'
        return linked_list_str_repr

    def __len__(self):
        return self.get_length()

    # def insert_head(self, data):
    #     self.head = Node(data, next=self.head)

    def insert(self, data, index=None):
        if index is None:
            if self.head is None:  # If there is no head or if the list is empty, then add the data element
                self.head = Node(data)  # Since there is no next, it stays None

            curr_node = self.head
            while curr_node.next:  # Adding data at the end of the linked list
                curr_node = curr_node.next
            else:
                curr_node.next = Node(data, previous=curr_node)

        elif index is not None:
            if 0 > index >= self.get_length():
                raise Exception("Index {index} is out of range. Please enter a valid input".format(index=index))

            if index == 0:
                # Head is always at none so none is pointing to the first value right after head or head.next
                self.append(data)
                return
            else:
                count = 0
                curr_node = self.head
                while curr_node.next:
                    # We need to add an element at the index specified.
                    # So we need to link the previous element (at index-1) to the new element
                    # we are inserting at index, and the this new element should point to the
                    # element right after the index (at index+1).
                    if count == index - 1:
                        new_node = Node(data, next=curr_node.next, previous=curr_node)
                        curr_node.next = new_node
                        break
                    curr_node = curr_node.next
                    count += 1

    def __insert_values__(self, iterable):
        self.head = None
        for x in iterable:
            self.insert(x)

    def append(self, data):

        # check if head is none or if the list is empty
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data=data)
            # Current node starts from head
            curr_node = self.head
            while curr_node.next:  # While Current_node is not null
                curr_node = curr_node.next
            else:  # While current_node is null, i.e, the end of the list then
                curr_node.next = new_node  # point the last/current node to the new one
                new_node.previous = curr_node  # point the previous link of the new one to the current

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data, next=self.head)  # initialise the node so that next points to head
            self.head.previous = new_node  # head's previous link was to none which needs to change to the new node
            self.head = new_node  # the new head should be the new node

    def get_length(self):
        count = 0
        item = self.head
        while item.next:
            count += 1
            item = item.next
        return count

    def remove(self, index):
        if 0 > index >= self.get_length():
            raise Exception("Index {index} is out of range. Please enter a valid input".format(index=index))

        if index == 0:
            # Head is always at none so none is pointing to the first value right after head or head.next
            self.head.next.previous = None
            self.head = self.head.next
            return
        else:
            count = 0
            curr_node = self.head
            while curr_node.next:
                # We need to delete the element present at the index specified.
                # So we need to link the previous element (at index-1) to the element
                # right after the index (at index+1).
                if count == index - 1:
                    curr_node.next = curr_node.next.next
                    curr_node.next.previous = curr_node
                    # This could also be written as
                    # current_item_link = item.next #this gives the data item at index
                    # next_data_item = current_item_link.next #this will yield the data item at index+1
                    # item.next = next_data_item #now the current item points to the data at index+1
                    break
                curr_node = curr_node.next
                count += 1

    def get_elements(self, index=None, whole=False):
        """ Using this method one can traverse the whole list
            or elements upto the defined index (whole==True)
            or just the element at the defined index."""
        if whole:
            if index is None:
                if self.head is None:
                    print("Linked List is empty.")
                    return

                curr_node = self.head
                item_str = 'None(HEAD)<==>'
                while curr_node:
                    item_str += str(curr_node.data) + '<==>'
                    curr_node = curr_node.next
                else:
                    item_str += 'None'

            else:
                if 0 > index >= self.get_length():
                    raise Exception("Index {index} is out of range. Please enter a valid input".format(index=index))

                if index == 0:
                    # Head is always at none so none is pointing to the first value right after head or head.next
                    return self.head.next
                else:
                    count = 0
                    item = self.head
                    item_str = 'None(HEAD)<==>'
                    while item:
                        item_str += str(item.data) + '==>'
                        item = item.next
                        if index == count:
                            item_str += "NEXT_INDEX({})".format(index + 1)
                            break
                        count += 1
                    else:
                        item_str += 'END'
        else:
            count = 0
            item = self.head
            item_str = 'None(HEAD)<==>'
            while item:
                item_str += str(item.data) + '<==>'
                item = item.next
                if index == count:
                    return item.data
                count += 1

        return item_str


if __name__ == "__main__":
    print("Simple Linked List from a list. ")
    ll = DoublyLinkedList()
    data_list = [50, 40, 60, 100, 200, 250, 20, 30, 400]
    for i in data_list:
        ll.append(i)
    data_list_1 = [10, 20, 30, 40]
    for i in data_list_1:
        ll.prepend(i)
    print(ll.get_elements(whole=True))
    l1 = DoublyLinkedList(data_list_1)
    print(ll.get_elements(whole=True))
    print(l1)