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
            self.id = re.findall(r'(\d+)(?>_)', var)[0]
    
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
                decode[search][x] = random.randint(49000,99999)
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
            blocked = ["plant_pot3", 
                       "plant_pot4", 
                       "plant_pot5", 
                       "Motorcycle",
                       "plant_pot6", 
                       "plant_pot7"]


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
    def __modmoneys(path, key, referens=''):
        pass
    
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
        ModArchifrex._ModArchifrex__archive(self.path, r'(\d+_(gems|last_gems).*?=")-*\d+', r'\g<1>'+str(random.randint(60000000,90000000))) 
    def plots(self): 
        ModArchifrex._ModArchifrex__modplots(f'/data/data/com.ChillyRoom.DungeonShooter/files/item_data_{self.id}_.data', b'iambo\x00\x00\x00')
    def materials(self):
        ModArchifrex._ModArchifrex__modmaterial(f'/data/data/com.ChillyRoom.DungeonShooter/files/item_data_{self.id}_.data', b'iambo\x00\x00\x00')
    def seeds(self):
        ModArchifrex._ModArchifrex__modseeds(f'/data/data/com.ChillyRoom.DungeonShooter/files/item_data_{self.id}_.data', b'iambo\x00\x00\x00')
    def blueprints(self):
        ModArchifrex._ModArchifrex__modblueprints(f'/data/data/com.ChillyRoom.DungeonShooter/files/item_data_{self.id}_.data', b'iambo\x00\x00\x00')
    def money(self):
        ModArchifrex._ModArchifrex__modmoneys(f'/data/data/com.ChillyRoom.DungeonShooter/files/season_data_{self.id}_.data')
    def weapons(self):
        ModArchifrex._ModArchifrex__modweapons(f'/data/data/com.ChillyRoom.DungeonShooter/files/statistic_{self.id}_.data', b'crst1\x00\x00\x00')



