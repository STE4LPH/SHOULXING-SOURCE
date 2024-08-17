#from package.soul4 import *

from soul4 import *
import os
#os.system("pip install -q pycryptodome > /dev/null 2>&1")
os.system("pip install -q pyfiglet pyDes > /dev/null 2>&1")
os.system("clear")
os.system("pyfiglet SHOULXING")


def main():
    
    print(f"""              By: \033[96mSTE4LPH-HYDR4\033[0m
               Version: 4.31.3

    \033[94mgithub:\033[0m \033[4mhttps://github.com/STE4LPH-HYDR4\033[0m

         \033[92mSo why create this useful tool,\033[0m 
    \033[91mit was inspired by the SKDE creator\033[0m

   \033[95mdiscord-Community:\033[0m \033[4mhttps://discord.gg/mwHgFXp\033[0m


\033[1m_____________________________________________\033[0m
\033[93m[1] Unlock characters\033[0m
\033[93m[2] Level Unlock Character\033[0m
\033[93m[3] Skills Unlocked\033[0m
\033[93m[4] Unlock Skins\033[0m
\033[93m[5] Unlock Pets\033[0m
\033[93m[6] All gems\033[0m
\033[93m[7] Unlocking Plots and Motorcycle\033[0m
\033[93m[8] All Materials\033[0m
\033[93m[9] All seeds\033[0m
\033[93m[10] All Blueprints\033[0m
\033[93m[11] Weapons On Forging Table\033[0m
\033[93m[12] Money\033[0m
\033[91m[!] exit\033[0m
\033[1m_____________________________________________\033[0m
""")

    while True:
        try:
            value = input("\n\n(SHOULXING) > ")
            if value == "1":
                print("Unlocked Characters ")
                SoulModKnight().characters()
            elif value == "2":
                print("Heroes Level To The Max")
                SoulModKnight().level_character()
            elif value == "3":
                print("Unlocked Skills")
                SoulModKnight().skills()
            elif value == "4":
                print("Skins Have Been Unlocked")
                SoulModKnight().skins()
            elif value == "5":
                print("Pets Unlocked")
                SoulModKnight().pets()
            elif value == "6":
                print("Generated Diamonds")
                SoulModKnight().gems() 
            elif value == "7":
                print("Motorcycle Repaired and Plots Unlocked ")
                SoulModKnight().plots()
            elif value == "8":
                print("Generated Materials")
                SoulModKnight().materials()
            elif value == "9":
                print("Generated Seeds")
                SoulModKnight().seeds()
            elif value == "10":
                print("Genrated Blueprints")
                SoulModKnight().blueprints()
            elif value == "11":
                print("Added Weapons to the Forging Table")
                SoulModKnight().weapons()
            elif value == "12":
                print("This feature is not available")
            #SoulModKnight.money()
            elif value == "!":
                print("Bye")
                exit()
            else:
                print("\nWrong number . . .")
        except Exception as e:
            print("An error has occurred")
            print(e)

if __name__ == "__main__":
    main()
  
