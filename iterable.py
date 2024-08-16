# iterable 資料型態

# 字串、列表、集合、字典

# for 迴圈
# for 迴圈 IN 可疊代的資料

# 列表
print("列表")
for x in ["a","b","c"]:
    print(x)

# 字串
print("字串")
for x in "abc":
    print(x)

# 集合
print("集合")
for x in {"a","c","s"}:
    print(x)

# 字典
print("字典")
dic = {"a":3,"c":4}
for x in dic:
    print(x,str(dic[x]))

# 內建函式
# 取最大值
print("內建函式")
result = max([10,20,30,40])
print(result)

# 排序
result = sorted([10,20,30,40], reverse = True)
print(result)