import requests
from bs4 import BeautifulSoup

names = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
band6 = 0

def atarsort(letter1, school):
    global band6
    url = "https://educationstandards.nsw.edu.au/wps/portal/nesa/about/events/merit-lists/distinguished-achievers/%s" % (letter1)

    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'lxml')
    soup

    table1 = soup.find('tbody')
    table1

    for i in table1.find_all('tr'):
    
        title = i.text
        
        if school in title:
            band6 += 1
            band6 += str(i).count('<br/>')
            names.append(title)         
            
for x in range(len(alphabet)):
    atarsort(alphabet[x], "School name") #<--- School Name

for x in range(len(names)):
    print(names[x])

print("Total Students: " + str(len(names)))
print("Total Band 6's: " + str(band6))