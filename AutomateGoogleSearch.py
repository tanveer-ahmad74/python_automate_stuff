from selenium import webdriver

search_topic = input("Enter a name or site that you want to search...!")

driver = webdriver.Chrome()
element = browser.get("https://www.google.com/search?q=" + search_topic + "&start")

element =driver.find_element(by=By.TAG_NAME, value='h3')
element.click()
driver.close()
