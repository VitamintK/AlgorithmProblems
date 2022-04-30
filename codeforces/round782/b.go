package main

// import "fmt"
import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
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
		fmt.Fscan(reader, &n, &k, &s)
		var ans []byte
		var flips []int
		flip := false
		for i := 0; i < n; i++ {
			val := s[i]
			if flip {
				if val == '1' {
					val = '0'
				} else {
					val = '1'
				}
			}
			if k == 0 || i == n-1 {
				ans = append(ans, val)
				flips = append(flips, k)
			} else {
				if k%2 == 0 {
					if val == '1' {
						// we are 1, want to keep it: dont flip!
						ans = append(ans, '1')
						flips = append(flips, 0)
					} else {
						// we are 0, want to flip it: flip!
						ans = append(ans, '1')
						k--
						flip = !flip
						flips = append(flips, 1)
					}
				} else {
					if val == '1' {
						// we are 1, want to keep it: flip!
						ans = append(ans, '1')
						k--
						flip = !flip
						flips = append(flips, 1)
					} else {
						// we are 0, want to flip it: don't flip!
						ans = append(ans, '1')
						flips = append(flips, 0)
					}
				}
			}
		}
		fmt.Fprintln(writer, string(ans))
		var flipstrings []string
		for _, j := range flips {
			flipstrings = append(flipstrings, strconv.Itoa(j))
		}
		fmt.Fprintln(writer, strings.Join(flipstrings, " "))
		// fmt.Fprintln(writer, ans)
	}
}
