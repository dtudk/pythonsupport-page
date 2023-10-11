__all__ = [
    "HomepageFormatter",
    "Coursebase",
    "CourseStrip",
]


def split_str(s, sep=None, maxsplit=-1):
    """ split a string """
    sl = s.split(sep, maxsplit)
    if maxsplit > 0:
        n_add = maxsplit + 1 - len(sl)
        sl.extend([''] * n_add)
    print(sl)
    return sl


class HomepageFormatter:

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

class Coursebase:

    def __init__(self, prefix):
        self.prefix = prefix

    def format(self, course):
        if ":" in course:
            years, course = course.split(":", maxsplit=1)
            if "-" in years:
                start, end = tuple(map(int, years.split("-")))
            else:
                start = int(years)
                end = start + 1

            if start < 1000:
                start += 2000
            if end < 1000:
                end += 2000

            years = f"{start}-{end}"
            return f"{self.prefix}/{years}/{course}"
        return f"{self.prefix}/{course}"

    __mod__ = format

class CourseStrip:
    def format(self, course):
        if ":" in course:
            return course.split(":", maxsplit=1)[-1]
        return course
    __mod__ = format
