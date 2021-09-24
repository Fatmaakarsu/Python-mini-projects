import random

list = ["Tas","Kagit","Makas"]
heart = 3

while True:
    yourChoice = input("Chose one : Tas , Kagit , Makas ->")
    computerChoice = random.choice(list)

    print(f"Computer chose {computerChoice}")

    if yourChoice=="Tas":
      if computerChoice == list[0]:
        print("scoreless !")
        print(f"heart : {heart}")
      elif computerChoice == list[1]:
       print("The computer won ! You lost.")
       heart=heart-1
       print(f"heart : {heart}")
      else:
        print("You won !")
        print(f"heart : {heart}")
    elif yourChoice=="Kagit":
      if computerChoice == list[0]:
        print("You won !")
        print(f"heart : {heart}")
      elif computerChoice == list[1]:
        print("scorless")
        print(f"heart : {heart}")
      else:
        print("The computer won ! You lost.")
        heart=heart-1
        print(f"heart : {heart}")
    elif yourChoice =="Makas":
      if computerChoice == list[0]:
        print("The computer won ! You lost.")
        heart=heart-1
        print(f"heart : {heart}")
      elif computerChoice == list[1]:
        print("You won !")
        print(f"heart : {heart}")
      else:
        print("scorless")
        print(f"heart : {heart}")
    else:
      print("You typed wrong string")
      print(f"heart : {heart}")
    if heart==0:
        print("Game over!")
        break


