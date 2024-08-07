# r	只讀取檔案(唯讀)。檔案必須存在。
# r+	讀取寫入檔案(讀寫)。不會新建檔案，檔案必須存在，寫入會覆蓋原本內容。
# w	新建寫入檔案(只寫)。文件內容清零。
# w+	新建讀取寫入檔案(讀寫)。文件內容清零。
# a	寫入檔案(只寫)。新增在檔案後面，不會覆蓋原本的。
# a+	允許新增與讀取(讀寫)。新增在檔案後面，不會覆蓋原本的。

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

