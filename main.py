
from team import *
from pizza import *
from tqdm import tqdm
import operator

def readF(filename):
    f = open(filename)

    nPizza, n2, n3, n4 = [int(x) for x in f.readline().split(' ')[0:4]]

    pizzaL = []
    teamL2, teamL3, teamL4 = [],[],[]
    unqPizza = set()
    total = 0
    for i in range(nPizza):
        ings = f.readline().replace('\n','').split(' ')[1:]
        pizzaL.append(
            Pizza(i, ings)
        )
        unqPizza = unqPizza.union(pizzaL[-1].ings)
        total += len(pizzaL[-1].ings)
    
    for i in range(n2):
        teamL2.append(Team(2))
    for i in range(n3):
        teamL3.append(Team(3))
    for i in range(n4):
        teamL4.append(Team(4))

    print('------', filename)
    print('Avg Ings:', total/len(pizzaL))
    print('Total Pizza:', nPizza)
    print('Nums:', n2,n3,n4 )
    print('Unique ings:', len(unqPizza))
    print('Total Cap:', n2*2 + n3*3 + n4*4 )
  

    return nPizza, n2, n3, n4, pizzaL, teamL2, teamL3, teamL4  

def outF(filename, teamL2, teamL3, teamL4):
    f = open(filename, 'w+')
    f.write(str( len(teamL2)+len(teamL3)+len(teamL4)) + '\n')
    for team in teamL4+teamL3+teamL2:
        s = ' '.join( [str(p.index) for p in team.pizzas ] )
        f.write( '{} {}\n'.format(team.cap , s) )
    f.close()


filename = 'data/a_example.in'
# readF("data/a_example.in")
# readF("data/b_little_bit_of_everything.in")
# readF("data/c_many_ingredients.in")
# readF("data/d_many_pizzas.in")
# readF("data/e_many_teams.in")

PART_SIZE=100
nPizza, n2, n3, n4, pizzaL, teamL2, teamL3, teamL4 = readF("data/d_many_pizzas.in")
pizzaLSorted = sorted(pizzaL, key=operator.attrgetter('count'), reverse=True)
#### initial add start ########
it = iter(pizzaLSorted)
for i in range(n4):
    teamL4[i].add(next(it))
for i in range(n3):
    teamL3[i].add(next(it))
for i in range(n2):
    teamL2[i].add(next(it))
pizzaLSortedFilt = pizzaLSorted[n4+n3+n2:]
#### initial add finish ########

solve(teamL4, pizzaLSortedFilt)
solve(teamL4, pizzaLSortedFilt)
solve(teamL4, pizzaLSortedFilt)
solve(teamL3, pizzaLSortedFilt)
solve(teamL3, pizzaLSortedFilt)
solve(teamL2, pizzaLSortedFilt)

outF('a.out', teamL2, teamL3, teamL4  )


# pizzaLPart = pizzaL[0:PART_SIZE]

# for pizzaI in tqdm(pizzaLPart):
#     for pizzaJ in pizzaLPart:
#         if pizzaI.score.get(pizzaJ.index) == None:
#             score = pizzaI.calcScore(pizzaJ)
#             pizzaI.score[pizzaJ.index] = score
#             pizzaJ.score[pizzaI.index] = score