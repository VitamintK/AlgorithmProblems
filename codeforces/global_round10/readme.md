[Global Round 10](https://codeforces.com/contest/1392)

rank 1095 / X (combined div 1 and div 2)

~~fuuuuuck I used python/pypy for problem B which had 2*10^5 inputs and it TLEd ;_;  
lesson learned: I'm never using python for codeforces again, except for trivial problems where n << TLE
(especially reading inputs?  maybe pypy is especially slow at that?)~~

wait... I'm actually just an idiot.  I wrote `xs = [max(xs)-x for x in xs]` but `max` is `O(n)` so this is `O(n^2)`

other than that, solved A, C, D, E (4/9)

Problem titles:  
- Omkar and Password
- Omkar and Infinity Clock
- Omkar and Waterslide
- Omkar and Bed Wars
- Omkar and Duck
- Omkar and Landslide
- ...

Saw one guy hack a lot of Bs so I tried but couldn't find the hack case so I got 2 incorrect hacks
