class Solution:
    def thousandSeparator(self, n: int) -> str:
        return '{0:,}'.format(n).replace(',','.')