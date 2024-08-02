# 載入內建的 sys 模組並取得資訊
# import sys

# print(sys.platform) # 作業系統
# print(sys.maxsize) # 最大整數  

# import sys as s # 別名 

# print(s.platform) # 作業系統
# print(s.maxsize) # 最大整數  


# 建立 自定義的模組，載入使用
# import geometry

# #兩點距離
# result = geometry.distance(1,1,5,-5)
# print(result)

# #兩點斜率
# result = geometry.slope(1,1,5,-5)
# print(result)

# 調整搜尋模組的路徑

import sys
sys.path.append("modules")
print(sys.path)
print("==========================")
import geometry
#兩點距離
result = geometry.distance(1,1,5,-5)
print(result)

