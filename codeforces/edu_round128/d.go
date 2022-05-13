package main

// import "fmt"
import (
	"bufio"
	"fmt"
	"os"
)

// oops I misinterpreted the problem and thought it was really easy
// so this is wrong lol
func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var n, k int
	fmt.Scan(&n, &k)
	a := make([]int, n)
	total := 0
	x := 0
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &a[i])
		total += a[i]
		if a[i] == 0 {
			x++
		}
	}
	if total > k*x || -total > k*x {
		fmt.Fprintln(writer, -1)
	} else {
		ans := 0
		for sign := 1; sign >= -1; sign -= 2 {

			ks := make([]int, x)
			used := 0
			for i := x - 1; i >= 0; i-- {
				var maxval int
				if i == 0 {
					maxval = total * sign
				} else {
					maxval = (i-1)*k + total*sign
				}
				val := maxval - used
				if k < val {
					val = k
				}
				ks[i] = val
				used += val
				fmt.Println("ah", val)
			}
			highval := 0
			v := 0
			kcount := 0
			for i := 0; i < n; i++ {
				v += a[i] * sign
				if a[i] == 0 {
					v += ks[kcount] * -1
					kcount++
				}
				if v > highval {
					highval = v
				}
				fmt.Println(v)
			}
			fmt.Println("highval", highval)
			ans += highval
		}
		fmt.Fprintln(writer, ans+1)
	}
}
