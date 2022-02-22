from selenium import webdriver

url = 'https://menu.mtholyoke.edu/shortmenu.aspx?sName=Mount+Holyoke+College+Dining+Services&locationNum=40&locationName=Classics&naFlag=1&mealName=Breakfast'
browser = webdriver.Chrome()
browser.get(url)

browser.find_element_by_xpath('//*[@id="Breakfast-inner"]/ul/li[3]/a[1]').click()