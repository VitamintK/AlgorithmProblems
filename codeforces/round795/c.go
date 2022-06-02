package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var T int
	fmt.Scan(&T)
	var n int
	var k int
	var s string
	for t := 0; t < T; t++ {
		fmt.Fscan(reader, &n, &k)
		fmt.Fscan(reader, &s)
		xs := make([]int, n)
		for i := 0; i < n; i++ {
			x, _ := strconv.Atoi(string(s[i]))
			xs[i] = x
			// if i > 0 {
			// 	ans += x
			// 	ans += xs[i-1] * 10
			// }
		}
		best := 0
		used := 0
		for i := 0; i < n && i < k+1; i++ {
			x := xs[n-1-i]
			if x > best {
				best = x
				used = i
			}
		}
		if used > -1 {
			xs = append(xs[:n-1-used], xs[n-used:]...)
			xs = append(xs, best)
		}
		k -= used
		best = 0
		used = -1
		// fmt.Println(xs)
		// fmt.Println(k)
		for i := 0; i < n-1 && i < k+1; i++ {
			x := xs[i]
			if x > best {
				best = x
				used = i
			}
		}
		if used > -1 {
			asdf := xs[used+1:]
			xs = append([]int{best}, xs[:used]...)
			xs = append(xs, asdf...)
		}
		ans := 0
		for i := 1; i < n; i++ {
			ans += xs[i] + xs[i-1]*10
		}
		// fmt.Println(xs)
		fmt.Fprintln(writer, ans)
	}
}
