import difflib
from typing import Tuple


def diff_files(source: str, target: str) -> Tuple[int, int]:
    """
    Codex attempt #3
    """
    source_lines = source.splitlines()
    target_lines = target.splitlines()
    d = difflib.Differ()
    diff = d.compare(source_lines, target_lines)
    inserted = 0
    deleted = 0
    for line in diff:
        if line.startswith('+'):
            inserted += 1
        elif line.startswith('-'):
            deleted += 1
    return inserted, deleted

print(diff_files('1\n10\n2\n3\n13\n5\n6\n4','2\n12\n3\n5\n14\n4\n6\n1'))