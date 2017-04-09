n = int(input().strip())
weight_weights = set()
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
weight_weights.update(set(a))
weight_weights.update(set(b))
weight_weights = sorted(list(weight_weights))
weights = [(x,[]) for x in weight_weights]
for ind, i in enumerate(a):
    weights[i].append((1,ind))
for ind, i in enumerate(b):
    weights[i].append((2,ind))
weights = zip(
