class IO:
    strList = ["test","pack"]
    def read(strList):
        if strList not in IO.strList:
            print("沒有這個函數")
        else:
            print("目前得到:" + strList)

print(IO.strList)

IO.read("pack")
IO.read("111")