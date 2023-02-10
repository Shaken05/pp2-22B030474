def palindrome(s):
    r = s[::-1]
    if s == r:
        return "YES"
    else:
        return "NO"
s = input()
print(palindrome(s))
