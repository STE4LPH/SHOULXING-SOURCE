from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad, pad
import re, os, json, base64, unicodedata
import random
import things
import xml.etree.ElementTree as ET
class ModArchifrex:
    key = [115, 108, 99, 122, 125, 103, 117, 99, 127, 87, 109, 108, 107, 74, 95]
    
    def __init__(self, path='/data/data/com.ChillyRoom.DungeonShooter/shared_prefs/com.ChillyRoom.DungeonShooter.v2.playerprefs.xml'):
        self.path = path

        with open(path,'r') as file:
            var = file.read()
            self.id = re.findall(r'<string name="last_chilly_uid">(\d+)</string>', var)[0]
            #self.id = re.findall(r'(\d+)(?>_)', var)[0]
    
    """archive -> playerprefs.xml"""    
    @staticmethod
    def __archive(path, regex, mody):
        with open(path, "r+") as file:
            code = file.read()
            mod = re.sub(regex, mody, code)    
            mody = code.replace(code, mod) 
            file.seek(0)
            file.write(mody)
            file.truncate()
    
    @staticmethod
    def __level(path, regex):
        with open(path, 'r+') as file:
            code = file.read()
            values = re.findall(r'c\d+_level.*?="\d+"', code)
            c_level = ['c0','c2','c3','c5','c8','c10','c14','c15']
            for x in values:
                if x.split('_')[0] in c_level:
                    mod = re.sub(r'(c\d+_level.*?=")\d+',r'\g<1>8',x)
                else:
                    mod = re.sub(r'(c\d+_level.*?=")\d+',r'\g<1>7',x)
                code = code.replace(x, mod)
            file.seek(0)
            file.write(code)
            file.truncate()


    """archive -> items.data"""
    @staticmethod
    def __modencrypt(path, key):
        with open(path, 'rb') as file:
            data_cifre = file.read()
            decode = base64.b64decode(data_cifre)
        cipher = DES.new(key,DES.MODE_CBC, iv=b'Ahbool\x00\x00')
        decrypte_data = unpad(cipher.decrypt(decode), DES.block_size)

        return decrypte_data
    
    @staticmethod
    def __modcrypthed(path, decode, items, file, key, search):        
        for i in items:
            if i in decode[search]:
                pass
            else:
                decode[search].extend([i])
                file.seek(0)
            json.dump(decode, file, indent=4)
            file.truncate()
        
        with open(path, 'r+') as target:
            modified_content = target.read()        
            data_bytes = modified_content.encode()
            cipher = DES.new(key, DES.MODE_CBC, b'Ahbool\x00\x00')
            ciphertext = cipher.encrypt(pad(data_bytes, DES.block_size))
            encoded_ciphertext = base64.b64encode(ciphertext)
            target.seek(0)
            target.write(encoded_ciphertext.decode())
            target.truncate()

    @staticmethod       
    def __modcrypthed_dic(path, decode, items, file, key, search):
        decode[search] = items
        for x,y in decode[search].items():
            if y == "?":
                decode[search][x] = 50000;
                #decode[search][x] = random.randint(49000,99999)
            else:
                continue

        file.seek(0)
        json.dump(decode, file, indent=4)
        file.truncate()

       # Hacer quw  se agregue ños materiales 
        with open(path, 'r+') as target:
            modified_content = target.read()        
            data_bytes = modified_content.encode()
            cipher = DES.new(key, DES.MODE_CBC, b'Ahbool\x00\x00')
            ciphertext = cipher.encrypt(pad(data_bytes, DES.block_size))
            encoded_ciphertext = base64.b64encode(ciphertext)
            target.seek(0)
            target.write(encoded_ciphertext.decode())
            target.truncate()  
    

    #Modicando  archivos

    @staticmethod
    def __modplots(path, key, referens='itemUnlock'):
        data_plot = ModArchifrex.__modencrypt(path, key)
        json_data = json.loads(data_plot.decode())        
        with open(path, 'w') as target:
            blocked = [
                "plant_pot3", 
                "plant_pot4", 
                "plant_pot5", 
                "plant_pot6", 
                "plant_pot7",
                "Motorcycle"
            ]

            ModArchifrex.__modcrypthed(path, json_data, blocked, target, key, referens)

    @staticmethod
    def __modmaterial(path, key, referens='materials'):
        data_materials = ModArchifrex.__modencrypt(path, key)
        json_data = json.loads(data_materials.decode())
        with open(path, 'w') as target:
            all_material = things.items_materials

            ModArchifrex.__modcrypthed_dic(path, json_data, all_material, target, key, referens)

    @staticmethod
    def __modseeds(path, key, referens='seeds'):
        data_seeds = ModArchifrex.__modencrypt(path, key)
        json_data = json.loads(data_seeds.decode())
        with open(path, 'w') as target:
            all_seeds = things.items_plants

            ModArchifrex.__modcrypthed_dic(path, json_data, all_seeds, target, key, referens)

    @staticmethod
    def __modblueprints(path, key, referens='blueprints'):
        data_blueprints = ModArchifrex.__modencrypt(path, key)
        json_data = json.loads(data_blueprints.decode())
        with open(path, 'w') as target:
            all_blueprints = things.blueprints
            
            ModArchifrex.__modcrypthed_dic(path, json_data, all_blueprints, target, key, referens)
    
    @staticmethod
    def __modweapons(path, key, referens='object2ObtainTime'):
        data_weapons = ModArchifrex.__modencrypt(path,key)
        json_data = json.loads(data_weapons.decode())
        pattern = re.compile(r'\bweapon_\w+\b')
        
        for x,y in json_data[referens].items():
            if pattern.match(x):
                json_data[referens][x]= random.randint(10, 99)
            else:
                pass
        with open(path, 'r+') as file:
            file.seek(0)
            json.dump(json_data, file, indent=4,ensure_ascii=False)
            file.truncate()

        with open(path, 'r+') as target:
            modified_content = target.read()        
            data_bytes = modified_content.encode()
            cipher = DES.new(key, DES.MODE_CBC, b'Ahbool\x00\x00')
            ciphertext = cipher.encrypt(pad(data_bytes, DES.block_size))
            encoded_ciphertext = base64.b64encode(ciphertext)
            target.seek(0)
            target.write(encoded_ciphertext.decode())
            target.truncate()
    
    
    @staticmethod
    def __modskills(path, ids):
        tree = ET.parse(path)
        root = tree.getroot()
        with open(path, 'r+') as file:
            text = file.read()
        for skill in things.skills:
            if re.search(skill, text):
                pass
            else:
                new_int = ET.Element('int', {'name': f'{ids}_{skill}', 'value': '1'})
                root.append(new_int)            
                tree.write(path)
               
    @staticmethod
    def __modseasoncoin(path, key, amount):
        decrypte_data = ModArchifrex._ModArchifrex__modencrypt(path, key)
        json_data = json.loads(decrypte_data.decode())

        json_data['coin'] = amount
        print(f"Season coins set to: {amount}")

        temp_path = path + ".tmp"
        with open(temp_path, 'w') as file:
            json.dump(json_data, file, indent=4)

        with open(temp_path, 'r') as target:
            modified_content = target.read()
            data_bytes = modified_content.encode()
            cipher = DES.new(key, DES.MODE_CBC, b'Ahbool\x00\x00')
            ciphertext = cipher.encrypt(pad(data_bytes, DES.block_size))
            encoded_ciphertext = base64.b64encode(ciphertext)

        with open(path, 'w') as final_file:
            final_file.write(encoded_ciphertext.decode())
            final_file.truncate()
        
        os.remove(temp_path)
    
    @staticmethod
    def __modevolveweapons(path, key):
        try:
            decrypte_data = ModArchifrex._ModArchifrex__modencrypt(path, key)
            json_data = json.loads(decrypte_data.decode())
        except FileNotFoundError:
            print(f"\033[91m[ERROR] File not found: {path}\033[0m")
            print("You may need to play a run with an evolvable weapon first.")
            return
        except Exception as e:
            print(f"\033[91m[ERROR] Decryption failed. The key is likely incorrect.\033[0m")
            print(f"Details: {e}")
            return

        weapons_dict = json_data.get("weapons", {})

        for weapon_name in things.evolvable_weapons:
            skin_name = f"{weapon_name}_s_1"
            
            if weapon_name in weapons_dict:
                weapons_dict[weapon_name]["Level"] = 7
                weapons_dict[weapon_name]["CurrentSkinIndex"] = 1
                if skin_name not in weapons_dict[weapon_name]["UnlockedSkins"]:
                    weapons_dict[weapon_name]["UnlockedSkins"].append(skin_name)
            else:
                weapons_dict[weapon_name] = {
                    "Name": weapon_name,
                    "Level": 7,
                    "CurrentSkinIndex": 1,
                    "UnlockedSkins": [skin_name]
                }
        
        json_data["weapons"] = weapons_dict

        temp_path = path + ".tmp"
        with open(temp_path, 'w') as file:
            json.dump(json_data, file, indent=4)

        with open(temp_path, 'r') as target:
            modified_content = target.read()
            data_bytes = modified_content.encode()
            cipher = DES.new(key, DES.MODE_CBC, b'Ahbool\x00\x00')
            ciphertext = cipher.encrypt(pad(data_bytes, DES.block_size))
            encoded_ciphertext = base64.b64encode(ciphertext)

        with open(path, 'w') as final_file:
            final_file.write(encoded_ciphertext.decode())
            final_file.truncate()
            
        os.remove(temp_path)
        print("Evolvable weapons have been maxed out!")
    
    @staticmethod
    def __modchips(path, key):
        try:
            decrypte_data = ModArchifrex._ModArchifrex__modencrypt(path, key)
            json_data = json.loads(decrypte_data.decode())
        except Exception as e:
            print(f"\033[91m[ERROR] Failed to read or decrypt season_data.\033[0m")
            print(f"Details: {e}")
            print("The decryption key is likely incorrect.")
            return

        existing_chips = json_data.get("chips", [])
        processed_chips = {chip["chipName"]: chip for chip in existing_chips}

        for chip_name in things.chip_list:
            processed_chips[chip_name] = {
                "chipName": chip_name,
                "level": 10,
                "refineLevel": 10
            }
        
        json_data["chips"] = list(processed_chips.values())

        temp_path = path + ".tmp"
        with open(temp_path, 'w') as file:
            json.dump(json_data, file, indent=4)

        with open(temp_path, 'r') as target:
            modified_content = target.read()
            data_bytes = modified_content.encode()
            cipher = DES.new(key, DES.MODE_CBC, b'Ahbool\x00\x00')
            ciphertext = cipher.encrypt(pad(data_bytes, DES.block_size))
            encoded_ciphertext = base64.b64encode(ciphertext)

        with open(path, 'w') as final_file:
            final_file.write(encoded_ciphertext.decode())
            final_file.truncate()
            
        os.remove(temp_path)
        print("All season chips have been unlocked and maxed out!")
        
    @staticmethod
    def __modfollowers(path, key):
        try:
            decrypte_data = ModArchifrex._ModArchifrex__modencrypt(path, key)
            json_data = json.loads(decrypte_data.decode())
        except Exception as e:
            print(f"\033[91m[ERROR] Failed to read or decrypt season_data.\033[0m\nDetails: {e}")
            return

        follower_data = json_data.setdefault("comboGunData", {}).setdefault("followerData", {})
        existing_followers = follower_data.get("followerList", [])
        processed_followers = {f["followerConfigId"]: f for f in existing_followers}

        for follower_name in things.follower_list:
            processed_followers[follower_name] = {
                "followerConfigId": follower_name,
                "level": 4
            }
        
        follower_data["followerList"] = list(processed_followers.values())
        
        temp_path = path + ".tmp"
        with open(temp_path, 'w') as file:
            json.dump(json_data, file, indent=4)
        with open(temp_path, 'r') as target:
            modified_content = target.read()
            data_bytes = modified_content.encode()
            cipher = DES.new(key, DES.MODE_CBC, b'Ahbool\x00\x00')
            ciphertext = cipher.encrypt(pad(data_bytes, DES.block_size))
            encoded_ciphertext = base64.b64encode(ciphertext)
        with open(path, 'w') as final_file:
            final_file.write(encoded_ciphertext.decode())
            final_file.truncate()
        os.remove(temp_path)
        print("All followers have been unlocked and maxed out!")

    @staticmethod
    def __modmounts(path, key):
        try:
            decrypte_data = ModArchifrex._ModArchifrex__modencrypt(path, key)
            json_data = json.loads(decrypte_data.decode())
        except Exception as e:
            print(f"\033[91m[ERROR] Failed to read or decrypt season_data.\033[0m\nDetails: {e}")
            return

        mount_data = json_data.setdefault("comboGunData", {}).setdefault("mountData", {})
        existing_mounts = mount_data.get("mountList", [])
        processed_mounts = {m["id"]: m for m in existing_mounts}
        
        for mount_name in things.mount_list:
            processed_mounts[mount_name] = {
                "id": mount_name,
                "index": 0,
                "level": 4
            }
            
        mount_data["mountList"] = list(processed_mounts.values())
        
        temp_path = path + ".tmp"
        with open(temp_path, 'w') as file:
            json.dump(json_data, file, indent=4)
        with open(temp_path, 'r') as target:
            modified_content = target.read()
            data_bytes = modified_content.encode()
            cipher = DES.new(key, DES.MODE_CBC, b'Ahbool\x00\x00')
            ciphertext = cipher.encrypt(pad(data_bytes, DES.block_size))
            encoded_ciphertext = base64.b64encode(ciphertext)
        with open(path, 'w') as final_file:
            final_file.write(encoded_ciphertext.decode())
            final_file.truncate()
        os.remove(temp_path)
        print("All mounts have been unlocked and maxed out!")


