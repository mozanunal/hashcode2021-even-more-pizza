# Hashcode 2021 Even More Pizza



It is our implementation for Hashcode 2021 practice question. It is a clean and readable 4 hours solution writen in **Python**.

- [Competition Link](https://codingcompetitions.withgoogle.com/hashcode/)
- [Past Competitions](https://codingcompetitions.withgoogle.com/hashcode/archive)


| Data      | Scores |
| ----------- | ----------- |
| A – Example | 65 points |
| B – A little bit of everything | 10,816 points |
| C – Many ingredients | 646,200,381 points |
| D – Many pizzas | 7,793,757 points |
| E – Many teams | 6,029,429 points |
| Total | 660,034,448 points |

## Solution

This is a brief explanation of the solution process. Please see the code for the details. We have created 2 classes:
### Pizza Class
Stores ingredients as set and index to create submission file.

```python
class Pizza(object):
    def __init__(self, index, ings):
        self.index = index
        self.ings = set(ings)
        self.count = len(self.ings)
        self.selected = False
        self.score = {}
```

### Team Class

Team class stores the pizzas which are sent to the team. Add function of team class handles:
- adds unique ingridient with union function
- adds pizza to pizzas
- marks pizza as selected
- checks the capacity and already selected pizza error states

```python
class Team():
    def __init__(self, cap):
        self.cap = cap
        self.pizzas = []
        self.ings = set()

    def calcSc(self, pizza):
        comm = self.ings.intersection(pizza.ings)
        uniq = self.ings.union(pizza.ings)
        total = pizza.count
        for p in self.pizzas:
            total += p.count
        sc = len(uniq) / (total)
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
```

## Solver

Solver takes a list of team and a list of pizzas as argument. The pizzas
should already be sorted with count of ingredients. PART_SIZE is used to shorten the calculation process. When checking the potential pizza candidates how many sample will be check is determined with this size in `enumerate(pizzas[0:PART_SIZE])`.

```python
PART_SIZE=256

def solve(teams, pizzas):
    for team in tqdm(teams):
        if len(pizzas) < 1:
            print('done--------------')
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
```
## Solving Process

Solving start with 4 member teams. Since the score is calculated the **square** of the unique ingredients, filling 4 member teams first gives better result.

```python
nPizza, n2, n3, n4, pizzaL, teamL2, teamL3, teamL4 = readF(filename)
pizzaLSorted = sorted(pizzaL, key=operator.attrgetter('count'), reverse=True)
#### initial add start ########
it = iter(pizzaLSorted)
for i in range(len(teamL4)):
    teamL4[i].add(next(it))
pizzaLSorted = pizzaLSorted[n4:]
solve(teamL4, pizzaLSorted)
solve(teamL4, pizzaLSorted)
solve(teamL4, pizzaLSorted)

it = iter(pizzaLSorted)
for i in range(len(teamL3)):
    teamL3[i].add(next(it))
pizzaLSorted = pizzaLSorted[n3:]
solve(teamL3, pizzaLSorted)
solve(teamL3, pizzaLSorted)

it = iter(pizzaLSorted)
for i in range(len(teamL2)):
    teamL2[i].add(next(it))
pizzaLSorted = pizzaLSorted[n2:]
solve(teamL2, pizzaLSorted)

outF( filename.replace('data/','')+'.out', teamL2, teamL3, teamL4  
```


## My Other HashCode Repos

- [Hash Code 2020- Online Qualification](https://github.com/mozanunal/hashcode2020)
- [Hash Code 2018- Online Qualification](https://github.com/mozanunal/hashcode-2018-qualificationQuestion)
- [Hash Code 2017- Practice & Online Qualification](https://github.com/mozanunal/NOP_HashCode2017)


## Team