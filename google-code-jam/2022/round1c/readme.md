had to do 1C bc I didn't qualify through 1A (i wuz high) and I was on a trip during 1B.

Unfortunately, 1C was at 5 AM eastern time :( but I made it out of bed and solved A and B. A was prettyyy tedious -- probably my most disliked codejam problem ever (which is because I usually find codejam problems to be really great and fun), but i think that's in part because I approached it with the mindset that it was an easy, 5-minute problem, and I struggled through the cases, where if I had picked a graph representation of the problem, it might have flowed more easily. Still, there's a large gap in this problem between "ok I'm sure I can solve this" and actually writing the code to solve it, which is not good.

B was tough. B-small was very easy, but B-large confounded me for a long time. I finally thought "what if we only need 2 numbers?", an instinct purely based on past programming contests. I worked out the equation, put it into wolfram alpha, and indeed it seemed like I had an answer. Still, there's a problem of how to choose the first number: you must choose it to that the resulting fraction is integer. I have no idea how to choose it, so I tried a brute-force loop up to 1000. This gave WA, so I tried increasing the limit, until eventually it gave TLE instead of WA. Then I switched to pypy, but it still didn't work. (this went on for about 10 submissions.) I was just about to give up and look up some diophantine equation stuff when I tried increasing the limit once more, using pypy. For some reason, I hadn't tried this, and it worked. Beats me why it worked, but I got lucky! (I think I would have qualified anyways with only A and B-small solved? so I don't feel like too much of a fraud).

C actually looked cool, but my 7 AM brain was too weak to seriously try to solve it. Looks like DP is the intended solution for small, and probably a smart DP works for large as well?

I ended up qualifying with a tentative 686rd place.
