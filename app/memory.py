# memory.py - Memory and history management module

class Memory:
    def __init__(self):
        self.history = []

    def add(self, result):
        self.history.append(result)

    def recall(self):
        if self.history:
            return self.history[-1]
        else:
            return None

    def clear(self):
        self.history.clear()
