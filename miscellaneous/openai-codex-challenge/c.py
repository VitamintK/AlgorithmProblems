from typing import Dict, Union

Tree = Dict[str, Union[str, "Tree"]]


def decompress(compressed: str, tree: Tree) -> str:
    ans = []
    t = tree
    for x in compressed:
        t = t[x]
        if t == str(t):
            ans.append(t)
            t = tree
    return ''.join(ans)

# Examples
print(decompress('110100100', {'0': 'a', '1': {'0': 'n', '1': 'b'}}))
print(decompress('0111010100', {'0': {'0': 'x', '1': 'z'}, '1': 'y'}))