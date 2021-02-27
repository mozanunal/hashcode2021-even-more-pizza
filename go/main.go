package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

func solve(teams []Team, pizzas []Pizza) {

}

func solveF(filename string) {

	const LOOK_AHEAD_COUNT = 100

	content, err := ioutil.ReadFile(filename)

	if err != nil {
		log.Fatal(err)
	}

	contStr := string(content)
	lines := strings.Split(contStr, "\n")
	line0 := strings.Split(lines[0], " ")
	// nPizza, _ := strconv.Atoi(line0[0])
	n2, _ := strconv.Atoi(line0[1])
	n3, _ := strconv.Atoi(line0[2])
	n4, _ := strconv.Atoi(line0[3])
	var pizzaList []Pizza
	var teamList []Team
	for i, line := range lines[1:] {
		if len(line) < 1 {
			break
		}
		pizzaList = append(pizzaList, NewPizza(i, line))
	}
	pizzaList = SortPizzaList(pizzaList)
	for i := 0; i < n4; i++ {
		teamList = append(teamList, NewTeam(i, 4))
	}
	for i := 0; i < n3; i++ {
		teamList = append(teamList, NewTeam(i+n4, 3))
	}
	for i := 0; i < n2; i++ {
		teamList = append(teamList, NewTeam(i+n3+n4, 2))
	}

	for i := range teamList {
		for j := 0; j < teamList[i].cap; j++ {
			// for every team
			maxScore := 0
			maxScoreIndex := -1
			lookAheadCount := 0
			for k, pizza := range pizzaList {
				if pizza.selected == false {
					lookAheadCount++
					if lookAheadCount > LOOK_AHEAD_COUNT {
						fmt.Println("Done...")
						break
					}
					score := calcSc(&teamList[i], &pizzaList[k])
					if score > maxScore {
						maxScore = score
						maxScoreIndex = k
					}
				}
			}
			if maxScoreIndex == -1 {
				fmt.Println("No Max Score")
				break
			} else {
				// fmt.Println("max Score is", maxScore)
				addPizza(&teamList[i], &pizzaList[maxScoreIndex])

			}
		}
	}

	// addPizza(&n2List[0], &pizzaList[0])
	// addPizza(&n2List[0], &pizzaList[1])
	// addPizza(&n2List[0], &pizzaList[2])
	// fmt.Println(nPizza, n2, n3, n4)
	// fmt.Println(pizzaList)
	fmt.Println(teamList[0])
	// fmt.Println(pizzaList[0])
	// fmt.Println(pizzaList[len(pizzaList)-1])

}

func main() {
	filename := "../data/b_little_bit_of_everything.in"
	fmt.Println("--------", filename)
	solveF(filename)
	// fmt.Println("hello world")
	// p := newPizza(0, "3 a b c", 3)
	// fmt.Println(*p)
}
