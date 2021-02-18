
from tqdm import tqdm

PART_SIZE=100

def solve(teams, pizzas):
    for team in tqdm(teams):
        maxScore = 0
        maxScoreIdx = 0
        for i, pizza in enumerate(pizzas[0:PART_SIZE]):
            score = team.calcSc(pizza)
            if score > maxScore:
                maxScore = score
                maxScoreIdx = i
        team.add(pizzas[i])
        pizzas.pop(i)

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
    
    def __repr__(self):
        return '[{}-{}-{}]'.format(self.cap, [p.index for p in self.pizzas], self.ings)

    @property
    def is_full(self):
        return len(self.pizzas) == self.cap