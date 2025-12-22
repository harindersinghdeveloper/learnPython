import requests
import bs4
response = requests.get("https://www.example.com/")
if response.status_code==200:
    soup = bs4.BeautifulSoup(response.text, "lxml")
    print(soup.prettify())
    title = soup.select('title')
    print(title[0].get_text().__eq__("Example Domain"))
else:
    print(f'Response status is: {response.status_code}, unable to successfully load the website')


