import random
score_p = 0
score_c = 0
while True:
    comp = random.randint(1, 6)
    player = random.randint(1, 6)
    contin = input("Сыграть ещё? напиши 0")
    print("Комп очков",score_c,"Игрок очков",score_p)
    if contin == "0":
        break
    elif comp > player:
        print("Winner comp")
        score_c = score_c + 1
    elif comp < player:
        print("Winner player")
        score_p = score_p + 1
    else:
        print("Равно")

