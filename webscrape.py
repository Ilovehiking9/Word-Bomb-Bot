from bs4 import BeautifulSoup
import requests
import random
import re
from multiprocessing import Process

def findWord(s):

    if "=" in s:
        return ('no')

    word = re.sub(r'[\W_]+', '', s)
    word = word.replace("5", "s")
    word = word.replace(")", "s")
    word = word.replace("|", "i")

    print(word)
    #chance in casehe
    coinflip = random.randint(1,2)
    if coinflip == 1:
        word.replace("b", "d")

    amount = random.randint(11,13)

    url = f"https://wordfind.com/{amount}-letter-words-with-{word}/#results"
    wordlist = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    bigtable = soup.find("div", {"class": "lBlock"})
    try:
        ul = bigtable.ul
    except AttributeError:
        return "none"

    #list of all elements
    elements = ul.findAll("li")


    for i in list(range(0,100)):
        randomIndex = random.randint(0, len(elements)-1)
        atag = str(elements[randomIndex].contents[0].contents[0])
        #word name

        if word in atag:
            wordlist.append(atag)

    randomNumber = random.randint(0, len(wordlist))

    try:
        return wordlist[randomNumber]
    except IndexError:
        print("none")





if __name__ == "__main__":


    print(findWord("az"))
