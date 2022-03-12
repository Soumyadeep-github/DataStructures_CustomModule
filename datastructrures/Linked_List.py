from collections.abc import Iterable


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, args=None):
        self.head = None
        if isinstance(args, LinkedList):
            print("Already of type LinkedList. Try different methods to get the data.")
        elif not (isinstance(args, Iterable)) and args is not None:
            self.insert_head(args)
        elif isinstance(args, Iterable):
            if isinstance(args, LinkedList):
                print("Already of type LinkedList. Try different methods to get the data.")
            elif not (isinstance(args, LinkedList)):
                self.__insert_values__(args)

    def __repr__(self, l_list=None):
        if l_list is None:
            item = self.head
            linked_list_str_repr = 'None-->'
            while item.next:
                linked_list_str_repr += str(item.data) + '-->'
                item = item.next
            else:
                linked_list_str_repr += 'None'

            return linked_list_str_repr
        # elif isinstance(l_list, LinkedList):
        #     return l_list.get_elements(index=l_list.get_length()-1, whole=True)

    def __eq__(self, other):
        count = 0
        if isinstance(other, LinkedList) and self.get_length() == other.get_length():
            item_other = other.head
            item_self = self.head
            while item_other and item_self:
                if item_other == item_self:
                    count += 1
                item_other = item_other.next
                item_self = item_self.next
            else:
                return False
        if count == other.get_length() == self.get_length():
            return True
        return False

    def __len__(self):
        return self.get_length()

    def insert_recursive(self, iterable):
        if len(iterable) == 1:
            self.insert_head(iterable[0])
        else:
            mid = len(iterable) // 2
            self.insert_recursive(iterable[:mid])
            self.insert_recursive(iterable[mid:])

    def insert_head(self, data):
        self.head = Node(data, self.head)  # data argument becomes the new head and the existing head is shifted

    def insert(self, data, index=None):
        if index is None:
            if not self.head:  # If there is no head or if the list is empty, then add the data element
                self.head = Node(data)  # Since there is no next, it stays None

            item = self.head
            while item.next is not None:  # Adding data at the end of the linked list
                item = item.next
            else:
                item.next = Node(data)

        elif index is not None:
            if index < 0 or index >= self.get_length():
                raise Exception("Index {index} is out of range. Please enter a valid input".format(index=index))

            if index == 0:
                # Head is always at none so none is pointing to the first value right after head or head.next
                self.insert_head(data)
                return
            else:
                count = 0
                item = self.head
                while item:
                    # We need to add an element at the index specified.
                    # So we need to link the previous element (at index-1) to the new element
                    # we are inserting at index, and the this new element should point to the
                    # element right after the index (at index+1).
                    if count == index - 1:
                        new_node = Node(data, item.next)
                        item.next = new_node
                        break
                    item = item.next
                    count += 1

    def __insert_values__(self, iterable):
        self.head = None
        for x in iterable:
            self.insert(x)

    def get_elements(self, index=None, whole=False):
        """ Using this method one can traverse the whole list
            or elements upto the defined index (whole==True)
            or just the element at the defined index."""
        if whole:
            if index is None:
                if self.head is None:
                    print("Linked List is empty.")
                    return

                item = self.head
                item_str = 'HEAD-->'
                while item:
                    item_str += str(item.data) + '-->'
                    item = item.next
                else:
                    item_str += 'END'
            else:
                if index < 0 or index >= self.get_length():
                    raise Exception("Index {index} is out of range. Please enter a valid input".format(index=index))

                if index == 0:
                    # Head is always at none so none is pointing to the first value right after head or head.next
                    return self.head.next
                else:
                    count = 0
                    item = self.head
                    item_str = 'HEAD-->'
                    while item:
                        item_str += str(item.data) + '-->'
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
            item_str = 'HEAD-->'
            while item:
                item_str += str(item.data) + '-->'
                item = item.next
                if index == count:
                    return item.data
                count += 1

        return item_str

    def get_length(self):
        count = 0
        item = self.head
        while item.next:
            count += 1
            item = item.next
        return count

    def remove(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Index {index} is out of range. Please enter a valid input".format(index=index))

        if index == 0:
            # Head is always at none so none is pointing to the first value right after head or head.next
            self.head = self.head.next
            return
        else:
            count = 0
            item = self.head
            while item:
                # We need to delete the element present at the index specified.
                # So we need to link the previous element (at index-1) to the element
                # right after the index (at index+1).
                if count == index - 1:
                    item.next = item.next.next
                    # This could also be written as
                    # current_item_link = item.next #this gives the data item at index
                    # next_data_item = current_item_link.next #this will yield the data item at index+1
                    # item.next = next_data_item #now the current item points to the data at index+1
                    break
                item = item.next
                count += 1


if __name__ == '__main__':
    print("Simple Linked List from a list. ")
    ll = LinkedList()
    data_list = [50, 40, 60, 100, 200, 250, 20, 30, 400]
    for i in data_list:
        ll.insert_head(i)
    ll.insert(700)
    print("Input data :\n{}".format(data_list))
    print("This is how the Linked List would look like (conceptually): \n{}".format(ll.get_elements()))
    print('---------------------------------------------------------------')
    print("Type casting a list to a LinkedList: ")
    l_ = LinkedList(data_list)
    l_.get_length()
    print("\nInput data :\n{}".format(data_list))
    print("\nThis is how the Linked List would look like (conceptually): \n{}".format(l_.get_elements()))
    print("\nGet the length of a Linked List like this: \nlinked_list = LinkedList("
          "input_data_list)\nlinked_list.get_length()\n>>>{get_length}\nOR"
          "\nlen(linked_list)\n>>>{_len}".format(get_length=l_.get_length(), _len=len(l_)))
    print("Using the repr method to show the Linked List elements : \n{}".format(l_))
    print("\nElement at position 3 is {}.".format(l_.get_elements(2)))
    print('---------------------------------------------------------------')
    print("Use a Linked List of strings:")
    ll_string = LinkedList()
    data_list_string = ["Mango", "Apple", "Orange", "Banana", "Cucumber", "Grapes", "Pomegranate", "Avocado"]
    print("\nInput data :\n{}".format(data_list_string))
    ll_string.__insert_values__(data_list_string)
    print("\nLinked List from the above list looks like this:")
    print(ll_string)
    print("\nRemove an element at index 5 or 'Grapes' for example:")
    ll_string.remove(5)
    print(ll_string)
    print("\nAdd an element at index 5 -> 'Raisin' for example:")
    ll_string.insert(data="Raisin", index=5)
    print(ll_string)
    print(ll_string.get_elements(4))
    # print(LinkedList(data_list) == LinkedList(data_list))
    print(isinstance(ll_string, LinkedList))
    # LinkedList(args=ll_string)
    print(LinkedList(data_list) is l_)
