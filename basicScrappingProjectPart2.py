#import package
from bs4 import BeautifulSoup

#read local file
with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
#class jehetu python er built in, so class er pore _ use kora hoise. ebhabe kichu jodi match kore, then amader ke _ diye alada korte hobe.
    course_card = soup.find_all('div', class_ = 'card')
    for course in course_card:
        course_name = course.h5.text
        #price shob a tag er moddhe lekha, tai 'a' use kora hoise niche.
        course_price = course.a.text.split()[-1]
        #print(course_name + ' & Price = '+ course_price)
        #uporer commented line tai arekbhabe lekha jay
        print(f'{course_name} costs {course_price}')
        #print((course_price))
