// R, G, B = map(int, input().split())
// rs = [int(x) for x in input().split()]
// gs = [int(x) for x in input().split()]
// bs = [int(x) for x in input().split()]
// rs.sort()
// gs.sort()
// bs.sort()
// sticks = [rs, gs, bs]
// import sys
// sys.setrecursionlimit(1000)
// memo = dict()
// def dfs(i,j,k):
//     if (i,j,k) in memo:
//         return memo[(i,j,k)]
//     if sum([i==-1,j==-1,k==-1])>1:
//         return 0
//     a = gs[j]*bs[k] + dfs(i,j-1,k-1) if j>=0 and k>=0 else 0
//     b = rs[i]*bs[k] + dfs(i-1,j,k-1) if i>=0 and k>=0 else 0
//     c = rs[i]*gs[j] + dfs(i-1,j-1,k) if i>=0 and j>=0 else 0
//     r = max(a,b,c)
//     memo[(i,j,k)] = r
//     return r
// ans = dfs(R-1, G-1, B-1)
// print(ans)

package main

import (
	"fmt"
	"sort"
)

type ky struct {
	i, j, k int
}

var memo map[ky]int

func dfs(i int, j int, k int) int {
	if v, ok := memo[ky{i, j, k}]; ok {
		return v
	}
	if (i == -1 && j == -1) || (i == -1 && k == -1) || (j == -1 && k == -1) {
		return 0
	}
	a, b, c := 0, 0, 0
	if j >= 0 && k >= 0 {
		a = gs[j]*bs[k] + dfs(i, j-1, k-1)
	}
	if i >= 0 && k >= 0 {
		b = rs[i]*bs[k] + dfs(i-1, j, k-1)
	}
	if i >= 0 && j >= 0 {
		c = rs[i]*gs[j] + dfs(i-1, j-1, k)
	}
	// r := math.Max(a, b, c)
	best := 0
	if a > best {
		best = a
	}
	if b > best {
		best = b
	}
	if c > best {
		best = c
	}
	memo[ky{i, j, k}] = best
	return best
}

var rs []int
var bs []int
var gs []int

func main() {
	var R, G, B int
	fmt.Scan(&R, &G, &B)
	rs = make([]int, R)
	gs = make([]int, G)
	bs = make([]int, B)
	for i := 0; i < R; i++ {
		fmt.Scan(&rs[i])
	}
	for i := 0; i < G; i++ {
		fmt.Scan(&gs[i])
	}
	for i := 0; i < B; i++ {
		fmt.Scan(&bs[i])
	}
	sort.Ints(rs)
	sort.Ints(bs)
	sort.Ints(gs)
	memo = make(map[ky]int)

	ans := dfs(R-1, G-1, B-1)
	fmt.Printf("%d", ans)
}
