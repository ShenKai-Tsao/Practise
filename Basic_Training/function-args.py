# 參數的預設資料

# 平方根
def power(xValue):
    return xValue * xValue

iValue = 3
print(power(iValue))

# 使用參數名稱
# 減法
def Subtraction(xValue, xVaule2 = 0):
    return xValue - xVaule2

iValue = 3
print(Subtraction(iValue))

# 無限參數名稱

# 平均數
def avg(*xValue):
    iSum = 0
    for i in xValue:
        iSum += i
    print (iSum/len(xValue))

avg(3,4)
