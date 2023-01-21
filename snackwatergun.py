import random;

print("------------------WELCOME TO THE GAME-------------------------------------------")
ch = 1
refree = dict({1:"SANCK",2:"GUN",3:"WATER"})
computerscore = 0
yourscore = 0
while ch!=0:
    print("ENTER 1 TO SELECT SNACK\nENTER 2 TO SELECT GUN\nENTER 3 TO SELECT WATER\nENTER 4 TO EXIT")
    you = int(input("enter you choice: "))
    match you:
        case 1:
            ch=1
            print#("-------------------------------------------------------------------------------------------")
        case 2:
            ch=2
            print#("-------------------------------------------------------------------------------------------")

        case 3:
            ch=3
            print#("-------------------------------------------------------------------------------------------")
        case 4:
            you=0
            break
            print("-------------------------------------------------------------------------------------------")

        case _:
            print("ENTER THE CORRECT CHOICE")
            continue
    
    computer = random.choice([1,2,3])
    print(f"YOUR CHOICE WAS - {refree[you]} ")
    print(f"COMPUTER CHOICE WAS - {refree[computer]}")
    if you==1 and computer==2 or you==2 and computer==3 or you==3 and computer==1:
          computerscore+=1
    elif you==computer:
          continue
    else:
          yourscore+=1
    print(f"YOUR SCORE IS - {yourscore}")
    print(f"COMPUTER SCORE IS - {computerscore}")
    print("-------------------------------------------------------------------------------------------")


if(yourscore>computerscore):
     print("YOU WINS!!!!!!!")
elif yourscore<computerscore:
     print("COMPUTER WINS BETTER LUCK NEXT TIME")
else:
     print("DRAW!!!!!!!")
