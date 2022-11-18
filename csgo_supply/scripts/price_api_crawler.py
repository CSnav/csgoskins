import requests, json, copy
from options import GT_CHOICES, KN_CHOICES, GL_CHOICES
from apiinfo import BITSKINS_API_KEY, get_bitskins_code
# All helper functions return a dict in the form of 
# { "gun": [{ "name": name,
#             "price": price },
#           {...}, ...]
# { "knives": [{ "name": name,
#                "price": price},
#              {...}, ...]
# { "gloves": [{ "name": name,
#                "price": price},
#              {...}, ...]


def get_cs_deals_prices():
    headers = { 'content_type': 'application/json' }
    body = { "appid": 730 }
    request = requests.get(url="https://cs.deals/API/IPricing/GetLowestPrices/v1",
                           headers=headers,
                           json=body)
    if(request.status_code != 200):
        return []
    raw_data = request.json().get("response", {}).get("items", [])
    ret = { "guns": [],
            "knives": [],
            "gloves": [] } 
    for item in raw_data:
        for gun in GT_CHOICES:
            if gun in item.get("marketname", ""):
                ret['guns'].append({"name": item['marketname'],
                                    "price": (item.get('lowest_price', None) or "0.0000")[:-2]})
        for knife in KN_CHOICES:
            if knife in item.get("marketname", ""):
                ret['knives'].append({"name": item['marketname'],
                                      "price": (item.get('lowest_price', None) or "0.0000")[:-2]})
        for gloves in GL_CHOICES:
            if gloves in item.get("marketname", ""):
                ret['gloves'].append({"name": item['marketname'],
                                      "price": (item.get('lowest_price', None) or "0.0000")[:-2]})
    print(ret)
    return(ret)

def get_skinport_prices():
    headers = { 'content_type': 'application/json' }
    params = "app_id=730&currency=USD&tradable=true"
    request = requests.get(url=f"https://api.skinport.com/v1/items?{params}",
                           headers=headers)
    if(request.status_code != 200):
        return []
    raw_data = request.json()
    ret = { "guns": [],
            "knives": [],
            "gloves": [] } 
    for item in raw_data:
        for gun in GT_CHOICES:
            if gun in item.get("market_hash_name", ""):
                ret['guns'].append({"name": item['market_hash_name'],
                                    "price": '%.2f' % (item.get('min_price', None) or 0.00)})
        for knife in KN_CHOICES:
            if knife in item.get("market_hash_name", ""):
                ret['knives'].append({"name": item['market_hash_name'],
                                      "price": '%.2f' % (item.get('min_price', None) or 0.00)})
        for gloves in GL_CHOICES:
            if gloves in item.get("market_hash_name", ""):
                ret['gloves'].append({"name": item['market_hash_name'],
                                      "price": '%.2f' % (item.get('min_price', None) or 0.00)})
    print(ret)
    return(ret)

def get_bitskins_prices():
    headers = { 'content_type': 'application/json' }
    params = f"api_key={BITSKINS_API_KEY}&code={get_bitskins_code()}&app_id=730"
    request = requests.get(url=f"https://bitskins.com/api/v1/get_price_data_for_items_on_sale/?{params}",
                           headers=headers)
    if(request.status_code != 200):
        return []
    raw_data = request.json().get("data", {}).get("items", [])
    ret = { "guns": [],
            "knives": [],
            "gloves": [] } 
    for item in raw_data:
        for gun in GT_CHOICES:
            if gun in item.get("market_hash_name", ""):
                ret['guns'].append({"name": item['market_hash_name'],
                                    "price": item.get('lowest_price', None) or  '0.00'})
        for knife in KN_CHOICES:
            if knife in item.get("market_hash_name", ""):
                ret['knives'].append({"name": item['market_hash_name'],
                                      "price": item.get('lowest_price', None) or  '0.00'})
        for gloves in GL_CHOICES:
            if gloves in item.get("market_hash_name", ""):
                ret['gloves'].append({"name": item['market_hash_name'],
                                      "price": item.get('lowest_price', None) or  '0.00'})
    return(ret)

def combine_prices():
    cs_deals = get_cs_deals_prices()
    skinport = get_skinport_prices()
    bitskins = get_bitskins_prices()
    ret = { "guns": {},
            "knives": {},
            "gloves": {} } 
    for item_category in cs_deals:
        for item in cs_deals[item_category]:
            if(item.get("name") not in ret[item_category]):
                ret[item_category][item.get("name")] = {}
            ret[item_category][item.get("name")]["cs_deals"] = item.get("price")
        for item in skinport[item_category]:
            if(item.get("name") not in ret[item_category]):
                ret[item_category][item.get("name")] = {}
            ret[item_category][item.get("name")]["skinport"] = item.get("price")
        for item in bitskins[item_category]:
            if(item.get("name") not in ret[item_category]):
                ret[item_category][item.get("name")] = {}
            ret[item_category][item.get("name")]["bitskins"] = item.get("price")
    with open("prices.json", "w") as fp:
        json.dump(ret, fp, indent=2)
    return(ret)
 
if __name__ == "__main__":
    combine_prices()

# conn = http.client.HTTPSConnection("cs.deals")
# 
# payload = "{\"appid\":730}"
# 
# headers = { 'content-type': "application/json" }
# 
# conn.request("POST", "/API/IPricing/GetLowestPrices/v1", payload, headers)
# 
# res = conn.getresponse()
# data = res.read()
# 
# 
# print(data.decode("utf-8"))
