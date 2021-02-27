package main

import "fmt"

// Team is
type Team struct {
	index  int
	cap    int
	pizzas []*Pizza
	ings   map[string]bool
}

// NewTeam is
func NewTeam(index int, cap int) Team {
	t := Team{}
	t.index = index
	t.cap = cap
	t.pizzas = []*Pizza{}
	t.ings = map[string]bool{}
	return t
}

func addPizza(team *Team, pizza *Pizza) {
	if pizza.selected {
		panic("Pizza already selected.")
	}
	if len(team.pizzas)+1 > team.cap {
		panic("Team is full")
	}
	team.pizzas = append(team.pizzas, pizza)
	for k := range pizza.ings {
		team.ings[k] = true
	}
	pizza.selected = true
	fmt.Println("Pizza:", pizza.index, ":sc", pizza.count, "added to Team:", team.index)
}

func calcSc(team *Team, pizza *Pizza) int {
	commCount := 0
	for k := range pizza.ings {
		_, ok := team.ings[k]
		if ok {
			commCount++
		}
	}
	return len(pizza.ings) + len(team.ings) - commCount
}
