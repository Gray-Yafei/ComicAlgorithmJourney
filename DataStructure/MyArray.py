class MyArray():
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1

    def insert_v2(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if self.size >= len(self.array):
            self.resize()
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1

    def resize(self):
        array_new = [None] * len(self.array) * 2
        for i in range(len(self.array)):
            array_new[i] = self.array[i]
        self.array = array_new

    def output(self):
        for i in range(self.size):
            print(self.array[i])

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1


if __name__ == "__main__":
    array = MyArray(3)
    array.insert_v2(0, 9)
    array.insert_v2(0, 8)
    array.insert(0, 9)
    array.insert_v2(0, 9)

    array.output()
    print("push test!")