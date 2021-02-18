
class Team():
    def __init__(self, cap):
        self.cap = cap
        self.pizzas = []
        self.ings = set()
        
    @staticmethod
    def calcScore(pizzas):
        uniq = set.union( [p.ings for p in pizzas] )
        total = 0
        for p in pizzas:
            total += p.count
        return len(uniq) / total

    def calcSc(self, pizza):
        uniq = self.ings.union(pizza.ings)
        total = pizza.count
        for p in self.pizzas:
            total += p.count
        return len(uniq) / total

    def add(self, pizza):
        assert 1 + len(self.pizzas) <= self.cap
        self.pizzas.append(pizza)
        assert pizza.selected == False
        pizza.selected = True
        self.ings = self.ings.union(pizza.ings)

    @property
    def is_full(self):
        return len(self.pizzas) == self.cap