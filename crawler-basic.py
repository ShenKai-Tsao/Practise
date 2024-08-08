
# 抓取 dcard 網頁原始碼 (HTML)
import urllib.request as req

url = "https://www.ptt.cc/bbs/Hiking/index.html"

# 建立一個 request 物件，附加 Request Headers 的資訊
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}) 

with req.urlopen(request) as response:
    data = response.read().decode("utf-8") # 取得台灣大學網站原始碼(HTML CSS JS)

# 解析原始碼，取得每篇文章標題
# 安裝第三方套件： 語法， pip install beautifulsoup4
import bs4

root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("div", class_="title") # 尋找 class = "title" 的 div 標籤

with open("data.txt", "w", encoding="utf-8") as file:
    for i in titles:
        a_tag = i.find('a')
        if a_tag:
            file.write(a_tag.string + "\n")


    # if titles.a != None:
    #     print(titles.a.string)


