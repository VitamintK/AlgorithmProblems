class Segment:
    def __init__(self, value, length, index):
        self.value = value
        self.length = length
        self.index = index
        self.left = None
        self.right = None
        self.removed = False
    def chain_right(self, right):
        self.right = right
        right.left = self
    def __lt__(self, other):
        return (-self.length, self.index) < (-other.length, other.index)
    def rm(self):
        to_return = None
        if self.left is not None and self.right is not None and self.left.value == self.right.value:
            #print("JOINING")
            #print("combine", self.left.value, "and", self.right.value)
            self.left.length += self.right.length
            self.right.removed = True
            self.right = self.right.right
            to_return = self.left

        if self.left is not None:
            self.left.right = self.right
        if self.right is not None:
            self.right.left = self.left
        self.removed = True
        return to_return

import heapq

q = []

n = int(input())
#if n == 904:
#    print(input()[2500:])
l = [int(x) for x in input().split()] + [None]
prev = None
prev_segment = None
count = -1
ind = 0
for i in l:
    if i == prev:
        count+=1
    else:
        if prev is not None:
            s = Segment(prev, count, ind)
            if prev_segment is not None:
                prev_segment.chain_right(s)
            heapq.heappush(q, s)
            prev_segment = s
        count = 1
        prev = i
    ind+=1

ans = 0
while len(q) > 0:
    segment = heapq.heappop(q)
    print(segment.length, segment.index)
    if segment.removed:
        print("^  skipped")
        continue
    ans +=1
    #print(segment.value, segment.length)
    new_segment = segment.rm()
    if new_segment is not None:
        heapq.heappush(q, new_segment)
        print("new", new_segment.length, new_segment.index)

print(ans)