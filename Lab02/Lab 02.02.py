class Stack:
    def __init__(self):
        self.top = None

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def push(self, item):
        new_node = self.Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_item = self.top.data
        self.top = self.top.next
        return popped_item

    def is_empty(self):
        return self.top is None

class GroupStackNode:
    def __init__(self, stack=None):
        self.stack = stack
        self.next = None

def distribute_students_to_groups():
    m = int(input())
    n = int(input())
    students = Stack()

    for _ in range(n):
        students.push(input())

    group_head = None
    group_tail = None
    for _ in range(m):
        new_group = GroupStackNode(Stack())
        if group_head is None:
            group_head = new_group
            group_tail = new_group
        else:
            group_tail.next = new_group
            group_tail = new_group

    current_group = group_head
    while not students.is_empty():
        current_group.stack.push(students.pop())
        if current_group.next is None:
            current_group = group_head
        else:
            current_group = current_group.next

    current_group = group_head
    group_number = 1
    while current_group is not None:
        print(f"Group {group_number}:", end=" ")
        temp_stack = Stack()
        while not current_group.stack.is_empty():
            temp_stack.push(current_group.stack.pop())
        first = True
        while not temp_stack.is_empty():
            if not first:
                print(",", end=" ")
            print(temp_stack.pop(), end="")
            first = False
        print()
        current_group = current_group.next
        group_number += 1

distribute_students_to_groups()
