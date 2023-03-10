import pandas as pd
from openpyxl import load_workbook, Workbook

data = pd.read_excel("characters.xlsx")
pd.options.mode.chained_assignment = None


# Functions
def attack(attacker, defancer):
    damage = data["Atk"][attacker] - data["Def"][defancer]
    data["HP"][defancer] -= damage
    print("{0} -> {1} || Damage: {2}, {3}'s new HP: {4}\n"
          .format(data["Chars"][attacker], 
                  data["Chars"][defancer], 
                  damage, 
                  data["Chars"][defancer], 
                  data["HP"][defancer]))
    
def heal(attacker):
    data["HP"][attacker] += 25*round
    print("{0}'s new HP: {1}\n"
          .format(data["Chars"][attacker],
                  data["HP"][attacker]))

def attackBoost(attacker):
    data["Atk"][attacker] += 15*round
    print("{0}'s new Atk: {1}\n"
          .format(data["Chars"][attacker],
                  data["Atk"][attacker]))


round = 0

# Program Start
while True:
    print("_" * 30)
    view = int(input("-- Main Page --\n1- Play!\n2- Add Character\n3- Quit\nChoose-- "))

    # Play!
    if view == 1:
        print("_" * 30)
        

        print(data["Chars"])

        player1 = int(input("\n(1. Player) Choose your character number! - "))
        print(data["Chars"][player1])


        player2 = int(input("(2. Player) Choose your character number! - "))
        print(data["Chars"][player2])

        print("_" * 30)
        print("-- Game Starting --")
        
        # Game Start
        while True:    
            round += 1

            print("_" * 30,"\n-- Choosing -- round: {0}\n1- Attack\n2- Heal\n3- Attack Boost\n".format(round))

            # Player 1
            while True:
                mode = int(input("Choose a mode! (1)- "))

                if mode == 1: 
                    attack(player1, player2)
                    break
                elif mode == 2:
                    heal(player1)
                    break
                elif mode == 3:
                    attackBoost(player1)
                    break
                else:
                    print("invalid number")
        
            if data["HP"][player2] <= 0:
                print("{0} (player1) won the game".format(data["Chars"][player1]))
                print("_" * 30)
                break
            
            # Player 2
            while True:
                mode = int(input("Choose a mode! (2)- "))

                if mode == 1:
                    attack(player2,player1)
                    break
                elif mode == 2:
                    heal(player2)
                    break    
                elif mode == 3:
                    attackBoost(player2)
                    break
                else:
                    print("invalid number")
            
            if data["HP"][player1] <= 0:
                print("{0} (player2) won the game".format(data["Chars"][player2]))
                print("_" * 30)
                break
            


    # Character Add
    elif view == 2:
        print("_" * 30)
        print("-- Character Adding Screen --")

        name = input("Name: ")
        HP = int(input("HP: "))
        Atk = int(input("Atk: "))
        Def = int(input("Def: "))

        newChar = {"Chars":[name], "HP":[HP], "Atk":[Atk], "Def":[Def]}
        newData = pd.DataFrame(data=newChar)

        data = pd.concat([data, newData], ignore_index=True)
        data.to_excel("characters.xlsx")

        
        data = pd.read_excel("characters.xlsx", index_col=0)
        

        print(data[["Chars", "Atk", "HP", "Def"]].to_string(index=False))

        # Excel Arangement
        wb = load_workbook('characters.xlsx')
        ws = wb['Sheet1']
        ws.delete_cols(1)
        wb.save("characters.xlsx")


    # Quit
    elif view == 3:
        print("Program closed")
        break

