import threading
from selenium import webdriver

chrome_path = r"C:\Users\woute\Desktop\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def getAmount():
    driver.get("https://teamtrees.org/")
    print(driver.find_element_by_id("totalTrees").text)

setInterval(getAmount,10)