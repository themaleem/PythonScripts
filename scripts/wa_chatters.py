_author_  = "olumide bello"
_date_created_='November 21, 2019'
"""
Script dependencies include:

Python re module

"""

print(
        """
        This program returns a list of all names or number of people (or person)
        that has sent one message in a whatsapp chat.

        All you need is to export the chat from a whatsapp groups or 
        a normal 2-party chat 
        """
)

import re

#Regular Expression pattern to match the beginning of a line of message 
#please read up RegExp if you can't understand the pattern below
text=re.compile(r'\d\d/\d\d/\d\d\d\d, \d\d:\d\d - (.*:)') 


def get_chatters(filepath):
#     open file in rb(read binary) mode to take care of emoji and byte chat instances
        #Milestone 2
    with open(filepath,'rb') as file:
        #   initialize a variable (file_content) for byte-like string with b''
        #   and add each line in the file to vaiable 
        file_content=''    
        for i in file:
        #   decode() methods changes the byte-stream into a str object
            file_content+=i.decode('utf-8')
    
    chatters=[]
    #find all matches of 'text' pattern in 'file_content' 
    patterns=re.findall(text,file_content)

    #Milestone 3.1
    print(f'This chat contains {len(patterns)} sent messages')
    
    for i in patterns:
    #   the regexp finds all matches even after the first semi-colon ':' but we really only need the first :
    #   so we split whatever it returns at every semicolon ':' 
    #   and grab the first item of the splitted list
    #   thats what we really need, the sender of message in the chat
        i=i.split(':')[0]
        
        #   append sender's name if not already in chatter's list
        if i not in chatters: 
            chatters.append(i)
    
    return chatters

if __name__ == "__main__":
    file_path=input(r'Please enter exported whatsapp-chat text file: ')
    print(get_chatters(file_path))
