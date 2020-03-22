from collections import defaultdict
import sys

sys.setrecursionlimit(500000)
class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.words = 0
    def set_word(self):
        self.words += 1
    def get(self, c):
        return self.children[c]
    def add(self, s):
        n = self
        for c in s:
            n = n.get(c)
        n.set_word()
    def recurse(self):
        global ans
        self.score = self.words
        for i in self.children.values():
            child_score = i.recurse()
            self.score += child_score
            ans += child_score//k
        return self.score


T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    tr = TrieNode()
    for i in range(n):
        s = input()
        tr.add(s)
    ans = 0
    tr.recurse()
    # print(tr.score)
    print("Case #{}: {}".format(t+1, ans))