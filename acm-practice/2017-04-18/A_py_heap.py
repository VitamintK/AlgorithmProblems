#https://www.hackerrank.com/challenges/qheap1
#This problem can be solved by just naively doing everything with a heap or BST priority queue.
#here I used the lightweight python heap module called heapq, which lets you do heap operations on a list.
import heapq
pq = []
n = int(input())
end = 0
for i in range(n):
    JJ = [int(x) for x in input().split()]
    t = JJ[0]
    if len(JJ) > 1:
        v = JJ[1]
    if t == 1:
        heapq.heappush(pq, v)
        end += 1
    elif t == 2:
        ind = pq.index(v)
        pq[ind] = pq[end-1]
        pq[end-1] = 1e13
        end -= 1
    else:
        heapq.heapify(pq)
        print(pq[0])