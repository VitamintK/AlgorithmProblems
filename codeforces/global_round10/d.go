package main

import (
	"bufio"
	"fmt"
	"os"
)

// func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
// func scanf(f string, a ...interface{})  { fmt.Fscanf(reader, f, a...) }

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var T int
	fmt.Scan(&T)
	var n int
	var s string
	for t := 0; t < T; t++ {
		fmt.Fscan(reader, &n)
		fmt.Fscan(reader, &s)
		start := 0
		for i := 1; i < n; i++ {
			if s[i] != s[i-1] {
				start = i
			}
		}
		ans := 0
		runlen := 1
		for i := 1; i < n; i++ {
			p := (start + i) % n
			prev := (p + n - 1) % n
			if s[p] == s[prev] {
				runlen++
			} else {
				ans += (runlen) / 3
				runlen = 1
			}
		}
		if runlen == n {
			ans += (runlen + 2) / 3
		} else {
			ans += (runlen) / 3
		}
		fmt.Fprintln(writer, ans)
	}
}
