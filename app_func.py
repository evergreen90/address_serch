import requests


def search_address(zipcode):
    print(__name__)
    response = requests.get(
        f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}")

    dic = response.json()

    prefecture_name = dic["results"][0]["address1"]
    city_name = dic["results"][0]["address2"]
    town_name = dic["results"][0]["address3"]

    address = f"{prefecture_name}{city_name}{town_name}"
    return address