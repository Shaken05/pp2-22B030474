def unique(lst):
    return list(dict.fromkeys(lst))     
lst = list(map(int, input().split()))
print(unique(lst))
