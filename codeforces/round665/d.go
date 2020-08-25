package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

// func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
// func scanf(f string, a ...interface{})  { fmt.Fscanf(reader, f, a...) }
var MOD int64 = 1000000007

var n int
var edges [][]int
var contributions int64s

func dfs(node int, parent int) int64 {
	bs := make([]int64, 0)
	var below int64 = 0
	for _, u := range edges[node] {
		if u == parent {
			continue
		}
		b := dfs(u, node)
		below += b
		bs = append(bs, b)
	}
	for _, b := range bs {
		above := int64(n) - b
		c := (b * above)
		contributions = append(contributions, c)
	}
	return below + 1
}

type int64s []int64

func (a int64s) Len() int           { return len(a) }
func (a int64s) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a int64s) Less(i, j int) bool { return a[i] < a[j] }

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var T int
	fmt.Scan(&T)

	for t := 0; t < T; t++ {
		fmt.Fscan(reader, &n)
		edges = make([][]int, n)
		contributions = make([]int64, 0)
		var u, v int
		for i := 0; i < n-1; i++ {
			fmt.Fscan(reader, &u)
			fmt.Fscan(reader, &v)
			edges[u-1] = append(edges[u-1], v-1)
			edges[v-1] = append(edges[v-1], u-1)
		}
		var m int
		fmt.Fscan(reader, &m)
		ps := make(int64s, m)
		for i := 0; i < m; i++ {
			fmt.Fscan(reader, &ps[i])
		}
		dfs(0, 0)
		sort.Sort(sort.Reverse(contributions))
		sort.Sort(ps)
		for len(ps) > len(contributions) {
			a := ps[len(ps)-1]
			b := ps[len(ps)-2]
			ps = ps[:len(ps)-2]
			ps = append(ps, (a*b)%MOD)
		}
		revps := make([]int64, len(ps))
		for i := len(ps) - 1; i >= 0; i-- {
			revps[len(ps)-i-1] = ps[i]
		}
		ps = revps
		for i := len(ps); i < len(contributions); i++ {
			ps = append(ps, 1)
		}
		var ans int64 = 0
		for i := 0; i < len(contributions); i++ {
			g := (contributions[i] * ps[i]) % MOD
			ans += g
			ans %= MOD
		}
		fmt.Fprintln(writer, ans)
	}
}
