# 練習

# 計算兩點距離
# 傳入兩個座標參數
def distance(vX1, vY1, vX2, vY2):
    iValue = abs((vX1 - vX2)) ** 2 
    iValue2 = abs((vY1 - vY2)) ** 2 
    iResult = (iValue + iValue2) ** 0.5
    return iResult

# 計算兩點斜率
# 傳入兩個座標參數
def slope(vX1, vY1, vX2, vY2):
    iValue = abs((vX1 - vX2))
    iValue2 = abs((vY1 - vY2))
    iResult = iValue / iValue2
    return iResult
