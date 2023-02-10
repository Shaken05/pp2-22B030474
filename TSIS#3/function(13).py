n = random.randint(1, 20)
answer = n
print("Hello! What's your name? ", end="")
s = input()
print(s)

print("Well, {zzxc}, I am thinking of a number between 1 and 20.".format(zzxc = s))

print(number)
counter = 0
while number != answer:
    print("Take a guess.")
    number = int(input())
    if(number > answer):
        print("Your guess is too big")
    else:
        print("Your guess is too low.")
    counter += 1
print("Good job, KBTU! You guessed my number in {res} guesses!".format(res = counter))
