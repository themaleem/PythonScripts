_author_ = "Olumide Bello"
print("""
    This is a simple script that plays the popular 2048 game
    imitating a human player such as yourself by sending actual
    swipes to the game.

    Try it out and see how far ypu can go before you run out of moves to make! Haha
""")
from random import choice 
from selenium import webdriver 
from time import sleep

#list of selenium keys to be chosen from at random and sent to the browser
keys = ["Keys.DOWN", "Keys.UP", "Keys.LEFT", "Keys.RIGHT"]

#amount of time the a swipe will be sent to thee browser object
swipes=int(input('Amount of swaps: '))

#initializing a browser object to be controlled, i used chromedriver
#you could use FireFox or GeckoDriver as you wish
try:
    chrome = webdriver.Chrome()

    #navigation browser object to the 2048 game website
    chrome.get('https://play2048.co')

    #grabbing the body element of the HTML
    body = chrome.find_element_by_tag_name('body')

    for i in range(swipes):
        random_arrow_key=choice(keys)
    
        #imitating an actual arrow key (swipe) and sending it to broswer object
        body.send_keys(random_arrow_key) 

        sleep(1) #wait 1 sec before sending the next command
except Exception as e:
    print(e)
    print('Oops! The error(s) above as shown occured, please try again.')
