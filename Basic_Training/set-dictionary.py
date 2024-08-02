# 集合的運算
#s1 = {3,4,5}
#print (3 in s1) # True
#print (10 in s1) # False
#print (6 not in s1) # True

#s1 = {3,4,5}
#s2 = {4,5,6,7}
#s3 = s1 & s2 # 交集 取兩個集合中 相同資料 # {4,5}
#s3 = s1 | s2 # 聯集 取兩個集合中的所有資料，但不重複取得 # {3,4,5,6,7}
#s3 = s1 - s2 # 差集 從 s1 中 減去和 s2 重疊的 # {3}
#s3 = s1 ^ s2 # 反交集 取兩個集合中，不可重複的資料 {3, 6, 7}
#print (s3)

#s = set("Hello") # set(字串) 將字串拆解為集合，扣除重複的
#print(s)
#print("H" in s)
# 字典的運算 key-value 配對 

#dic = {"apple":"蘋果","bug":"蟲"}
#dic["apple"] = "小蘋果"
#print(dic["apple"])

#dic = {"apple":"蘋果","bug":"蟲"}
#print("apple" in dic) # True
#print("test" in dic) # False
#print("test" not in dic) # True
#del dic["apple"] # 刪除字典中的鍵值配對 (key-value pair)
#print(dic)

dic = {x : x * 2 for x in [2, 3]} #從列表產生字典 for in # {2: 4, 3: 6}
print(dic) 

dic = {y : y + "a" for y in set("Hello")}
# {'o': 'oa', 'H': 'Ha', 'l': 'la', 'e': 'ea'}
del dic["H"]
{'e': 'ea', 'l': 'la', 'o': 'oa'}
print(dic)

