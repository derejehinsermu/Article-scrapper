# Article-scrapper

The program can be used to scrape the content from an article from web by an input of a set of URLs in a text file.
This project uses newspaper3k and python-docx libraries. The output of this program will give a neatly modified excell Document in '.xlsx' format.
This makes our life a lot easier by saving a lot of time to obtain data from an article.

This prorgam gives the following from an article in the excell Document,

    The Title
    Content
    Link    
    Keywords from the Article
    
##INSTRUCTIONS
### Install prerequest libraries
        .pip install -r requirement.txt
### How to Use
      python Article_scrape_and_save_in_excel.py "url"
      
      
##NOTE

    If you are running the program for the first time, run pip install -r requirement.txt  file before executing the program, it will install all the necessary modules.
