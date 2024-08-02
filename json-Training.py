import json
# # 使用 JSON 格式讀取、複寫檔案
# with open("test.json", mode="r", encoding="utf-8") as file:
#     data = json.load(file)  
# detail = data["detail"]
# no = detail["no"]
# print (no)

# 定義JSON字串
json_str = '''
{
  "name": "My name",
  "version": "1.0.0.0",
  "detail": [
    { "no": "1" },
    { "no": "2" }
  ]
}
'''

# 解析JSON字串
data = json.loads(json_str)

# 讀取並輸出詳細信息
details = data["detail"]

# 輸出詳細信息
print("Details:", details)
for detail in details:
    print("No:", detail["no"])

