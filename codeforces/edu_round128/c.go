package main

// import "fmt"
import (
	"bufio"
	"fmt"
	"os"
)

var s string
var n int
var zeroes int
var ones int

func f(budget int) bool {
	r := 0
	ones_eaten := ones
	zeroes_left := 0
	left_ones_eaten := 0
	for l := -1; l < n; l++ {
		if l != -1 {
			if s[l] == '1' {
				ones_eaten++
				left_ones_eaten++
			} else {
				zeroes_left--
			}
		}
		if left_ones_eaten > budget {
			break
		}
		for r < n && (r <= l || ones_eaten > budget) {
			if s[r] == '1' {
				ones_eaten--
			} else {
				zeroes_left++
			}
			r++
		}
		if zeroes_left <= budget {
			// fmt.Println(ones_eaten, budget)
			return true
		}
	}
	return false
}

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var T int
	fmt.Scan(&T)
	for t := 0; t < T; t++ {
		fmt.Fscan(reader, &s)
		n = len(s)
		zeroes = 0
		for i := 0; i < n; i++ {
			if s[i] == '0' {
				zeroes++
			}
		}
		ones = n - zeroes
		// ahhhhh can't figure out how to do it in O(n) so let's do O(n log n) w/ binary search?
		// or w/ a log(n) structure like in LCS
		// don't want to do that so let's do binary search with sliding window
		l := -1
		r := ones
		// fmt.Println(l, r)
		for r-l > 1 {
			m := (l + r + 1) / 2
			can := f(m)
			if can {
				r = m
			} else {
				l = m
			}
		}
		fmt.Fprintln(writer, r)
	}
}
