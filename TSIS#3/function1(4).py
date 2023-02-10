def filter_prime(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    return [x for x in nums if is_prime(x)]
numbers = list(map(int, input().split()))
print(filter_prime(numbers))
