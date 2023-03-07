import time
import math

def square_root(num):
    return math.sqrt(num)

num = int(input())
milliseconds = int(input())

time.sleep(milliseconds / 1000)#переводим миллисекунды в секунды
result = square_root(num)

print("Square root of",num, "after",milliseconds,"miliseconds is",result)
