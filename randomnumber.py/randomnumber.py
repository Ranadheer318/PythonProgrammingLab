import random
n=random.randint(1,100)
x=int(input("guess the number"))
while True:
    if(x<n):
      print("number is too low")
    elif(x>n):
      print("number is too high")
    else:
      print("congrats,you have found the number")

