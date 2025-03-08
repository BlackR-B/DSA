class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.history = None

    def add_history(self, action, item):
        new_node = Node((action, item))
        if self.history is None:
            self.history = new_node
        else:
            current = self.history
            while current.next is not None:
                current = current.next
            current.next = new_node

    def pop_history(self):
        if self.history is None:
            return None
        if self.history.next is None:
            last_action = self.history.data
            self.history = None
            return last_action
        current = self.history
        while current.next.next is not None:
            current = current.next
        last_action = current.next.data
        current.next = None
        return last_action

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.add_history("enqueue", item)

    def dequeue(self):
        if self.front is None:
            print("Underflow! Dequeue from an empty queue")
            return None
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.add_history("dequeue", item)
        print(f"Dequeue item: {item.show_info()}")
        return item

    def peek(self):
        if self.front is None:
            print("Underflow! peek from an empty queue")
            return None
        return self.front.data

    def isEmpty(self):
        return self.front is None

    def show_Queue(self):
        if self.isEmpty():
            print("Queue is empty!")
            return
        current = self.front
        index = 1
        while current:
            print(f"Queue#{index} {current.data.show_info()}")
            current = current.next
            index += 1

    def lastSong(self, time):
        if self.isEmpty():
            print("Nothing here! Please add some song")
            return
        current = self.front
        total_time = 0
        while current:
            total_time += current.data.duration
            current = current.next
        time %= total_time

        current = self.front
        while current:
            if time < current.data.duration:
                print(f"Last song: {current.data.show_info()}")
                return
            time -= current.data.duration
            current = current.next

    def removeSong(self, name):
        if self.isEmpty():
            print(f"Can not Delete! {name} is not exist")
            return
        dummy = Node(None)
        dummy.next = self.front
        prev, current = dummy, self.front

        while current:
            if current.data.name == name:
                prev.next = current.next
                if current == self.rear:
                    self.rear = prev
                self.front = dummy.next
                self.add_history("remove", current.data)
                print(f"Deleted: {name}")
                return
            prev, current = current, current.next
        print(f"Can not Delete! {name} is not exist")

    def groupSong(self):
        if self.isEmpty():
            print("Queue is empty!")
            return
        groups = {"JPOP": None, "KPOP": None, "R&B": None}
        current = self.front
        while current:
            genre = current.data.genre
            if genre in groups:
                if groups[genre] is None:
                    groups[genre] = Node(current.data.name)
                else:
                    temp = groups[genre]
                    while temp.next is not None:
                        temp = temp.next
                    temp.next = Node(current.data.name)
            current = current.next
        for genre, songs in groups.items():
            if songs is None:
                print(f"{genre}: ...")
            else:
                result = []
                current = songs
                while current:
                    result.append(current.data)
                    current = current.next
                print(f"{genre}: {' | '.join(result)}")

    def undo(self):
        last_action = self.pop_history()
        if last_action is None:
            print("Nothing to undo!")
            return
        action, item = last_action

        if action == "enqueue":
            self.dequeue()
        elif action == "dequeue":
            self.enqueue(item)
        elif action == "remove":
            self.enqueue(item)

    def rev_queue(self):
        if self.isEmpty():
            return
        prev, current = None, self.front
        self.rear = self.front
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.front = prev

class Song:
    def __init__(self, name, genre, duration):
        self.name = name
        self.genre = genre
        self.duration = duration

    def show_info(self):
        minutes, seconds = divmod(self.duration, 60)
        return f"{self.name} <|> {self.genre} <|> {minutes}.{seconds:02}"

def add_songs_to_queue(queue):
    while True:
        print("\nEnter song details (or type 'done' to finish):")
        name = input("Song name: ")
        if name.lower() == 'done':
            break
        genre = input("Genre: ")
        try:
            duration = int(input("Duration (in seconds): "))
        except ValueError:
            print("Invalid input for duration. Please enter an integer.")
            continue

        song = Song(name, genre, duration)
        queue.enqueue(song)
        print(f"Added: {song.show_info()}")

q = Queue()
add_songs_to_queue(q)
q.show_Queue()
