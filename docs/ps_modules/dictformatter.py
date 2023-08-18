__all__ = "DictFormatter"

class DictFormatter:

    __slots__ = ('info',)

    def __init__(self):
        self.info = {}

    def add(self, course, homepage):
        self.info[course] = homepage

    def format(self, spec):
        return self.info[spec]
    __mod__ = format

    def __getstate__(self):
        return self.info

    def __setstate__(self, state):
        self.__init__()
        for course, page in state.items():
            self.add(course, page)

