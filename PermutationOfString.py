from itertools import permutations

def permute_string(s):
    return [''.join(p) for p in permutations(s)]

print(permute_string("ABC")) 