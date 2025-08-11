from app_func import search_address
def main():
    zipcode = input("ハイフン無しの郵便番号 > ")
    # zipcode = "0287111"
    address = search_address(zipcode)
    print(address)
if __name__ == "__main__":
    main()




# import requests
#
#
# zipcode = input("郵便番号を入力してください:")
# response = requests.get(f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}")
# 
# adress_info = response.json()["results"][0]
# 
# pref = adress_info["address1"]
# city = adress_info["address2"]
# area = adress_info["address3"]
#
# print(f"{pref}{city}{area}")