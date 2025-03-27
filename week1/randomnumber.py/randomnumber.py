import random
n=random.randint(1,100)
while True:
    x=int(input("guess the number"))
    if(x<n):
      print("number is too low")
    elif(x>n):
      print("number is too high")
    else:
      print("congrats,you have found the number")
