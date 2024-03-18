from multiprocessing.dummy import Value


class Value:
    def __init__(self, data):
        self.data = data

    def __repr__ (self):
        return f'{self.__dict__}'

    def __str__(self):
        return f'Værdien af data er: {self.__dict__}'



