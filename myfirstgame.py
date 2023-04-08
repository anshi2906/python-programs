def game(comp,you):
    if comp=='you':
        return None
    elif comp=='r':
        if you =='p':
            return True
        elif you=='s':
            return False
    elif comp=='p':
        if you=='r':
            return False
        elif you=='s':
            return True
    elif comp=='s':
        if you=='r':
            return True
        elif you=='p':
            return False
print("comp turn: choose rock(r),paper(p),scissor(s)?")
import random
randno=random.randint(1,3)
if randno==1:
    comp='r'
elif randno ==2:
    comp='p'
elif randno==3:
    comp='s'
you =input("your turn:choose-r,p,s:")
a=game(comp,you)
print(f"comp chhose{comp}")
print(f"you choose{you}")
if a== None:
    print("tie")
elif a==True:
    print("you win")
else:
    print("you lose")
