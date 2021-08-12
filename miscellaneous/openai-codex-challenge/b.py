# I'm pretty sure the "accepted" answer is incorrect.
# the accepted answer uses splitlines, but I believe split gives the correct answer, as it doesn't ignore
# terminal newlines.
# (also, ignores the fact that difflib doesn't guarantee minimum edit distance)

import difflib
from typing import Tuple


def diff_files(source: str, target: str) -> Tuple[int, int]:
    print(source)
    print(target)
    print(source.splitlines(), target.splitlines())
    # source = source.split('\n')
    # target = target.split('\n')
    source = source.splitlines()
    target = target.splitlines()
    print(source, target)
    s = difflib.SequenceMatcher(None, source, target)
    matches = s.get_matching_blocks()
    ins = 0
    dele = 0
    ap, bp = 0,0
    print(matches)
    for match in matches:
        ins += match.a-ap
        dele += match.b-bp
        ap,bp = match.a+match.size, match.b+match.size
    # print(dele,ins)
    if len(target) == 1 and target[0] == '':
        return 0,ins
    print(list(difflib.ndiff(source, target)))
    return dele,ins

# Examples
print(diff_files('Apple\nOrange\nPear', 'Apple\nPear\nBanana\nMango'))
print(diff_files('Apple\nOrange\nPear', 'Apple\nPear\nBanana'))
print(diff_files('\nz\ncW\nFe1by\n6X5\n\nsqFzv\nb', 'S\nxb3\n1\nlfJ1\nt9sqW\nUUUZE\n\n\n\nw\nqjT\ngGVBL\n\n'))
print(diff_files('\nz\ncW\nFe1by\n6X5\n\nsqFzv\nb', 'S\nxb3\n1\nlfJ1\nt9sqW\nUUUZE\n\n\n\nw\nqjT\ngGVBL\n\n'))
print(diff_files('0', ''))
