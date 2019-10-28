from selenium import webdriver

chrome_path = r"C:\Users\woute\Desktop\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

url = "https://teamtrees.org/"
driver.get(url)

print(driver.find_element_by_id("totalTrees").text)

