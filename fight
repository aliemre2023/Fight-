from random import randint

man1 = {"HP":100,"Atk":13,"Def":3}
man2 = {"HP":120,"Atk":8,"Def":6}

round = 0

def attack(attacker,defancer):
    global round
    round += 1
    damage = attacker["Atk"]
    defancer["HP"] -= damage

def attackBoost(attacker):
    global round
    round += 1
    attacker["Atk"] += 15*round

def heal(attacker):
    global round
    round += 1
    attacker["HP"] += 25*round

def chanceAttack(attacker,defancer):
    global round
    round += 1
    damage = attacker["Atk"]+randint(-20,30)*round
    defancer["HP"] -= damage





while True:
    while True:
        print("Round bouns:", round)
        print("""
        ----- MAN1 SEÇİYOR -----
            1 - attack
            2 - attackBoost
            3 - heal
            4 - chanceAttack
            """)
        inp = input("   >> ")

        if inp == "1":
            attack(man1,man2)
            print("man1 man2'ye",man1["Atk"],"hasar vurdu.")
            print("man1=",man1,"\nman2=",man2)
            break
        elif inp == "2":
            attackBoost(man1)
            print("man1'in gücü artık",man1["Atk"])
            print("man1=",man1,"\nman2=",man2)
            break
        elif inp == "3":
            heal(man1)
            print("man1'in HP'si",man1["HP"],"seviyesine yükseldi")
            print("man1=",man1,"\nman2=",man2)
            break
        elif inp == "4":
            oldHP = man2["HP"]
            chanceAttack(man1,man2)
            newHP = man2["HP"]
            print("man1 man2'ye şans eseri",oldHP-newHP,"vurdu.")
            print("man1=",man1,"\nman2=",man2)
            break

    if man2["HP"] <= 0 :
        print("man1 kazandı.")
        break

    while True:
        print("Round bouns:",round)
        print("""
        ----- MAN2 SEÇİYOR -----
            1 - attack
            2 - attackBoost
            3 - heal
            4 - chanceAttack
            """)
        inp = input("   >> ")

        if inp == "1":
            attack(man2,man1)
            print("man2 man1'ye",man2["Atk"],"hasar vurdu.")
            print("man2=",man2,"\nman1=",man1)
            break
        elif inp == "2":
            attackBoost(man2)
            print("man2'in gücü artık",man2["Atk"])
            print("man2=",man2,"\nman1=",man1)
            break
        elif inp == "3":
            heal(man2)
            print("man2'in HP'si",man2["HP"],"seviyesine yükseldi")
            print("man2=",man2,"\nman1=",man1)
            break
        elif inp == "4":
            oldHP = man1["HP"]
            chanceAttack(man2,man1)
            newHP = man1["HP"]
            print("man2 man1'ye şans eseri",oldHP-newHP,"vurdu.")
            print("man2=",man2,"\nman1=",man1)
            break
