import requests
from bs4 import BeautifulSoup


def PrintBlogTitles():

    reqObj = requests.get("https://three20kbps.wordpress.com/")
    content = BeautifulSoup(reqObj.content, "html.parser")
    articles = content.find_all("article")

    for article in articles:
        title = article.find_all("h1", {"class": "entry-title"})[0]
        print title.text
        print "\n"


if __name__ == '__main__':
    PrintBlogTitles()
