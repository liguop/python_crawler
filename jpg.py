from bs4 import BeautifulSoup
import urllib  
import requests
import random

"""
# 下面是换IP，不让他封你IP
def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list

def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies

if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nn/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    ip_list = get_ip_list(url, headers=headers)
    proxies = get_random_ip(ip_list)
    print(proxies) 
"""
file = open('C:/Users/tj/Desktop/test.html','r',encoding='utf-8')
soup = BeautifulSoup(file,'lxml')

li=[]
b=soup.find('div', class_="entry-content").find_all('img')
for x in range(len(b)):
	print(x+1,":      ",b[x].attrs["src"])   
	li.append(b[x].attrs["src"])
print("共有", len(li),"张图片")
for x in range(44,len(li)):
	print("已经抓到第"+str(x+1)+"张")
	urllib.request.urlretrieve(li[x],'C:/Users/tj/Desktop/jpg/'+str(x)+'.jpg')  
	print("第",x+1,"张抓取完毕")
print("全部抓取完毕")
"""
import requests 
response = requests.get("************************.html")

print(response)
#获取r的文本 就是一个json字符串
json_response = response.content.decode()
print(json_response)
"""