# 類別與實體物件、實體屬性

#　實體屬性：　封裝在實體物件中的變數
print("實體屬性")
print("-------------------------------------------------------------")
# Point 實體物件的設計：平面座標上的點
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

# 建立力第一個實體物件
p1 = Point(3,4)
print(p1.x,p1.y)

# 建立力第二個實體物件
p2 = Point(5,6)
print(p2.x,p2.y)
print("-------------------------------------------------------------")

# # FullName 實體物件的設計： 分開紀錄姓、名資料的全名

# class FullName:
#     def __init__(self, vFirstName: str, vLastName: str) -> None:
#         self.vFirstName = vFirstName
#         self.vLastName = vLastName

    
#         print(vLastName + vFirstName)

# with open("data.txt", "w", encoding="utf-8") as file:
#     for i in range(2):
#         sLastName = input("請輸入你的姓:")
#         sFirsttName = input("請輸入你的名:")
#         sData1 = FullName(sFirsttName, sLastName)
#         file.write("姓: " + sData1.vLastName + " 名: " + sData1.vFirstName +"\n")




#　實體方法：　封裝在實體物件中的變數
print("實體方法")
print("-------------------------------------------------------------")
# Point 實體物件的設計：平面座標上的點
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    def show(self) -> None:
        print(self.x, self.y)
    def distance(self, vTargetX, TargetY) -> float:
        return(((self.x-vTargetX)**2 + (self.y-TargetY)**2))**0.5

# 建立第一個實體物件並呼叫實體方法
p1 = Point(3,4)
p1.distance(0,0) # 計算座標 (3,4) 與 (0,0) 距離

# 建立第二個實體物件並呼叫實體方法
p2 = Point(5,6)
p2.distance(0,0)
print("-------------------------------------------------------------")

# 練習使用封裝呼叫實體方法
import FileTraining.FileControl as FileControl
f1 = FileControl.File("data.txt")
f1.open()
f1.write("text1")
data = f1.read()
print(data)
