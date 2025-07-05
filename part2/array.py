class Array:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)

    def delete(self, value):
        if value in self.data:
            self.data.remove(value)

    def access(self, index):
        return self.data[index] if index < len(self.data) else None
