# 定義函式
# 函式內部的程式碼， 若是沒有函示呼叫，就部會執行

def multiply(xValue,xValue2):
    return xValue * xValue2


# 呼叫函式
iValue = int(input("請輸入數值一"))
iValue2 = int(input("請輸入數值一"))
print(multiply(iValue, iValue2))
print(type(multiply(iValue,iValue2)))