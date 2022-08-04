import requests
import pandas as pd
import geohash2

def oneroom(addr) :
    # 위도 경도 알아오기
    url = f"https://apis.zigbang.com/v2/search?leaseYn=N&q={addr}&serviceType=원룸"
    response = requests.get(url)
    data = response.json()["items"][0]
    lat, lng = data["lat"], data["lng"]
    
    # 위도, 경도 값을 geohash로 변환
    geohash = geohash2.encode(lat, lng, precision=5)
    
    # geohash를 통해 매물id를 가져온다
    url = f"https://apis.zigbang.com/v2/items?deposit_gteq=0&domain=zigbang\
&geohash={geohash}&needHasNoFiltered=true&rent_gteq=0&sales_type_in=전세|월세&service_type_eq=원룸"
    # \로 문자열을 이어줄 때 ' ' 공백이 있으면 에러 발생하니 주의
    response = requests.get(url)
    items = response.json()["items"]
    ids = [item["item_id"]for item in items]
    
    # 매물id를 통해서 매물에 대한 정보를 가져온다
    url = "https://apis.zigbang.com/v2/items/list"
    params = {
        "domain" : "zigbang",
        "withCoalition" : "true",
        "item_ids" : ids
        #"item_ids" : ids[:900]
    }
    response = requests.post(url, params)
    items = response.json()["items"]
    # 필요한 정보들만 따로 선별해서 가져올 수 있게 한다
    columns = ["item_id", "sales_type", "deposit", "rent", "size_m2", "address1", "manage_cost"]
    df = pd.DataFrame(items)[columns]
    return df
