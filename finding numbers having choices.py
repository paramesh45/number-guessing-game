import random
n=random.randint(1,100)

guess=int(input("guess a number:"))

a=10
for x in range(0,a):
    if guess<n:
        print("too small")
        a -= 1
        print("you remaining guess is :", a)
        guess = int(input("guess a number:"))

    elif guess>n:
        print("too big")
        a -= 1
        print("you remaining guess is :", a)
        guess = int(input("guess a number:"))

    else:
        print("your are too intelligent guess is absolutely correct the number is ",n)
        break

score=a*100
print(score)