# 有序可變動的列表 List
grades = [12,15,14,16,17]
#grades[1:4] = [] # 連續刪除列標中 第 1 個編號 4(不包含) 資料
#grades  = grades + [1,5] # 列表串接

#length = len(grades) #取得列表長度 len(列表資料)
#print(length)

#grades[0] = 55 # 把 55 放到列表中第一個位置
#print(grades)

# 巢狀列表
#date = [[3,4,5],[6,7,8]]
#print(date[0][1])
#date[0][0:2] = [5,5,5]
#print(date)

# 有序不可變動的列表 Tuple

date= (3,4,5)
date[0] = 5 #錯誤 Tuple 的資料不可以不變動
print(date)