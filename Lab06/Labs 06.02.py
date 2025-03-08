import json
class Student:
    def __init__(self, std_id, name, gpa):
        self.std_id = int(std_id)
        self.name = name
        self.gpa = float(gpa)
    
    def print_details(self):
        print(f"ID: {self.std_id}")
        print(f"Name: {self.name}")
        print(f"GPA: {self.gpa:.2f}")

class ProbHash:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size

    def hash(key, self):
        return key % self.size
    
    def rehash(hkey, self):
        return (hkey + 1) % self.size
    
    def insert_data(student, self):
        