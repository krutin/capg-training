from bs4 import BeautifulSoup
import requests
def imdb(url):
    headers={
    "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"    
    }
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.text,'html.parser')
    movies=soup.find_all('h3',class_="ipc-title__text")
    movies=movies[0:5]
    movies_titles=[movie.get_text(strip=True) for movie in movies]
    for title in movies_titles:
        print(title)
url="https://www.imdb.com/search/title/?title_type=feature&release_date=2011-01-01,2011-12-31"
imdb(url)

