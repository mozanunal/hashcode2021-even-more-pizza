


class Pizza(object):
    def __init__(self, index, ings):
        self.index = index
        self.ings = set(ings)
        self.count = len(self.ings)
        self.selected = False
        self.score = {}

    def __repr__(self):
        return '[id:{}-len:{}-{}]'.format(self.index, self.count, self.ings)