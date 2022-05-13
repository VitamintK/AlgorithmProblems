package main

// import "fmt"
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
		fmt.Fscan(reader, &n, &s, &k)
		// fmt.Println(n, s, k)
		ks := make(map[byte]bool)
		var ki string
		for i := 0; i < k; i++ {
			fmt.Fscan(reader, &ki)
			ks[ki[0]] = true
		}
		ans := 0
		count := 0
		for i := 0; i < n; i++ {
			if ks[s[i]] {
				if count > ans {
					ans = count
				}
				count = 1
			} else {
				count++
			}
		}
		fmt.Fprintln(writer, ans)
	}
}
