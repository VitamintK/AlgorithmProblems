n = int(input())

def is_suffix(phone, p):
    if len(p) <= len(phone):
        return False
    return phone == p[-len(phone):]

def is_any_suffix(phone, phones):
    for p in phones:
        if is_suffix(phone, p):
            return True
    return False

from collections import defaultdict

name_map = defaultdict(list)
for i in range(n):
    entry = input().split()
    name = entry[0]
    num = int(entry[1])
    phones = entry[2:]
    name_map[name].extend(phones)

print(len(name_map))
for name in name_map:
    phones = name_map[name]
    final_phones = set()
    for phone in phones:
        if not is_any_suffix(phone, phones) and phone not in final_phones:
            final_phones.add(phone)
    print(name, len(final_phones), ' '.join(final_phones))
