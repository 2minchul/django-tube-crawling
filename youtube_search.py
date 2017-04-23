import requests
from bs4 import BeautifulSoup

from djangoTube_insert_video import Post_new_video

search_keyword = "빅뱅"
# search_keyword = input("Search keyword: ")


djangoTube = Post_new_video()
br = requests.Session()

url = "https://www.youtube.com/results?search_query=%s" % (search_keyword)

res = br.get(url)


soup = BeautifulSoup(res.text, 'html.parser')

for tag in soup.find_all('h3', {'class': 'yt-lockup-title'}):
    
    for a_tag in tag.find_all('a'):
        href, title = a_tag.get('href'), a_tag.get('title')

        djangoTube.post(title, href.replace("/watch?v=", ""))

        
