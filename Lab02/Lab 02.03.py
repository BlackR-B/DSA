class ArrayStack:
    def __init__(self):
        self.size = 0
        self.data = list()

    def push(self, input_data):
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        if self.data:
            last = self.data.pop()
            self.size -= 1
            return last
        else:
            print("Underflow: Cannot pop data from an empty list")
            return None

    def is_empty(self):
        return not bool(self.data)

    def get_stack_top(self):
        if self.data:
            top_element = self.data.pop()
            self.data.append(top_element)
            return top_element
        else:
            print("Underflow: Cannot get stack top from an empty list")
            return None

    def get_size(self):
        return len(self.data)

    def print_stack(self):
        print(self.data)

    def copy_stack(self, target):
        target.data = self.data.copy()
        target.size = self.size

def print_status():
    print("This is stack 1 (%d): " % STACK1_.get_size(), end='')
    STACK1_.print_stack()
    print("This is stack 2 (%d): " % STACK2_.get_size(), end='')
    STACK2_.print_stack()
    print("This is stack 3 (%d): " % STACK3_.get_size(), end='')
    STACK3_.print_stack()
    print("This is stack 4 (%d): " % STACK4_.get_size(), end='')
    STACK4_.print_stack()
    print()

STACK1_ = ArrayStack()
STACK2_ = ArrayStack()
STACK3_ = ArrayStack()
STACK4_ = ArrayStack()

for _ in range(int(input())):
    STACK1_.push(input())

for _ in range(int(input())):
    STACK2_.push(input())

TEMP1_, TEMP2_, TEMP3_, TEMP4_ = id(STACK1_), id(STACK2_), id(STACK3_), id(STACK4_)

print("Copy Stack 2 to Stack 4")
STACK2_.copy_stack(STACK4_)
print_status()

print("Copy Stack 1 to Stack 3")
STACK1_.copy_stack(STACK3_)
STACK1_.push("A")
print_status()

print("Copy Stack 2 to Stack 1")
STACK2_.copy_stack(STACK1_)
STACK2_.push("B")
print_status()

print("Copy Stack 3 to Stack 2")
STACK3_.copy_stack(STACK2_)
STACK3_.push("C")
print("Copy Stack 1 to Stack 3")
STACK1_.copy_stack(STACK3_)
STACK1_.push("D")
print("Copy Stack 2 to Stack 4")
STACK2_.copy_stack(STACK4_)
STACK2_.push("E")
print_status()

print(TEMP1_ == id(STACK1_), TEMP2_ == id(STACK2_), TEMP3_ == id(STACK3_), TEMP4_ == id(STACK4_))