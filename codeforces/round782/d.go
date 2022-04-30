package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var T int
	fmt.Scan(&T)
	var n int

	for t := 0; t < T; t++ {
		fmt.Fscan(reader, &n)
		xs := make([]int, n)
		for i := 0; i < n; i++ {
			fmt.Fscan(reader, &xs[i])
		}
		ans := make([]int, n)
		for i := 0; i < n; i++ {

		}
		fmt.Fprintln(writer, ans)
	}
}
