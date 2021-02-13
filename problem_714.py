class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.size = 0
        self.head = Node(value)

    def add(self, value):
        node = Node(value)
        node.value = value

        temp_node = self.head
        for i in range(self.size):
            temp_node = temp_node.next

        temp_node.next = node
        self.size += 1

    def print_list(self):
        temp_node = self.head
        for i in range(self.size):
            print(temp_node.value)
            temp_node = temp_node.next
        print(temp_node.value)

    def swap_every_other(self):
        temp_node = self.head
        for i in range(0, self.size, 2):
            v1 = temp_node.value
            v2 = temp_node.next.value
            temp_node.value = v2
            temp_node.next.value = v1
            temp_node = temp_node.next.next

def tester(numbers, expectation):
    try:
        ll = LinkedList(numbers[0])
    except IndexError:
        print(f"No linked list was created for {numbers}. Expectation: {expectation}.")
        return

    for num in numbers[1:]:
        ll.add(num)

    print("Linked list has numbers:")
    ll.print_list()

    print("Swapping every other element:")
    ll.swap_every_other()
    ll.print_list()
    
    print(f"Should be: {expectation}")

tester([1, 2, 3, 4], [2, 1, 4, 3])

tester([], [])

tester([1], [1])

tester([1, 2], [2, 1])

tester([1, 2, 3], [2, 1, 3])

tester([1, 2, 3, 4, 5], [2, 1, 4, 3, 5])
