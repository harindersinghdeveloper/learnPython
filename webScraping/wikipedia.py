import requests
import bs4
url = "https://en.wikipedia.org/wiki/Grace_Hopper"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Connection": "keep-alive",
})

response = session.get(url, timeout=15)
if response.ok:
    #grab content
    soup = bs4.BeautifulSoup(response.text, "lxml")
    # for s in soup.select(".vector-toc-text span"):
    #     print(s.text)

    #download image
    image = soup.select("td.infobox-image img")[0].get("src")
    print(image)
    image_link = session.get("https:"+image)
    print(image_link.content)
    f = open("Grace_Hopper.jpg", "wb")
    f.write(image_link.content)
    f.close()
else:
    print("Something went wrong, response status code is: " + str(response.status_code))