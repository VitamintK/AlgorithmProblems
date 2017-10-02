if __name__ == "__main__":
    n = int(input().strip())
    m = int(input().strip())
    volcanoes = []
    for a0 in range(m):
        x, y, w = input().strip().split(' ')
        x, y, w = [int(x), int(y), int(w)]
        # Write Your Code Here
        volcanoes.append((x,y,w))
    ans = 0
    for x in range(n):
        for y in range(n):
            w = 0
            for vx, vy, vw in volcanoes:
                w+=max(0, vw - max(abs(x-vx), abs(y-vy)))
            ans = max(ans, w)
    print(ans)