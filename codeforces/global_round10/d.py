# fuck go it doens't work

# defer writer.Flush()
# 	var T int
# 	scanf("%d", T)
# 	fmt.Fprintln(writer, T)
# 	var n int
# 	var s string
# 	for t := 0; t < T; t++ {
# 		fmt.Fscan(reader, n)
# 		fmt.Fscan(reader, n)
# 		start := 0
# 		for i := 1; i < n; i++ {
# 			if s[i] != s[i-1] {
# 				start = i - 1
# 			}
# 		}
# 		ans := 0
# 		runlen := 1
# 		for i := 1; i < n; i++ {
# 			p := (start + i) % n
# 			if s[p] == s[p-1] {
# 				runlen++
# 			} else {
# 				ans += (runlen) / 3
# 				runlen = 0
# 			}
# 		}
# 		ans += (runlen) / 3
# 		fmt.Fprintln(writer, ans)
# 	}
T = int(input())
for t in range(T):
    n = int(input())
    s = input()
    for i in range(1, n):
        if s[i] != s[i-1]:
            start = i
            break
    ans = 0
    runlen = 1
    for i in range(1, n):
        p = (start + i)%n
        if s[p] == s[p-1]:
            runlen += 1
        else:
            ans += runlen//3
            runlen = 1
    if runlen == n:
        ans += (runlen+2)//3
    else:
        ans += runlen//3
    print(ans)