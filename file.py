# 儲存檔案
# w 檔案的寫入

# file = open("data.txt", mode="w", encoding="utf-8") # 開啟
# file.write("Hello world\n") # 操作
# file.write("測試中文\n好棒棒") # 中文操作
# file.close()

with open("data.txt", mode = "w", encoding="utf-8") as file:
    file.write("1\n")
    file.write("3\n")
    file.write("2\n")

# # r 檔案的讀取
# with open("data.txt", mode = "r", encoding="utf-8") as file:
#     date =  file.read()
# print(date)

# r 檔案的讀取
sum = 0
with open("data.txt", mode = "r", encoding="utf-8") as file:
    for line in file:
      sum += int(line)

    # date =  file.read() 整個文件寫出
print(sum)




# 使用 JSON 格式讀取、複寫檔案