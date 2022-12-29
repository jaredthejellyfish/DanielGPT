class Conversation:
    def __init__(self, limit=5):
        self.limit = limit
        self.messages = []

    def add(self, message):
        self.messages.append(message)
        self.autotrim()

    def pop(self):
        self.messages = self.messages[1:]

    def autotrim(self):
        if len(self.messages) >= self.limit:
            self.pop()

    def to_ctx(self):
        newline = "\n"
        return f"{newline.join(self.messages)}\nDaniel: "

    def __len__(self):
        return len(self.messages)

    def __str__(self):
        return "\n".join(self.messages)

    def __repr__(self):
        return self.__str__()
