


class Pizza(object):
    def __init__(self, index, ings):
        self.index = index
        self.ings = set(ings)
        self.selected = False

    def __repr__(self):
        return '{}-{}'.format(self.index, self.ings)