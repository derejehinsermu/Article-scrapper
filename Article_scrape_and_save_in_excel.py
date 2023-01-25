from bs4 import BeautifulSoup, element
from newspaper import Article
from datetime import datetime
from requests import get

from sys import argv
import xlsxwriter
import nltk
import json

nltk.download('punkt')
def keywords(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    keywords = article.keywords
    return keywords

def scrapper(url):
    """Main Scrapper Function
    
    Keyword arguments:
    url -- the url for the news article
    Return: a dictionary file containing the title, content, updated date, modified date and author of the article
    """
    # url to html and then to parsed content
    html_content = get(url).text
    parsed_content = BeautifulSoup(html_content, "html.parser")
    
    # published date
    # raw_pub_date = parsed_content.find("meta", property="article:published_time")["content"]
    # published_date = datetime.strptime(raw_pub_date, "%Y-%m-%dT%H:%M:%S.%fZ")
    
    
    # modified date
    # raw_mod_date = parsed_content.find("meta", property="article:modified_time")["content"]
    # modified_date = datetime.strptime(raw_mod_date, "%Y-%m-%dT%H:%M:%S.%fZ")
    
    
    # article author
    # raw_author = parsed_content.find("meta", attrs={"name": "byl"})["content"]
    # author = raw_author[3:] # remove "By" boilerplate at the start of this attribute
    
    
    # article title
    title = parsed_content.find("h1", attrs={"id": "main-heading"}).get_text()
    
    
    # remove figure and emphasized contents
    for i in parsed_content.find_all("figure"):
        parsed_content.figure.decompose()
    for i in parsed_content.find_all("em"):
        i.decompose()
    
    # take the article body part only as html file
    parsed_content = parsed_content.find("article")

    
    # parse the article body content with appropriate breaks
    content = ''
    for tag in parsed_content.descendants:
        if isinstance(tag, element.Tag) and tag.name == "p":
            content += "\n\n"

        if isinstance(tag, element.NavigableString):
            content += tag
    
    keys = keywords(url)
    # putting all together as a dictionary and string
    article = {
        "LINK": url,
        "TITLE": title,
        "DESCRIPTION": content.strip(),
        "KEYWORDS": keys,
        
    }
    article_str = "LINK: {}\n\n".format(url)
    article_str += "TITLE: {}\n\n".format(title)
    article_str += "CONTENT: {}\n\n".format(content.strip())
    article_str += "KEYWORDS: {}\n".format(keys)



    return article, article_str
    


def save_excel(article):
    # import xlsxwriter module

    col_names = ['Link', 'Title', 'Description', 'Keywords']

    workbook = xlsxwriter.Workbook('scapped_content.xlsx')
    worksheet = workbook.add_worksheet()


    row = 0
    column = 0

    # iterating through content list
    for key in article.keys() :
        if row == 0 and column == 0:
            for title in col_names:
                worksheet.write(row, column, title)
                column += 1
            row = 1
            column = 0

        worksheet.write(row, column, str(article[key]))
        column += 1

    workbook.close()

    return


def main():
    url_arg = argv[1]
    article, article_str = scrapper(url_arg)

    save_excel(article)



if __name__ == "__main__":
    main()


