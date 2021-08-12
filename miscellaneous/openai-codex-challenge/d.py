# literally just copy pasted the docstring, used Codex, and then fixed the extra conditional
# magic!
import ast
from typing import List


def parse_imports(code: str) -> List[str]:
    """Parse the given Python source code and return the list of full-qualified paths for all imported symbols, sorted in ascending lexicographic order."""
    tree = ast.parse(code)
    symbols = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for entry in node.names:
                symbols.append(entry.name)
        elif isinstance(node, ast.ImportFrom):
            for entry in node.names:
#                 if entry.asname is None:
                symbols.append(node.module + "." + entry.name)
#                 else:
#                     symbols.append(node.module + "." + entry.asname)
    return sorted(symbols)

# Examples
print(parse_imports('import os'))
print(parse_imports('import os\nfrom typing import List'))