from types import CoroutineType
import requests
from requests.sessions import preferred_clock
from requests.utils import address_in_network

zipcode = input("郵便番号を入力してください:")
response = requests.get(f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}")

adress_info = response.json()["results"][0]

pref = adress_info["address1"]
city = adress_info["address2"]
area = adress_info["address3"]



print(f"{pref}{city}{area}")