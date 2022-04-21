import random
no=random.randint(1,9)
chances=1
turn=int(input("guess the no:"))
if(turn!=no&chances<=5):
    print("Wrong")
    chances=chances+1
    turn=int(input("guess the no:"))
elif(turn==no):
    print("your win")
elif(chances>5):
    print("your loss")
    print(no)
