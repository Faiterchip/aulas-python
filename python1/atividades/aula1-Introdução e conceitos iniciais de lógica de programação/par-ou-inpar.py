import random
score=0
pc=random.randint(1,2)
while True:
    chose=input("digite se é par ou inpar: ")
    chose=chose.lower()
    player=int(input("digite 1 ou 2: "))
    pc=random.randint(1,3)
    play=player%pc
    if (play==1) and (chose=='inpar'):
        score=score+1
        print("a")
    elif (play==0) and (chose=='par'):
        score=score+1
        print("a")
    elif (play==1) and (chose=='par'):
        print("b")
        break
    else:
        print("b")
        break
print("-------------------------------------")
print(f"seu resultado foi: {score}")
print(f"pc jogou: {pc}")
print("------------------------------------")