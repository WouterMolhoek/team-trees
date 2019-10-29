import threading
import json
import eel

from time import gmtime, strftime
from selenium import webdriver

eel.init('web', allowed_extensions=['.js', '.html'])

# SET PATH HERE
chrome_path = r"C:\Users\woute\Desktop\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

# Make an object
data = {}
data['trees'] = []

@eel.expose
def getAmount():
    # Refresh the page
    driver.get("https://teamtrees.org/")
    
    data['trees'].append([strftime("%H:%M:%S", gmtime()),driver.find_element_by_id("totalTrees").text.replace(',','')])

    # Write data to an JSON file
    with open('web/data/data.json', 'w') as outfile:
        json.dump(data, outfile)

eel.start('index.html')
