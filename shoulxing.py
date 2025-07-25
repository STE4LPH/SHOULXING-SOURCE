#from package.soul4 import *

from soul4 import *
import os
#os.system("pip install -q pycryptodome > /dev/null 2>&1")
try:
    import pyfiglet
except ImportError:
    print("pyfiglet library is not installed.")
    choice = input("Do you want to install? (y/n): ")
    if choice.lower() == 'y':
        os.system("pip install pyfiglet")
    else:
        print("Exiting...")
        exit()
os.system("clear")
os.system("pyfiglet SHOULXING")


def main():
    try:
        mod_instance = SoulModKnight()
        player_id = mod_instance.id
    except FileNotFoundError:
        print("\033[91m[ERROR] Could not find the playerprefs.xml file.\033[0m")
        print("Please make sure the path in soul4.py is correct and the game is installed.")
        return
    except IndexError:
        print("\033[91m[ERROR] Could not find player ID in the file.\033[0m")
        print("The playerprefs.xml file may be corrupt or empty.")
        return
    
    print(f"""              By: \033[96mSTE4LPH-HYDR4\033[0m
               Version: 4.31.3

    \033[94mgithub:\033[0m \033[4mhttps://github.com/STE4LPH-HYDR4\033[0m

         \033[92mSo why create this useful tool,\033[0m
    \033[91mit was inspired by the SKDE creator\033[0m

   \033[95mdiscord-Community:\033[0m \033[4mhttps://discord.gg/mwHgFXp\033[0m


\033[1m_____________________________________________\033[0m
    \033[92mCURRENT PLAYER ID: {player_id}\033[0m
\033[1m_____________________________________________\033[0m
\033[93m[1] Unlock Characters\033[0m
\033[93m[2] Max Out Character Levels\033[0m
\033[93m[3] Unlock All Skills\033[0m
\033[93m[4] Unlock All Skins\033[0m
\033[93m[5] Unlock All Pets\033[0m
\033[93m[6] Get Max Gems\033[0m
\033[93m[7] Unlock All Plots & Motorcycle\033[0m
\033[93m[8] Get All Materials\033[0m
\033[93m[9] Get All Seeds\033[0m
\033[93m[10] Get All Blueprints\033[0m
\033[93m[11] Add Weapons to Forging Table\033[0m
\033[93m[12] Set Season Coins\033[0m
\033[93m[13] Max Evolvable Weapons\033[0m
\033[93m[14] Unlock & Max All Chips\033[0m
\033[93m[15] Unlock & Max Followers\033[0m
\033[93m[16] Unlock & Max Mounts\033[0m
\033[91m[!] exit\033[0m
\033[1m_____________________________________________\033[0m
""")

    while True:
        try:
            value = input("\n\n(SHOULXING) > ")
            if value == "1":
                print("Characters Unlocked.")
                mod_instance.characters()
            elif value == "2":
                print("Heroes leveled to the max.")
                mod_instance.level_character()
            elif value == "3":
                print("Skills Unlocked.")
                mod_instance.skills()
            elif value == "4":
                print("Skins have been unlocked.")
                mod_instance.skins()
            elif value == "5":
                print("Pets unlocked.")
                mod_instance.pets()
            elif value == "6":
                print("Gems generated.")
                mod_instance.gems()
            elif value == "7":
                print("Motorcycle repaired and plots unlocked.")
                mod_instance.plots()
            elif value == "8":
                print("Materials generated.")
                mod_instance.materials()
            elif value == "9":
                print("Seeds generated.")
                mod_instance.seeds()
            elif value == "10":
                print("Blueprints generated.")
                mod_instance.blueprints()
            elif value == "11":
                print("Weapons added to the Forging Table.")
                mod_instance.weapons()
            elif value == "12":
                amount = int(input("Enter the coin you want (ex: 999999): ").strip())
                mod_instance.money(amount)
            elif value == "13":
                mod_instance.evolve_weapons()
            elif value == "14":
                mod_instance.max_chips()
            elif value == "15":
                mod_instance.max_followers()
            elif value == "16":
                mod_instance.max_mounts()
            elif value == "!":
                print("Bye")
                exit()
            else:
                print("\nInvalid option...")
        except Exception as e:
            print("An error has occurred")
            print(e)

if __name__ == "__main__":
    main()