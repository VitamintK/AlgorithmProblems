N = int(input())
import math
for i in range(N):
    n, l, d, g = map(int, input().split())
    apothem = l/(2*math.tan(math.pi/n))
    initial_area = (apothem*l/2) * n
    rectangle_expansion = d * l * g * n
    circle_expansion = d * g * d * g * math.pi * n
    circle_proportion = (180 - (180 - 360/n))/360
    circle_expansion *= circle_proportion
    # print(initial_area, rectangle_expansion, circle_expansion)
    print(initial_area + rectangle_expansion + circle_expansion)

# tan(2*pi/n) 