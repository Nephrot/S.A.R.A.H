from bs4 import BeautifulSoup
import requests
import re
import pyttsx3
stringStarter = "Meaning of the word python"
stringStarter = stringStarter.split()

def defineWord(stringStarter): 
    i = 0
    while i < stringStarter.__len__():
        print(i)
        if stringStarter[i] != "Define":
            if stringStarter[i] != "the":
                if stringStarter[i] != "word":
                    if stringStarter[i] != "of":
                        if stringStarter[i] != "Definition":
                            if stringStarter[i] != "Meaning":
                                    print(stringStarter[i])
                                    url = stringStarter[i]
                                    html = requests.get("https://www.vocabulary.com/dictionary/" + url).content
                                    unicode_str = html.decode("utf-8")
                                    encoded_str = unicode_str.encode("ascii", "ignore")
                                    new_soup = BeautifulSoup(encoded_str, "html.parser")
                                    a_text = new_soup.find_all('p')
                                    string = str(a_text)
                                    string = string.replace('<p sclass="one-click-content css-1o84u9 e15kc6du8">', "")
                                    string = string.replace('<span class="italic">', '')
                                    string = string.replace('</span>', '')
                                    string = string.replace('</p>', '')
                                    string = string.replace('<p>', '')
                                    string = string.replace('[', '')

                                    string = string.replace('<i>', '')
                                    string = string.replace('</i>', '')

                                    num2 = string.find('"long')
                                    string = string[0:num2]

                                    string = string.replace('<p class="short">', '')
                                    string = string.replace('<p class=', '')
                                    i = 100000000
                            else:
                                i+=1
                        else:
                            i+=1
                    else:
                        i+=1
                else:
                    i+=1
            else:
              i+=1
        else:
            i+=1


    print(string)
    if string.find("Whether you're a student") == -1:
        engine = pyttsx3.init()
        engine.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")       
        engine.say(string)
        engine.runAndWait()
defineWord(stringStarter)