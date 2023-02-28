import re
a = input()
res1 = re.sub(" ", ",", a)
res2 = re.sub(" ", ":", a)
print(res1)
print(res2)