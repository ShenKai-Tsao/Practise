# break

# n = 0
# while n < 5:
#     if n == 3:
#         break
#     print(n)
#     n += 1 
# print("變數 n 最後的值: ", n)


# continue
# n = 0
# for i in range(4):
#  if i % 2 == 0:
#   continue
#  print(i)
#  n += 1
# print("變數 i 最後的值: ", n)

# else

# sum = 0
# for i in range(11):
#     sum += i
# else:
#     print(sum)

# 綜合範例
# 找出整數的平方根

# n = input("請輸入一個整數:")

# for i in range(n):
#     if i * i == n:
#         print("找到整數平方根: ", i)
#         break
# else:
#     print(n, ": 沒有找到整數平方根")

import math

# 提示使用者輸入整數
num = int(input("請輸入一個整數: "))

# 計算平方根
sqrt_num = math.sqrt(num)

# 判斷平方根是否為整數
if sqrt_num.is_integer():
    print(f"{num} 的平方根是整數 {int(sqrt_num)}")
else:
    print(f"{num} 的平方根是 {sqrt_num}, 不是整數")


