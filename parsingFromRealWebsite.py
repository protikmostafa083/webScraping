import requests
from bs4 import BeautifulSoup

# import request
html_text = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
job= soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
company_name = job.find('h3', class_='joblist-comp-name')
print(job)
