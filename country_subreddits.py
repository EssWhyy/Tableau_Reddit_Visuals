import csv,time
from bs4 import BeautifulSoup
from datetime import datetime
import urllib.request

url = 'https://www.reddit.com/r/'

def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []

    with open(csvfilename, 'r') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows

print(datetime.now())
countries = read_csv('countries.csv')

for row in countries:
    country = row[0]
    country = country.replace(" ", "") #remove spaces
    subreddit_url = url + country
    
    try:
        #Using urllib to get the html structure, then beautifulsoup to find the tag with the member count.
        req = urllib.request.Request(subreddit_url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        members = soup.find('div',{'class':"_3XFx6CfPlg-4Usgxm0gK8R"}).get_text()
        if members[-1] == 'k': #convert k to 1000
            members = int(float(members[:len(members)-1]) * 1000)
        else:
            members = int(members)
        
        print(members) #number of subreddit members for a particular country

    except urllib.error.HTTPError: #if subreddit doesn't exist
        print("No subreddit for " + country)

    time.sleep(1)