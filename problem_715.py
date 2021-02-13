class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, value):
        self.size = 0
        self.head = Node(value)
        self.tail = self.head

    def add(self, value):
        node = Node(value)
        node.value = value

        temp_node = self.head
        for i in range(self.size):
            temp_node = temp_node.next

        temp_node.next = node
        node.prev = temp_node
        self.tail = node
        self.size += 1

    def peek(self):
        print(self.tail.value)

    def print_list(self):
        temp_node = self.head
        for i in range(self.size):
            print(temp_node.value)
            temp_node = temp_node.next
        print(temp_node.value)

    def is_palindrome(self):
        front = self.head
        back = self.tail
        # Should floor if decimal...
        for i in range(int(self.size / 1)):
            if front.value != back.value:
                return False
            front = front.next
            back = back.prev
        return True

def tester(numbers, expectation):
    try:
        ll = LinkedList(numbers[0])
    except IndexError:
        print(f"No linked list was created for {numbers}. Should be: {expectation}.")
        return

    for num in numbers[1:]:
        ll.add(num)

    print("Linked list has numbers:")
    ll.print_list()
    
    print(f"Is a palindrome: {ll.is_palindrome()}. Should be: {expectation}")

tester([1, 2, 3, 3, 2, 1], True)
tester([1, 2, 3, 2, 1], True)
tester([1, 2, 3, 1], False)
tester([], "N/a")
