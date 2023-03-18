class reverse_iter:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            i = self.lst[self.index]
            return i
        else:
            raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
