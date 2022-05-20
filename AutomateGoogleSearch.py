from selenium import webdriver

search_topic = input("Enter a name or site that you want to search...!")
search_topic = search_topic.replace(' ', '+')


browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

for i in range(1):
    element = browser.get("https://www.google.com/search?q="+search_topic+"&start"+str(i))