class SoulModKnight(ModArchifrex):
    def characters(self):
        ModArchifrex._ModArchifrex__archive(self.path, r'(c\d+_unlock)">False', r'\1">True')
    def level_character(self):
        ModArchifrex._ModArchifrex__level(self.path, r'(c\d+_level.*?=")\d+')
    def skills(self):
        ModArchifrex._ModArchifrex__archive(self.path, r'(c_\w+_skill.*?=")-*\d+',r'\g<1>1')
        ModArchifrex._ModArchifrex__modskills(self.path, self.id)
    def skins(self):
        ModArchifrex._ModArchifrex__archive(self.path, r'(c\d+_skin.*?=")-*\d+', r'\g<1>1')
    def pets(self):
        ModArchifrex._ModArchifrex__archive(self.path, r'(p\d+_unlock.*?")>False', r'\1>True') 
    def gems(self):        
        ModArchifrex._ModArchifrex__archive(self.path, r'(\d+_(gems|last_gems).*?=")-*\d+', r'\g<1>'+str(1000000000)) 
    def plots(self): 
        ModArchifrex._ModArchifrex__modplots(f'/data/data/com.ChillyRoom.DungeonShooter/files/item_data_{self.id}_.data', b'iambo\x00\x00\x00')
    def materials(self):
        ModArchifrex._ModArchifrex__modmaterial(f'/data/data/com.ChillyRoom.DungeonShooter/files/item_data_{self.id}_.data', b'iambo\x00\x00\x00')
    def seeds(self):
        ModArchifrex._ModArchifrex__modseeds(f'/data/data/com.ChillyRoom.DungeonShooter/files/item_data_{self.id}_.data', b'iambo\x00\x00\x00')
    def blueprints(self):
        ModArchifrex._ModArchifrex__modblueprints(f'/data/data/com.ChillyRoom.DungeonShooter/files/item_data_{self.id}_.data', b'iambo\x00\x00\x00')
    def money(self, amount=999999):
        key = b'iambo\x00\x00\x00' 
        path = f'/data/data/com.ChillyRoom.DungeonShooter/files/season_data_{self.id}_.data'      
        ModArchifrex._ModArchifrex__modseasoncoin(path, key, amount)
    def weapons(self):
        ModArchifrex._ModArchifrex__modweapons(f'/data/data/com.ChillyRoom.DungeonShooter/files/statistic_{self.id}_.data', b'crst1\x00\x00\x00')
    def evolve_weapons(self):
        key = b'iambo\x00\x00\x00'
        path = f'/data/data/com.ChillyRoom.DungeonShooter/files/weapon_evolution_data_{self.id}_.data'
        ModArchifrex._ModArchifrex__modevolveweapons(path, key)
    def max_chips(self):
        key = b'iambo\x00\x00\x00'
        path = f'/data/data/com.ChillyRoom.DungeonShooter/files/season_data_{self.id}_.data'
        ModArchifrex._ModArchifrex__modchips(path, key)
    def max_followers(self):
        key = b'iambo\x00\x00\x00'
        path = f'/data/data/com.ChillyRoom.DungeonShooter/files/season_data_{self.id}_.data'
        ModArchifrex._ModArchifrex__modfollowers(path, key)
    def max_mounts(self):
        key = b'iambo\x00\x00\x00'
        path = f'/data/data/com.ChillyRoom.DungeonShooter/files/season_data_{self.id}_.data'
        ModArchifrex._ModArchifrex__modmounts(path, key)