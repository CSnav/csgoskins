import requests
import time
import json
import uuid

def makeAPICall():
    res = requests.get('http://csgobackpack.net/api/GetItemsList/v2/?prettyprint=1&no_prices=1')
    if res.ok:
        return res.json().get("items_list", {})
    else:
        print(f'{res.status_code}: {res.text}')
        return {}

def getData(): 
    data = makeAPICall()
    assert(data)
    guns = []
    gloves = []
    knives = []
    pk = 1
    for item_name in data:
        item_type = data.get(item_name, {}).get("type", "")
        if(item_type == "Weapon"):
            weapon_type = data.get(item_name, {}).get("weapon_type", "")
            if(weapon_type == "Knife"):
                formatted_payload = processKnife(data.get(item_name, {}), pk)
                pk += 1
                knives.append(formatted_payload)
            else:
                formatted_payload = processGun(data.get(item_name, {}), pk)
                pk += 1
                guns.append(formatted_payload)
        elif(item_type == "Gloves"):
            formatted_payload = processGloves(data.get(item_name, {}), pk)
            pk += 1
            gloves.append(formatted_payload)			
    with open("gloves.json", "w") as fp:
        json.dump(gloves, fp, indent=2)
    with open("guns.json", "w") as fp:
        json.dump(guns, fp, indent=2)
    with open("knives.json", "w") as fp:
        json.dump(knives, fp, indent=2)
    
    
def processGun(raw_payload, pk):
    formatted_payload = {}
    formatted_payload['model'] = "skin_details.GunSkin"
    formatted_payload['pk'] = pk 
    formatted_payload['fields'] = {}
    formatted_payload['fields']['icon_url'] = raw_payload.get("icon_url", "")
    formatted_payload['fields']['icon_url_large'] = raw_payload.get("icon_url_large", "")
    formatted_payload['fields']['weapon_type'] = raw_payload.get("weapon_type", "")
    formatted_payload['fields']['gun_type']  = raw_payload.get("gun_type", "")
    formatted_payload['fields']['exterior'] = raw_payload.get("exterior", "")
    formatted_payload['fields']['rarity'] = raw_payload.get("rarity", "")
    formatted_payload['fields']['rarity_color'] = raw_payload.get("rarity_color", "")
    formatted_payload['fields']['stattrak'] = raw_payload.get("stattrak", 0)
    formatted_payload['fields']['souvenir'] = raw_payload.get("souvenir", 0)
    name = raw_payload.get("name", "")
    formatted_payload['fields']['name'] = name 
    # if(r'\u2605 ' in name):
    # 	name = name.replace(r'\u2605 ', '')	
    # if(r'\u2122' in name):
    # 	name = name.replace(r'\u2122', '')
    # if(r'\u00f6' in name):
    # 	name = name.replace(r'\u00f6', 'o')
    # if(r'\u58f1 ' in name):
    # 	name = name.replace(r'\u58f1 ', '')
    # if(r'\u5f10 ' in name):
    # 	name = name.replace(r'\u5f10 ', '')
    return formatted_payload

def processKnife(raw_payload, pk):
    formatted_payload = {}
    formatted_payload['model'] = "skin_details.KnifeSkin"
    formatted_payload['pk'] = pk 
    formatted_payload['fields'] = {}
    formatted_payload['fields']['icon_url'] = raw_payload.get("icon_url", "")
    formatted_payload['fields']['icon_url_large'] = raw_payload.get("icon_url_large", "")
    if(formatted_payload['fields']['icon_url_large'] == None):
        formatted_payload['fields']['icon_url_large'] = ""
    formatted_payload['fields']['weapon_type'] = raw_payload.get("weapon_type", "")
    formatted_payload['fields']['knife_type']  = raw_payload.get("knife_type", "")
    formatted_payload['fields']['exterior'] = raw_payload.get("exterior", "")
    formatted_payload['fields']['rarity'] = raw_payload.get("rarity", "")
    formatted_payload['fields']['rarity_color'] = raw_payload.get("rarity_color", "")
    formatted_payload['fields']['stattrak'] = raw_payload.get("stattrak", 0)
    name = raw_payload.get("name", "")
    formatted_payload['fields']['name'] = name 
    if("Battle-Scarred" in name):
        formatted_payload['fields']['exterior'] = "Battle-Scarred"
    elif("Well-Worn" in name):
        formatted_payload['fields']['exterior'] = "Well-Worn"
    elif("Field-Tested" in name):
        formatted_payload['fields']['exterior'] = "Field-Tested"
    elif("Minimal Wear" in name):
        formatted_payload['fields']['exterior'] = "Minimal Wear"
    elif("Factory New" in name):
        formatted_payload['fields']['exterior'] = "Factory New"
    #    print(formatted_payload) 
    return formatted_payload

def processGloves(raw_payload, pk):
    formatted_payload = {}
    formatted_payload['model'] = "skin_details.GloveSkin"
    formatted_payload['pk'] = pk 
    formatted_payload['fields'] = {}
    formatted_payload['fields']['icon_url'] = raw_payload.get("icon_url", "")
    formatted_payload['fields']['icon_url_large'] = raw_payload.get("icon_url_large", "")
    formatted_payload['fields']['exterior'] = raw_payload.get("exterior", "")
    formatted_payload['fields']['rarity'] = raw_payload.get("rarity", "")
    formatted_payload['fields']['rarity_color'] = raw_payload.get("rarity_color", "")	
    name = raw_payload.get("name", "")
    formatted_payload['fields']['name'] = name 
    if("Battle-Scarred" in name):
        formatted_payload['fields']['exterior'] = "Battle-Scarred"
    elif("Well-Worn" in name):
        formatted_payload['fields']['exterior'] = "Well-Worn"
    elif("Field-Tested" in name):
        formatted_payload['fields']['exterior'] = "Field-Tested"
    elif("Minimal Wear" in name):
        formatted_payload['fields']['exterior'] = "Minimal Wear"
    elif("Factory New" in name):
        formatted_payload['fields']['exterior'] = "Factory New"
    return formatted_payload

def main():
    getData()

if __name__ == "__main__":
    main()
