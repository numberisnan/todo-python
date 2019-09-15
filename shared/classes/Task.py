class Task:
    def __init__(self, name, description, **kwargs):
        self.name = name
        self.description = description

        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __int__(self):
        return self.p

    def __lt__(self, other):
        return self.p < other.p
