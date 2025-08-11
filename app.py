import requests

zipcode = input("郵便番号を入力してください:")
response = requests.get(f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}")

print(response)
print(response.text)


