import re
def ins_s(s):
    pattern = r'(?<!^)(?=[A-Z])'
    s = re.sub(pattern, ' ', s)
    return s
s = input() # for example: 'ThdscHgsabssaxasAgsa'
s = ins_s(s)
print(s)  # Output: Thdsc Hgsabssaxas Agsa