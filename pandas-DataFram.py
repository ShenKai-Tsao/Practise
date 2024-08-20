# 載入 pandas 模組
import pandas as pd 
# 資料索引
# 內建索引
data = pd.DataFrame({
    "name":["Amy","Billy","Frank"],
   "salary":[300000,400000,500000]

})

# 自訂索引
data = pd.DataFrame({
    "name":["Amy","Billy","Frank"],
   "salary":[300000,400000,500000]
}, index = ["a","b","c"])

print(data)

# 觀察資料
print("資料型態(列,欄)", data.shape)
print("資料數量", data.size)
print("資料索引", data.index)

#取得列(Row/橫向) 的 Series 資料，根據順序
print("取第二列資料", data.iloc[1], sep="\n")
print("======================")
#取得列(Row/橫向) 的 Series 資料，根據索引
print("取第C列資料", data.loc["c"], sep="\n")
#取得欄(Column/直向) 的 Series 資料，根據順序 欄的操作可以使用 Series 操作
print("取第一欄資料", data["name"], sep="\n")
names = data["name"]
print("把 name 都列印出大寫", names.str.upper(), sep = "\n")
salary = data["salary"]
print("算出 salary 的平均:", salary.mean())

# 建立新的欄位
# 一般寫法
data["revenue"] = [5000000,4000000,3000000]
# 運用 Series 寫法
data["rank"] = pd.Series([3,6,1], index=["a","b","c"])
data["cp"] = data["revenue"]/data["salary"]

print(data)


