n = int(input().strip())
raws = []
for i in range(n):
    raws.append(input().strip())
from collections import defaultdict
buckets = defaultdict(list)
for raw in raws:
    first, domain = raw.split('@')
    if domain.lower() == "bmail.com":
        first = first.replace('.', '').split('+')[0].lower()
    else:
        first = first.lower()
    sane = first + '@' + domain.lower()
    buckets[sane].append(raw)

print(len(buckets))
for i in buckets.values():
    print(len(i), ' '.join(i))
