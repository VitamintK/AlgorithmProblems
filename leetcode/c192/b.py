class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        marr = [(v, i) for i,v in enumerate(arr)]
        marr.sort()
        m = marr[(len(arr)-1)//2][0]
        print(m)
        marr.sort(key=lambda x: (abs(m-x[0]),x[0]) , reverse=True)
        return [v for v,i in marr[:k]]
        
        
        