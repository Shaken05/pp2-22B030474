import itertools
def permutations(string):
    per_list = list(itertools.permutations(string))
    for per in per_list:
        print("".join(per))

s = str(input())
print(permutations(s))
