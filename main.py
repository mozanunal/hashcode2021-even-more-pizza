
from pizza import *
from tqdm import tqdm


def readF(filename):
    f = open(filename)

    nPizza, n2, n3, n4 = [int(x) for x in f.readline().split(' ')[0:4]]

    pizzaList = []
    for i in range(nPizza):
        ings = f.readline().replace('\n','').split(' ')[1:]
        pizzaList.append(
            Pizza(i, ings)
        )

    print(pizzaList, n2, n3, n4)

filename = 'data/a_example.in'
# data/a_example.in
# data/b_little_bit_of_everything.in
# data/c_many_ingredients.in
# data/d_many_pizzas.in
# data/e_many_teams.in

readF("data/c_many_ingredients.in")