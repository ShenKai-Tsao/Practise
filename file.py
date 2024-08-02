# 儲存檔案
# w 檔案的寫入

file = open("data.txt", mode="w", encoding="utf-8") # 開啟
file.write("Hello world\n") # 操作
file.write("測試中文\n好棒棒") # 中文操作
file.close()

with open("data2.txt", mode = "w", encoding="utf-8") as file:
    file.write("測試新寫法\nRRRRRRR")

# 讀取檔案
with open("data.txt", mode = "r", encoding="utf-8") as file:
    date =  file.read()
print(date)




# 使用 JSON 格式讀取、複寫檔案