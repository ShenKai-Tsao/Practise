# 類別與實體物件、實體屬性、實體方法
# Point 實體物件的設計：平面座標上的點
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

# 建立力第一個實體物件
p1 = Point(3,4)
print(p1.x,p1.y)

# 建立力第一個實體物件
p2 = Point(5,6)
print(p2.x,p2.y)
print("-------------------------------------------------------------")

# FullName 實體物件的設計： 分開紀錄姓、名資料的全名

class FullName:
    def __init__(self, vFirstName: str, vLastName: str) -> None:
        self.vFirstName = vFirstName
        self.vLastName = vLastName
        print(vLastName + vFirstName)

with open("data.txt", "w", encoding="utf-8") as file:
    for i in range(2):
        sLastName = input("請輸入你的姓:")
        sFirsttName = input("請輸入你的名:")
        sData1 = FullName(sFirsttName, sLastName)
        file.write("姓: " + sData1.vLastName + " 名: " + sData1.vFirstName +"\n")


