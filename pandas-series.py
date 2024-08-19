import pandas as pd

# 數學統計相關
# 資料索引
# 內建的索引
data = pd.Series([1,2,3,4,5])

# 可自行定義索引
data = pd.Series([1,2,3,4,5], index=["a","b","c","d","e"])

print("建立一維運算(自定義索引)", data)


# 觀察資料
print("資料型態", data.dtype)
print("資料數量", data.size)
print("資料索引", data.index)

# 取得資料:
print("根據順序", data.iloc[2])
print("根據索引", data["e"])

# 數字運算：基本，統計，順序
print("總和", data.sum())
print("最大值", data.max())
print("相乘", data.prod())
print("平均", data.mean())
print("中位數", data.median())
print("標準差", data.std())
print("前N大 取前3", data.nlargest(3))
print("前N小 取前2", data.nsmallest(2))

data = pd.Series(["你好","Python", "Pandas"])

print("調整微小寫", data.str.lower())
print("調整微大寫", data.str.upper())
print("資料長度", data.str.len())
print("字串串連", data.str.cat(sep=","))
print("判斷字串中有沒有該值", data.str.contains("Python"))
print("取代", data.str.replace("你好","Hello"))

