package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

// func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
// func scanf(f string, a ...interface{})  { fmt.Fscanf(reader, f, a...) }

func main2() {
	// to run this file, rename to main
	// (I renamed to main2 bc it's in same directory as d)
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var T int
	fmt.Scan(&T)
	var n int
outer:
	for t := 0; t < T; t++ {
		fmt.Fscan(reader, &n)
		as := make([]int, n)
		sas := make([]int, n)
		gmin := 1123456789
		for i := 0; i < n; i++ {
			fmt.Fscan(reader, &as[i])
			sas[i] = as[i]
			if as[i] < gmin {
				gmin = as[i]
			}
		}
		sort.Ints(sas)
		for i := 0; i < n; i++ {
			if sas[i] != as[i] {
				if as[i]%gmin != 0 || sas[i]%gmin != 0 {
					fmt.Fprintln(writer, "NO")
					continue outer
				}
			}
		}
		fmt.Fprintln(writer, "YES")
		// fmt.Fprintln(writer, ans)
	}
}
