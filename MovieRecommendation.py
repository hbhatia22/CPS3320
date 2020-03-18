import requests
from bs4 import BeautifulSoup as BS
import re

genre = ['drama', 'musical', 'family', 'thriller', 'sports', 'horror', 'comedy']


# selects the movie based on users mood
def search(selection):
    if selection == genre[0]:
        url = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'

    elif selection == genre[1]:
        url = "https://www.imdb.com/search/title/?genres=musical&title_type=feature&sort=moviemeter, asc"

    elif selection == genre[2]:
        url = "https://www.imdb.com/search/title/?genres=family&title_type=feature&sort=moviemeter, asc"

    elif selection == genre[3]:
        url = "https://www.imdb.com/search/title/?genres=thriller&title_type=feature&sort=moviemeter, asc"

    elif selection == genre[4]:
        url = "https://www.imdb.com/search/title/?genres=sport&title_type=feature&sort=moviemeter, asc"

    elif selection == genre[5]:
        url = "https://www.imdb.com/search/title/?genres=horror&title_type=feature&sort=moviemeter, asc"

    elif selection == genre[6]:
        url = "https://www.imdb.com/search/title/?genres=comedy&title_type=feature&sort=moviemeter, asc"

    response = requests.get(url)
    data = response.text

    soup = BS(data, "lxml")
    title = soup.find_all("a", attrs={"href": re.compile(r'\/title\/tt+\d*\/')})
    return title


if __name__ == '__main__':

    user = input("Press any key to continue: ")
    user = user.lower()
    while user != 'exit':
        print("Select genre from a list of genres: ", genre)
        choice = input("What's the genre for today's movie: ")
        choice = choice.lower()
        if choice in genre:

            a = search(choice)
            count = 0

            for i in a:
                tmp = str(i).split('>')
                if len(tmp) == 3:
                    print(tmp[1][:-3])
                if count > 15:
                    break
                count += 1

        else:
            print("Genre choice not supported yet!!!")

        user = input("Exit to quit else press any key to continue: ")
        user = user.lower()
