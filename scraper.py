from bs4 import BeautifulSoup
import urllib.request

def parseAmount():
    source = urllib.request.urlopen('https://teamtrees.org/')
    # Get the amount of trees planted
    soup = BeautifulSoup(source, 'html.parser')
    amount = soup.find('div', id='totalTrees').getText()
    
    return amount

def scrape():
    amount = parseAmount()
    print(amount)

scrape()


