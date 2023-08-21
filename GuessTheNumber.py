import random

def guess(x):
    random_number=random.randint(1,x)
    guess=1
    while guess!=random_number:
        guess=int(int(input("Enter number: ")))
        if guess>random_number:
            print("Number is too high")
        elif guess<random_number:
            print("Number is too low")
        elif guess==random_number:
            print("congrats")
guess(10)

        
    
