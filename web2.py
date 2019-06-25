import time
from bs4 import BeautifulSoup
from selenium import webdriver

#options = webdriver.webdriver.ChromeOptions()
options = webdriver.ChromeOptions()
options.add_argument('headless')

##copy chromedriver into python folder
##driver = webdriver.Chrome(executable_path=r"C:\Python Prog\chromedriver_win32\chromedriver.exe",chrome_options=options)
driver = webdriver.Chrome(chrome_options=options)
##driver = webdriver.Chrome(options)
driver.set_window_position(-2000,0)#this function will minimize the window
first_url = 1
last_url = 10    # Last book is 8,630,000

for book_reference_number in range(first_url, last_url):
    driver.get("https://www.goodreads.com/book/show/"+str(book_reference_number))
    time.sleep(2)#optional
    soup = BeautifulSoup(driver.page_source, 'lxml')
    try:
        book_title = soup.select('.gr-h1.gr-h1--serif')[0].text.strip()
    except:
        book_title = ''
    try:
        author_name = soup.select('.authorName')[0].text.strip()
    except:
        author_name = ''

    print('NO.', book_reference_number, 'TITLE: ', book_title, 'AUTHOR: ', author_name) 

webdriver.close()
input("Entr to close")
