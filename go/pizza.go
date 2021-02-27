package main

import (
	// "fmt"
	"sort"
	"strconv"
	"strings"
)

// Pizza is
type Pizza struct {
	index    int
	ings     map[string]bool
	count    int
	selected bool
}

// NewPizza is
func NewPizza(index int, ingsLine string) Pizza {
	p := Pizza{}
	p.index = index
	p.selected = false
	p.ings = make(map[string]bool)
	a := strings.Split(ingsLine, " ")
	for i, v := range a {
		if i < 1 {
			p.count, _ = strconv.Atoi(v)
		} else {
			p.ings[v] = true
		}
	}

	return p
}

// SortPizzaList is
func SortPizzaList(pizzaList []Pizza) []Pizza {
	sort.Slice(pizzaList, func(i, j int) bool {
		return pizzaList[i].count < pizzaList[j].count
	})

	return pizzaList
}
