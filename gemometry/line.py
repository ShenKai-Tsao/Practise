# 計算兩點斜率
# 傳入兩個座標參數
def slope(vX1, vY1, vX2, vY2):
    iValue = abs((vX1 - vX2))
    iValue2 = abs((vY1 - vY2))
    iResult = iValue / iValue2
    return iResult
