class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        def dfs(children, s, i, answer):
            child_values = []
            character = s[i]
            for c in children[i]:
                if s[c]==character:
                    dfs(children,s,c,answer)
                else:
                    child_values.append(dfs(children,s,c,answer))
            child_values.sort(reverse=True)
            ans = sum(child_values[:2])+1
            answer[0] = max(answer[0], ans)
            child_values += [0]
            return max(child_values)+1
        children = [[] for i in range(len(s))]
        for child,parent in enumerate(parent):
            if child==0:
                continue
            children[parent].append(child)
        answer = [0]
        dfs(children, s, 0, answer)
        return answer[0]
            