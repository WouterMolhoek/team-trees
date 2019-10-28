import threading
import json
from selenium import webdriver

chrome_path = r"C:\Users\woute\Desktop\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

data = {}
data['trees'] = []

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def getAmount():
    # Refresh the page
    driver.get("https://teamtrees.org/")
    
    data['trees'].append(driver.find_element_by_id("totalTrees").text)

    # Write data to an JSON file
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

setInterval(getAmount,10)