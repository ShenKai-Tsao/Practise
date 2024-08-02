# 計算兩點距離
# 傳入兩個座標參數
def distance(vX1, vY1, vX2, vY2):
    iValue = abs((vX1 - vX2)) ** 2 
    iValue2 = abs((vY1 - vY2)) ** 2 
    iResult22 = (iValue + iValue2) ** 0.5
    return iResult22