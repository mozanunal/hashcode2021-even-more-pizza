
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
    nLine = 0
    for team in teamL4+teamL3+teamL2:
        if team.is_full:
            nLine += 1 
    f.write(str( nLine ) + '\n')
    for team in teamL4+teamL3+teamL2:
        if team.is_full:
            s = ' '.join( [str(p.index) for p in team.pizzas ] )
            f.write( '{} {}\n'.format(team.cap , s) )
    f.close()

def solveAll(filename):
    nPizza, n2, n3, n4, pizzaL, teamL2, teamL3, teamL4 = readF(filename)
    pizzaLSorted = sorted(pizzaL, key=operator.attrgetter('count'), reverse=True)
    solve(teamL4, pizzaLSorted)
    solve(teamL3, pizzaLSorted)
    solve(teamL2, pizzaLSorted)
    outF( filename.replace('data/','')+'.out', teamL2, teamL3, teamL4  )


solveAll("data/b_little_bit_of_everything.in")
solveAll("data/c_many_ingredients.in")
solveAll("data/d_many_pizzas.in")
solveAll("data/e_many_teams.in")
