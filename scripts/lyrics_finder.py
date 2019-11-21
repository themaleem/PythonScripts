_author_  = "olumide bello"

"""
Script dependencies include:

request module
BeautifulSoup module

"""

print("""
    This program scrapes lyrics from the genius lyrics website "https://genius.com"
    a popular lyrics site and return requested lyrics 
    All you need is the artiste's name and the song's name
""")

import requests
from bs4 import BeautifulSoup


def get_lyrics(artiste,song):

    half_url = "https://genius.com/" #sGenius Lyrics website
    #this part is needed according to how genius lyrics urls are wired
    end = "-lyrics" 

    #https://genius.com/Rick-ross-diced-pineapples-lyrics
    full_url = half_url + artiste + "-" +song + end
    
    print(f"attempting to grab your lyrics from {full_url}") 

    try:
        #request to get data from the url above
        r = requests.get(full_url)

        #the actual HTML content of the url will be stoted in the variable "data" below 
        data = r.content

        #beautiful soup object
        soup = BeautifulSoup(data, "html.parser")

        #finds lyrics text with the html tags which contain the actual lyrics
        element = soup.find("div", {"class": "lyrics"})

        print("\n")   #newline

        print(element.text.strip()) #prints the final result without preceeding or ending newline characters 

        print("\n")
    
    except Exception as e:
        print(e)
        print('Oops! error occured while trying to grab your lyrics. Please try again! \nOr try requesting another lyrics')

    finally:
        print ('Thanks for using the program')


songs_name = input("input the name of the song : ") #eg Diced piNeapplEs

# here the above becomes "diced-pineapples"
song=songs_name.lower().replace(' ','-')
artiste_name = input("input the name of the artiste : ")#Rick Ross

# becomes rick-ross
artiste=artiste_name.lower().replace(' ','-') 

get_lyrics(artiste,song)

