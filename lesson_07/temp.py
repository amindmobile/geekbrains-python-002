import itertools


def compress(text):
    for char, same in itertools.groupby(text):
        count = sum(1 for _ in same)  # number of repetitions
        yield char if count == 1 else str(count)+char


print(''.join(compress("aaabccccCCaB")))
