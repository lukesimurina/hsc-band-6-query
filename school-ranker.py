import requests
from bs4 import BeautifulSoup

#Scrape school names from HSC Ninja as my code is bad
schools = []
rankings = []
url1 = "https://www.hscninja.com/honour/roll/year/2021"

soup = BeautifulSoup(url1, 'lxml')

table12 = soup.find("table", attrs={"class", "table table-striped"})

for i in table12.find_all("a", attrs={"class", "ng-binding"}):
    title = i.text
    schools.append(title)
######

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'no-surname']


def band6countForLetter(letter1, school):
    band6 = 0
    url = "nesa-band6/%s.html" % (letter1)

    with open(url) as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    table1 = soup.find('tbody')

    for i in table1.find_all('tr'):
    
        title = i.text
        
        if school in title:
            band6 += 1
            band6 += str(i).count('<br/>')
    return band6

def findBand6count(school):   
    count = 0    
    for x in range(len(alphabet)):
        count += band6countForLetter(alphabet[x], school)
    return count
with open('output.txt', 'a') as f:
    f.writelines("[")
    f.close()
    for a in schools:
        with open('output.txt', 'a') as f:
            total = findBand6count(a)
            f.writelines("['"+(str(a) + "', " + str(total) + "]"))
            f.writelines("\n")
            f.close()
    with open('output.txt', 'a') as f:
        f.writelines("]")
        f.close()
print("Done")