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
	var k int
	var s string
	for t := 0; t < T; t++ {
		fmt.Fscan(reader, &n, &k)
		fmt.Fscan(reader, &s)

		fmt.Fprintln(writer, ans)
	}
}
