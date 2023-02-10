prime_nums = list(filter(lambda x: all(x % i != 0 for i in range(2, x)), nums))

print("Prime numbers in the list:", prime_nums)
