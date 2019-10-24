from bs4 import BeautifulSoup
import urllib  
import requests
import random

print("开始爬取网页")
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}
web_data = requests.get("***************/3", headers=headers)
soup = BeautifulSoup(web_data.text, 'lxml')
print("已经爬取完网页")

li=[]
b=soup.find('div', class_="entry-content-width").find_all('img')
for x in range(len(b)):
	print(x+1,":      ",b[x].attrs["src"])   
	li.append(b[x].attrs["src"])
	
print("共有", len(li),"张图片")
path="C:/Users/tj/Desktop/01/"
print("保存路径是：  "+path)
for x in range(0,len(li)):
	print("已经抓到第"+str(x+1)+"张")
	
	try:
		urllib.request.urlretrieve(li[x],path+str(x+21)+'.jpg')  
	except:
		continue
	print("第",x+1,"张抓取完毕")
print("全部抓取完毕")
 