import requests
import bs4
import pdb
#list 2-star books on all pages
baseurl = "https://books.toscrape.com/catalogue/page-{}.html"
for x in range(1,50):
    page = requests.get(baseurl.format(x))
    soup = bs4.BeautifulSoup(page.content, "lxml")
    books = soup.select(".product_pod")
    twoStarBooks = []
    for book in books:
        if book.find("p", class_='star-rating').get("class").__contains__("Two"):
            #print(book)
            h3 = book.find("h3")
            title = h3.find("a").get("title")
            twoStarBooks.append(title)
    print(f'Two star books on page {x} are: {twoStarBooks}')