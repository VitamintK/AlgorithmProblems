package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// this problem looks soooooo boring
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var T int
	fmt.Scan(&T)
	var n int
	var a, b int64

	for t := 0; t < T; t++ {
		fmt.Fscan(reader, &n, &a, &b)
		xs := make([]int64, n+1)
		xs[0] = 0
		for i := 0; i < n; i++ {
			fmt.Fscan(reader, &xs[i+1])
		}
		var ans int64 = 10000000000000000
		var prev int64 = -1
		var cnt int64 = 0
		var sm int64 = 0
		for i := n; i >= 0; i-- {
			if i != n {
				sm += cnt * (prev - xs[i])
			}
			val := xs[i]*a + xs[i]*b
			val += b * sm
			if val < ans {
				ans = val
			}
			prev = xs[i]
			cnt++
		}
		fmt.Fprintln(writer, ans)
	}
}
