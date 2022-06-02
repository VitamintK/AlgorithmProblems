package main

import (
	"bufio"
	"fmt"
	"os"
)

// upsolving. was thinking divide-and-conquer but overcomplicating things
// didn't get the neat insights until reading the editorial.
// this is actually quite a complex problem! need 3 different data structures:
//  a prefix table and a suffix table
//  a RMQ segtree over the prefix table, and one ove the suffix table
//  a table that tells you the nearest element to the left >= xs[i] and same for the right
// ah, from the comments: there's also a very simple O(n) solution: https://codeforces.com/blog/entry/103212?#comment-917671

func makeNextGreater(values []int) []int {
	nextGreater := make([]int, len(values))
	for i := range nextGreater {
		nextGreater[i] = len(values)
	}
	stack := make([]int, 0)
	n := len(values)
	for i := n - 1; i >= 0; i-- {
		for len(stack) > 0 && stack[len(stack)-1] >= values[i] {
			nextGreater[stack[len(stack)-1]] = i
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, i)
	}
	return nextGreater
}

func makePrevGreater(values []int) []int {
	prevGreater := make([]int, len(values))
	for i := range prevGreater {
		prevGreater[i] = len(values)
	}
	stack := make([]int, 0)
	n := len(values)
	for i := 0; i < n; i++ {
		for len(stack) > 0 && stack[len(stack)-1] >= values[i] {
			prevGreater[stack[len(stack)-1]] = i
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, i)
	}
	return prevGreater
}

func query(segtree []int) int {

}

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
		// nextGreater[i] gives the index of the nearest element to the right which is >= xs[i]
		nextGreater := makeNextGreater(xs)
		prevGreater := makePrevGreater(xs)
		// prefices[i] gives the sum of everything up to and including xs[i]
		prefices := make([]int, n)
		suffices := make([]int, n)
		for i := 0; i < n; i++ {
			if i == 0 {
				prefices[i] = xs[i]
			} else {
				prefices[i] = prefices[i-1] + xs[i]
			}
		}
		for i := n - 1; i >= 0; i-- {
			if i == n-1 {
				suffices[i] = xs[i]
			} else {
				suffices[i] = suffices[i+1] + xs[i]
			}
		}
		// segtree to give RMQ
		ncap := 1
		for ncap < n {
			ncap *= 2
		}
		prefixTree := make([]int, ncap*2)
		suffixTree := make([]int, ncap*2)
		fmt.Fprintln(writer, ans)
	}
}
