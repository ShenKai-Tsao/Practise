from datetime import date,timedelta
# 取得今天的各種資訊
#dTody = date.today()
dTody = date(1995,4,6)
print(dTody.year,dTody.month,dTody.day)
print(dTody)
print(dTody.weekday() + 1)  # 0 代表星期一 1 代表星期二 .. 一此類推

# 印出往後算一周
dt = date.today()
differ=timedelta(weeks=1)
afterWeekDay = dt + differ
print(afterWeekDay)

# 印出本月份的所有日期和星期幾
today = date.today()
dt= date(today.year,today.month,1)

weekday_name = {
0: "周一",1: "週二",2: "周三",3: "週四",4: "周五",5: "週六",6: "周日",
}

while dt.month == today.month:
    weekday = dt.weekday()
    print("日期",dt, weekday_name[weekday])
    dt = dt + timedelta(days = 1)

