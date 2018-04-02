import sys


class ExtendedList():
    def __init__(self, elems=None):
        if elems is None:
            elems = []
        self.list = elems

    def __eq__(self, other):
        return self.list == other

    def __iter__(self):
        return self.list.__iter__()

    def __contains__(self, item):
        return self.list.__contains__(item)

    def __setitem__(self, key, value):
        self.list.__setitem__(key, value)

    def __getitem__(self, item):
        return self.list[item]

    def __len__(self):
        return self.list.__len__()

    def __str__(self):
        return str(self.list)

    def append(self, elem):
        self.list.append(elem)

    def extend(self, lst):
        if type(lst) is list:
            self.list.extend(lst)
        if type(lst) is ExtendedList:
            self.list.extend(lst.list)

    def insert(self, ind, val):
        self.list.insert(ind, val)

    def remove(self, x):
        self.list.remove(x)

    def pop(self, i):
        return self.list.pop(i)

    def index(self, x):
        return self.list.index(x)

    def count(self, x):
        return self.list.count(x)

    def sort(self):
        return self.list.sort()

    def clear(self):
        return self.list.clear()

    @property
    def reversed(self):
        return self.list[::-1]

    @property
    def R(self):
        return self.list[::-1]

    @property
    def F(self):
        return self.list[0]

    @F.setter
    def F(self, value):
        self.list[0] = value

    @property
    def first(self):
        return self.list[0]

    @first.setter
    def first(self, value):
        self.list[0] = value

    @property
    def last(self):
        return self.list[-1]

    @last.setter
    def last(self, value):
        self.list[-1] = value

    @property
    def L(self):
        return self.list[-1]

    @L.setter
    def L(self, value):
        self.list[-1] = value

    @property
    def size(self):
        return len(self.list)

    @property
    def S(self):
        return len(self.list)

    @S.setter
    def S(self, value):
        if value < len(self.list):
            self.list = self.list[0:value]
        elif value > len(self.list):
            for i in range(len(value - self.list)):
                self.list.append(None)

    @size.setter
    def size(self, value):
        if value < len(self.list):
            self.list = self.list[0:value]
        elif value > len(self.list):
            for i in range(len(value - self.list)):
                self.list.append(None)


if __name__ == '__main__':
    exec(sys.stdin.read())
