from bs4 import BeautifulSoup
from urllib.request import urlopen

response=urlopen('https://trends.google.co.kr/trends/trendingsearches/daily?geo=KR') 
soup = BeautifulSoup(response, 'html.parser')
i=1
f=open("새파일.text", 'w')
for anchor in soup.find_all('span',class_='title title-break'):
    data=str(i)+"위: "+anchor.get_text()+"\n" #조소를 반복적으로 가져옴    
    i = i + 1
    f.write(data)
f.close()
      
