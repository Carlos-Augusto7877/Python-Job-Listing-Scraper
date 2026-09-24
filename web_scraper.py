import requests
import csv
from bs4 import BeautifulSoup, Tag

foo = Tag(name='foo')
    
url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

job_cards = soup.find_all('div', class_="column is-half")

csvfile = open("Job_listings.csv", "w", newline='')
fieldnames = ['title', 'company', 'location', 'detail page']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

for c in job_cards:
    title = c.find("h2", class_="title is-5") or foo
    company = c.find("h3", class_="subtitle is-6 company") or foo
    location = c.find("p", class_="location") or foo
    detail_page_url = c.find('a', class_='card-footer-item', string='Apply') or foo
    
    writer.writerow({
        'title': title.text, 
        'company': company.text, 
        'location': location.text, 
        'detail page': detail_page_url.get('href') or ''
    })


csvfile.close()