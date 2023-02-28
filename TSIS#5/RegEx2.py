import re
a = input()
b = re.findall(r"ab{2,3}", a)
if b:
    print("True")
else:
    print("False")