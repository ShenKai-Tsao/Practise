# # 網路連接
# import urllib.request as resquest

# src = "https://www.ntu.edu.tw/"
# with resquest.urlopen(src) as response:
#     data = response.read().decode("utf-8") # 取得台灣大學網站原始碼(HTML CSS JS)

# print(data)

# 練習
import urllib.request as resquest
import json
src = "https://datacenter.taichung.gov.tw/swagger/OpenData/f3b5245a-c13e-4a68-a43e-dd2ffaa5f0b8"
with resquest.urlopen(src) as response:
    data = json.load(response)
    
with open("data.txt", "w", encoding="utf-8") as file:
  for company in data:
    sCompany = company["工廠名稱"]
    if len(sCompany) != 0:     
        print(sCompany)
    file.write(company["工廠名稱"] + "\n")

