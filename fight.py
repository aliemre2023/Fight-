from random import randint


dicti = {"a1" : {"HP":100,"Atk":13,"Def":3}, "b2" : {"HP":120,"Atk":8,"Def":6}}


def attack(attacker,defancer):
    damage = attacker["Atk"] - defancer["Def"]
    defancer["HP"] -= damage

def attackBoost(attacker):
    attacker["Atk"] += 15*round

def heal(attacker):
    attacker["HP"] += 25*round

def chanceAttack(attacker,defancer):
    damage = attacker["Atk"]+randint(-20,25)*round - defancer["Def"]
    defancer["HP"] -= damage

def defanceIncreaseing(attacker):
    attacker["Def"] += 10*round

def fiftyFifty(attacker,defancer):
    attacker["Atk"] = attacker["Atk"]/2
    defancer["HP"] = defancer["HP"]/2

def nuclearPunch(attacker,defancer):
    attacker["Atk"] = attacker["Atk"]*3/4
    attacker["HP"] = attacker["HP"]*3/5
    defancer["Atk"] = defancer["Atk"]*4/3
    defancer["HP"] = defancer["HP"]/2


while True:
    print("""
    1-savaş
    2-karakter ekle
    """)
    sec = input(" >>")
    if sec == "1":
        isim1, man1 = input("isim seçin:"),dicti[input("karaker seçin:")]
        isim2, man2 = input("isim seçin:"),dicti[input("karakter seçin:")]

        round = 0

        while True:
            round += 1

            while True:
                print("/"*50)
                print("Round bouns:", round)
                print("-------",isim1,"-------")
                print("""
                    1 - attack
                    2 - attack Boost
                    3 - heal
                    4 - chance Attack
                    5 - defance Increasing
                    6 - fifty Fifty
                    7 - nuclear Punch
                    """)
                inp = input("   >> ")

                if inp == "1":
                    attack(man1,man2)
                    print(isim1,man1["Atk"]-man2["Def"],"vuruş -->",isim2)
                    break
                elif inp == "2":
                    attackBoost(man1)
                    print(isim1,"güç artışı -->",man1["Atk"])
                    break
                elif inp == "3":
                    heal(man1)
                    print(isim1,"ycan artışı -->",man1["HP"])
                    break
                elif inp == "4":
                    oldHP = man2["HP"]
                    chanceAttack(man1,man2)
                    newHP = man2["HP"]
                    print(isim1,oldHP-newHP,"şans vuruşu -->",isim2)
                    break
                elif inp == "5":
                    defanceIncreaseing(man1)
                    print(isim1,"defans artışı -->",man1["Def"])
                    break
                elif inp == "6":
                    fiftyFifty(man1,man2)
                    print("Hammurabi döneminde mi yaşıyoruz abi.")
                    break
                elif inp == "7":
                    nuclearPunch(man1,man2)
                    print("Bu ne tantana kardeşim!")
                    break

            if man2["HP"] <= 0 :
                print(isim1,"kazandı.")
                break
            else:
                print("******\n",isim1,"=", man1, "\n", isim2,"=", man2,"\n******",sep="")


            while True:
                print("/" * 50)
                print("Round bouns:",round)
                print("-------",isim2,"-------")
                print("""
                    1 - attack
                    2 - attack Boost
                    3 - heal
                    4 - chance Attack
                    5 - defance Increasing
                    6 - fifty Fifty
                    7 - nuclear Punch
                    """)
                inp = input("   >> ")

                if inp == "1":
                    attack(man2,man1)
                    print(isim2,man2["Atk"]-man1["Def"],"vuruş -->",isim1)
                    break
                elif inp == "2":
                    attackBoost(man2)
                    print(isim2,"güç artışı -->",man2["Atk"])
                    break
                elif inp == "3":
                    heal(man2)
                    print(isim2,"ycan artışı -->",man2["HP"])
                    break
                elif inp == "4":
                    oldHP = man1["HP"]
                    chanceAttack(man2,man1)
                    newHP = man1["HP"]
                    print(isim2,oldHP-newHP,"şans vuruşu -->",isim1)
                    break
                elif inp == "5":
                    defanceIncreaseing(man2)
                    print(isim2,"defans artışı -->",man2["Def"])
                    break
                elif inp == "6":
                    fiftyFifty(man2,man1)
                    print("Hammurabi döneminde mi yaşıyoruz abi.")
                    break
                elif inp == "7":
                    nuclearPunch(man2,man1)
                    print("Bu ne tantana kardeşim!")
                    break

            if man1["HP"] <= 0:
                print(isim2,"kazandı.")
                break
            else:
                print("******\n",isim1,"=", man1, "\n", isim2,"=", man2,"\n******",sep="")

    elif sec == "2":
        print("Karakter Ekleme Ekranı")
        isim = input("KArakterin ismi:")
        HP = int(input("Karakterin HP'si:"))
        Atk = int(input("Karakterin Atttack'ı:"))
        Def = int(input("Karakterin Defance'sı:"))

        dicti[isim] = {"HP":HP,"Atk":Atk,"Def":Def}
        print(dicti)






