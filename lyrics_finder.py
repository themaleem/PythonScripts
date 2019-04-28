_author_  = "olumide bello"

print("""
    This program scrapes lyrics from the genius lyrics website "https://genius.com"
    a popular lyrics site and prints the 
    lyrics that was requested for on the console
    All you need is the artiste's name and the song's name
""")

import requests
from bs4 import BeautifulSoup
# OLUMIDE BELLO
# DATE = 2018/09/05
while True:
    try:

        songs_name = input("input the name of the song : ") #eg Diced piNeapplEs
        song='-'.join(songs_name.lower().split()) # here the above becomes "diced-pineapples"
        
        artiste_name = input("input the name of the artiste : ")#Rick Ross
        artiste='-'.join(artiste_name.lower().split()) # becomes rick-ross

        half_url = "https://genius.com/" #some part of the url
        end = "-lyrics" #this part is needed according to how genius lyrics urls are wired

        full_url = half_url + artiste + "-" +song + end #https://genius.com/Rick-ross-diced-pineapples-lyrics
        print(f"attempting to grab your lyrics from {full_url}")  # full valid url

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
        
    except KeyboardInterrupt:
        print('Exiting program...')
        print ('Thanks for using the program')
        break
    
    except Exception as e:
        print('Oops! error occured while trying to grab your lyrics. Please try again! \nOr try requesting another lyrics')
