class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(' ')
        words = text.strip().split()
        if len(words) > 1:
            num_space = spaces//(len(words)-1)
            s = (' '*num_space).join(words)
            s += ' '*(spaces%(len(words)-1))
        else:
            s = words[0] + ' '*spaces
        return s