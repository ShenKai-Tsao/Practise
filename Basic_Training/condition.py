# 判斷式
#x = input("請輸入數字") # 取得字串形式的使用者輸入
#x = int(x) # 將字串轉換成數字型態
#if x > 50:
#    print("大於 50")
#elif x >30:
#    print("大於 30, 小於等於 50")
#else:
#    print("小於 50")

# 四則運算
n1 = input("請使用者輸入數字一: ")
if not n1.isdigit :
  print("數字一不是數字 請重新輸入")

n2 = input("請使用者輸入數字二: ")
if not n2.isdigit :
  print("數字二不是數字 請重新輸入")

op = input("請輸入運算: +, -, *,/ : ")

if op == "+":
    s = n1 + n2
elif op == "-":
    s = n1 - n2
elif op == "*":
    s = n1 * n2
elif op == "/":
    s = n1 / n2
else :
    s = "請重新輸入運算值"

print(s)
