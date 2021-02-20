
from tqdm import tqdm

PART_SIZE=100

def solve2(teams, pizzas):
    if len(pizzas) < 1:
        return
    for team in tqdm(teams):
        if len(pizzas) < 1:
            break
        maxScore = 0
        maxScoreIdx = 0
        for i, pizza in enumerate(pizzas[0:PART_SIZE]):
            score = team.calcSc(pizza)
            if score > maxScore:
                maxScore = score
                maxScoreIdx = i
        team.add(pizzas[maxScoreIdx])
        pizzas.pop(maxScoreIdx)

def solve(teams, pizzas):
    if len(pizzas) < 1:
        return
    for team in tqdm(teams):
        if len(pizzas) < 1:
            break
        for i in range(team.cap):
            maxScore = 0
            maxScoreIdx = 0
            for i, pizza in enumerate(pizzas[0:PART_SIZE]):
                score = team.calcSc(pizza)
                if score > maxScore:
                    maxScore = score
                    maxScoreIdx = i
            team.add(pizzas[maxScoreIdx])
            pizzas.pop(maxScoreIdx)




class Team():
    def __init__(self, cap):
        self.cap = cap
        self.pizzas = []
        self.ings = set()

    # @staticmethod
    # def calcScore(pizzas):
    #     uniq = set.union( [p.ings for p in pizzas] )
    #     total = 0
    #     for p in pizzas:
    #         total += p.count
    #     return len(uniq) / total

    def calcSc(self, pizza):
        comm = self.ings.intersection(pizza.ings)
        uniq = self.ings.union(pizza.ings)
        total = pizza.count
        for p in self.pizzas:
            total += p.count
        sc = len(uniq) - len(comm) #(len(uniq)**2)/ (total)
        return sc

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
