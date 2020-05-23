class Solution:
    def arrangeWords(self, text: str) -> str:
        t = [x.lower() for x in text.split()]
        t.sort(key = lambda x: len(x))
        t[0] = t[0].title()
        return ' '.join(t)