# func main() {
# 	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
# 	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
# 	defer writer.Flush()
# 	var T int
# 	fmt.Scan(&T)

# 	for t := 0; t < T; t++ {
# 		var x int
# 		s, _ := reader.ReadString('\n')
# 		s = strings.TrimSpace(s)
# 		n := len(s)
# 		fmt.Fscan(reader, &x)
# 		reader.Discard(1)
# 		ans := make([]byte, n)
# 		for i := range ans {
# 			ans[i] = '1'
# 		}
# 		for i := 0; i < n; i++ {
# 			if s[i] == '1' {
# 				continue
# 			}
# 			if i-x >= 0 {
# 				ans[i-x] = '0'
# 			}
# 			if i+x < n {
# 				ans[i+x] = '0'
# 			}
# 		}
# 		impossible := false
# 		for i := range ans {
# 			if s[i] == '0' {
# 				continue
# 			}
# 			if i-x >= 0 && ans[i-x] == '1' {
# 				continue
# 			}
# 			if i+x < n && ans[i+x] == '1' {
# 				continue
# 			}
# 			impossible = true
# 			break
# 		}
# 		if impossible {
# 			fmt.Fprintln(writer, "-1")
# 			writer.Flush()
# 			continue
# 		}
# 		// for _, a := range ans {
# 		// 	fmt.Fprint(writer, a)
# 		// }
# 		anstring := string(ans)
# 		fmt.Fprintln(writer, anstring)
# 		writer.Flush()
# 		// fmt.Fprintln(writer, ans)
# 	}
# }
T = int(input())
for t in range(T):
    s = input()
    x = int(input())
    n = len(s)
    ans = [1 for i in range(n)]
    for i, a in enumerate(s):
        if a == '1':
            continue
        if i-x >= 0:
            ans[i-x] = 0
        if i+x < n:
            ans[i+x] = 0
    impossible = False
    for i, a in enumerate(s):
        if a == '0':
            continue
        if i-x >= 0 and ans[i-x] == 1:
            continue
        if i+x < n and ans[i+x] == 1:
            continue
        impossible = True
        break
    if impossible:
        print("-1")
        continue
    print(''.join(str(x) for x in ans))