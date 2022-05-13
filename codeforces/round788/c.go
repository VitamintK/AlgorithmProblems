package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	MOD := 1000000007
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var T int
	fmt.Scan(&T)
	var n int
	for t := 0; t < T; t++ {
		fmt.Fscan(reader, &n)
		as := make([]int, n)
		bs := make([]int, n)
		ds := make([]int, n)

		a_reverse := make([]int, n)
		b_reverse := make([]int, n)
		for i := 0; i < n; i++ {
			fmt.Fscan(reader, &as[i])
			as[i]--
			a_reverse[as[i]] = i
		}
		for i := 0; i < n; i++ {
			fmt.Fscan(reader, &bs[i])
			bs[i]--
			b_reverse[bs[i]] = i
		}
		for i := 0; i < n; i++ {
			fmt.Fscan(reader, &ds[i])
		}
		ans := 1
		// cycles := 0
		colored := make([]bool, n)
		for i := 0; i < n; i++ {
			if colored[i] {
				// fmt.Println(i)
				continue
			}
			// for j := 0; j < n; j++ {
			// 	fmt.Print(colored[j], " ")
			// }
			// fmt.Print("\n")
			a := as[i]
			untouched := true
			index := b_reverse[a]

			for index != i {
				colored[index] = true
				if ds[index] != 0 {
					untouched = false
				}
				a = as[index]
				index = b_reverse[a]
			}
			colored[index] = true
			if ds[index] != 0 {
				untouched = false
			}
			// fmt.Println(untouched)
			if untouched && as[i] != bs[i] {
				ans *= 2
				ans %= MOD
			}
		}
		fmt.Fprintln(writer, ans)
	}
}
