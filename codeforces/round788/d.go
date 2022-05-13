package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var T int
	fmt.Scan(&T)
	var n int
	precalc := make([]int, 0)
	vals := []int{0, 0, 0}
	cur := 0
	for i := 0; ; i++ {
		x := i % 3
		lines := vals[(x+1)%3] + vals[(x+2)%3]
		lines *= 2
		cur += lines
		precalc = append(precalc, cur)
		if cur > 1000000000 {
			break
		}
		vals[x]++
	}
	for t := 0; t < T; t++ {
		fmt.Fscan(reader, &n)
		ans := sort.SearchInts(precalc, n)
		fmt.Fprintln(writer, ans+1)
	}
}
