import random

random_number = random.randint(1,10)
while (True):
    Number = int(input("Enter the random no between 1-10 : "))
    if (Number>random_number):
        print(f"You entered a Larger no kinldy Decrease the Number & Enter the Number less than {Number}")
    elif (Number<random_number):
        print(f"You entered a Smaller no kinldy Increase the Number & Enter the Number less than {Number}")
    else:
        print(f"You finally Entered the Correct Number : {Number}")
        break