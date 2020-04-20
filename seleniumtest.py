from selenium import webdriver




file = open('urls.txt', 'r')
urls = file.readlines()
browser = webdriver.Chrome("D:\\chromedriver.exe")
for url in urls:
    
    browser.get(url.strip())
    
browser.close()       