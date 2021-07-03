import random
n=random.randint(1,100)

guess=int(input("guess a number:"))


while n!=guess:
    if guess>n:
        print("too big")
        guess = int(input("guess a number:"))
    elif guess<n:
        print("too small")
        guess = int(input("guess a number:"))
    else:
        break
print("your are too intelligent guess is absolutely correct")
print(n)