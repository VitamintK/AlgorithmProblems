import math
def answer(N, K):
    necessary = N-1
    extra = K - necessary
    necessary_enum = math.factorial(N)/2
    if extra > 0:
        extra_enum = math.factorial(N*(N-1))/(math.factorial(extra)*math.factorial(N*(N-1) - extra))
    else:
        extra_enum = 0
    return necessary_enum, extra_enum
