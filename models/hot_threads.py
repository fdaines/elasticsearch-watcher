class node:
    def __init__(self, name):
        self.name = name
        self.usages = []

    def add_usage(self, usage):
        self.usages.append(usage)
