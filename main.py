# import package

from bs4 import BeautifulSoup

# opening the local html file
with open('home.html','r') as html_file:
    content = html_file.read()
    #print(content)
    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())
    #grabbing some specific information
    tags = soup.find('h5')
    print(tags)
    # not closing execution and find all the methods
    tags = soup.find_all('h5')
    print(tags)

    #modifying the tags variable and finding all the courses available on the website
    courses_html_tags = soup.find_all('h5')
    for course in courses_html_tags:
        print(course.text)