# this is like my first time ever implementing union-find LOL

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        col += 2
        sets = dict()
        setsize = dict()
        parent = [0,1]
        for i in range(row):
            sets[(i,0)] = 0
            sets[(i,col-1)] = 1
        setsize[0] = row
        setsize[1] = row
        union_num = 2
        def find(union):
            while parent[union] != union:
                union = parent[union]
            return union
        def add(coords, union):
            setsize[union] +=1
            sets[coords] = union
        def combine(unions):
            if len(unions) == 1:
                return
            mn = 1e10
            argmn = None
            for union in unions:
                if setsize[union] < mn:
                    mn = setsize[union]
                    argmn = union
            newsize = 0
            for union in unions:
                newsize += setsize[union]
                parent[union] = argmn
            setsize[argmn] = newsize
            
        for i, cell in enumerate(cells):
            r,c = cell
            r-=1
            unions = []
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    if dr==0 and dc==0:
                        continue
                    nr,nc = r+dr, c+dc
                    if nr<0 or nr>=row or nc<0 or nc>=col:
                        continue
                    if (nr,nc) in sets:
                        unions.append(find(sets[(nr,nc)]))
            unions = list(set(unions))
            if len(unions) == 0:
                sets[(r,c)] = union_num
                setsize[union_num] = 1
                parent.append(union_num)
                union_num +=1
            else:
                add((r,c), unions[0])
                combine(unions)
            # print(cell, sets, parent, setsize)
            if find(0) == find(1):
                return i
        # print(sets, parent)