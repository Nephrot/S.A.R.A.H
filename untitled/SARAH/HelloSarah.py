import speech_recognition as sr
import random
import pyttsx3
import numpy
import num2words
import numpy
import ast
import math
import re
import sys
import tkinter as tk
import random
import time
import threading 
from tkinter import *

# ctrl alt m
def detectIfNumber(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          return 1 == 0

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current != 0

def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

bool = 0   
def text2operation(textnum, numwords={}):
    if not numwords:
      basic = [
        "plus", "added to", "minus", "subtracted by"
      ]
    if(textnum == "plus"):
        return "+"
    elif(textnum == "added"):
        return "+"
    elif(textnum == "minus"):
        return "-"
    elif(textnum == "multiplied"):
        return "*"
    elif (textnum == "times"):
        return "*"
    elif (textnum == "divided"):
        return "/"
    elif (textnum == "over"):
        return "/"
    elif(textnum == "subtracted"):
        return "-"
    elif(textnum == "of"):
        return "("
    elif (textnum == "end"):
        return ")"
    else:
        return ""

def createBasicProblem(string):
 
    num = ""
    equation = ""
    stringArray = string.split()
    i = 0
    something = 0
    savedOperation = ""
    degMode = 0;
    while i < len(stringArray):
        if(stringArray[i][len(stringArray[i])-2:len(stringArray[i])]== "th"):
          stringArray[i] = stringArray[i].replace("th", "")
        if detectIfNumber(stringArray[i]):
            num += stringArray[i] + " "
        elif(stringArray[i] == "hundred"):
            num += stringArray[i] + " "
        elif (stringArray[i] == "thousand"):
            num += stringArray[i] + " "
        elif (stringArray[i] == "million"):
            num += stringArray[i] + " "
        elif (stringArray[i] == "trillion"):
            num += stringArray[i] + " "
        elif (stringArray[i] == "point"):
            num = text2int(num)
            if (num != 0):
                equation += str(num)
                num = ""
            equation += "."

        elif (stringArray[i] == "by"):
            num = num
        elif (stringArray[i] == "of"):
            num = num
        elif (stringArray[i] == "the"):
            num = num
        elif (stringArray[i] == "mode"):
            num = num
        elif (stringArray[i] == "group"):
            equation += str("(");
        elif (stringArray[i] == "pow"):
            equation += str("math.pow(")
            something = 1
        elif (stringArray[i] == "how"):
            equation += str("math.pow(")
            something = 1
        elif (stringArray[i] == "squared"):
            equation += str(", 2");
        elif (stringArray[i] == "cubed"):
            equation += str(", 3");
        elif (stringArray[i] == "first"):
            equation += str("1");
        elif (stringArray[i] == "second"):
            equation += str("2");
        elif (stringArray[i] == "third"):
            equation += str("3");
        elif (stringArray[i] == "fif"):
            equation += str("5");
        elif (stringArray[i] == "eigh"):
            equation += str("8");
        elif (stringArray[i] == "nin"):
            equation += str("9");
        elif (stringArray[i] == "twelf"):
            equation += str("12");
        elif (stringArray[i] == "twentieth"):
            equation += str("20");
        elif (stringArray[i] == "thirtieth"):
            equation += str("30");
        elif (stringArray[i] == "fourtieth"):
            equation += str("40");
        elif (stringArray[i] == "fiftieth"):
            equation += str("50");
        elif (stringArray[i] == "deg"):
            equation += str("math.degrees(");
        elif (stringArray[i] == "rad"):
            equation += str("math.radians(");
        elif (stringArray[i] == "sine"):
            equation += str("math.sin(");
        elif (stringArray[i] == "cos"):
            equation += str("math.cos(");
        elif (stringArray[i] == "cosine"):
            equation += str("math.cos(");
        elif (stringArray[i] == "tan"):
            equation += str("math.tan(");
        elif (stringArray[i] == "tangent"):
            equation += str("math.tan(");
        elif (stringArray[i] == "arcsine"):
            equation += str("math.asin(");
        elif (stringArray[i] == "arccos"):
            equation += str("math.acos(");
        elif (stringArray[i] == "arccosine"):
            equation += str("math.acos(");
        elif (stringArray[i] == "arctan"):
            equation += str("math.atan(");
        elif (stringArray[i] == "arctangent"):
            equation += str("math.atan(");
        elif (stringArray[i] == "factorial"):
            equation += str("math.factorial(");
        elif (stringArray[i] == "e"):
            equation += str("math.exp(");
        elif (stringArray[i] == "square"):
            equation += str("math.sqrt(");
        elif (stringArray[i] == "cube"):
            equation += str("numpy.cbrt(");
        elif (stringArray[i] == "degrees"):
            equation += str("math.degrees(");
        elif (stringArray[i] == "radians"):
            equation += str("math.radians(");
        elif (stringArray[i] == "pi"):
            equation += str("math.pi");
        elif (stringArray[i] == "exit"):
            num = text2int(num)
            if (num != 0):
                equation += str(num)
            equation += str(")")
            num = ""
            #Nothing Happens
        elif (stringArray[i] == "to"):
            equation += str(", ")
            something = 0
        elif(stringArray[i] == "zero"): 
            num = num
        elif (stringArray[i] == "plus"):
            num = text2int(num)
            savedOperation = str(text2operation(stringArray[i]))
            if(num != 0):
                    equation += str(num)
            equation += str(text2operation(stringArray[i]))
            num = ""
        elif (stringArray[i] == "minus"):
            num = text2int(num)
            savedOperation = str(text2operation(stringArray[i]))
            if(num != 0):
                    equation += str(num)
            equation += str(text2operation(stringArray[i]))
            num = ""
        elif (stringArray[i] == "over"):
            num = text2int(num)
            savedOperation = str(text2operation(stringArray[i]))
            if(num != 0):
                    equation += str(num)
            equation += str(text2operation(stringArray[i]))
            num = ""
        elif (stringArray[i] == "times"):
            num = text2int(num)
            savedOperation = str(text2operation(stringArray[i]))
            if(num != 0):
                    equation += str(num)
            equation += str(text2operation(stringArray[i]))
            num = ""
        else:
            num = num
        i += 1

    num = text2int(num)
    if (num != 0):
        equation += str(num)
    equationArray = list(equation)
    j = 0
    k = 0
    while j < len(equationArray):
        if(equationArray[j] == "("):
           k += 1
        elif (equationArray[j] == ")"):
           k += 1
        j+=1
    if k % 2 != 0:
        equation += ")"
    equation.replace(" ", "")
    return(equation)

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def getMicOutput(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

       Test for hello value
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, None, 12)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValu  eError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

def operator():
    print("no")

def mainProgram(bool):
    while 10 > 0:
        equationSaved = ""
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        print("Say hello to S.A.R.A.H the Speech And Recognition Arithmetic Helper")

        HELLO = ["turn on sarah", "hello sarah", "wake up sarah", "get up sarah", "good morning sarah", "hi sarah", "good afternoon sarah", "good evening sarah",
                "what's new sarah", "hey sarah", "what's up sarah", "howdy sarah", "g'day sarah", "morning sarah"] 
        while bool == 0:
            callback()
            engine = pyttsx3.init()
            engine.setProperty('voice',
                                        "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
            
            engine.say("Say hello to me, Sarah, the Speech And Recognition Arithmetic Helper?")
            engine.runAndWait()
            callback3()
            PROMPT_LIMIT = 5
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()

            for j in range(PROMPT_LIMIT):
                guess = getMicOutput(recognizer, microphone)
                if guess["transcription"]:
                    break 
                if not guess["success"]:
                    break
                print("I didn't catch that. What did you say?\n")
                # engine = pyttsx3.init()
                # engine.setProperty('voice',
                #                             "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
                # engine.say("I didn't catch that. What did you say?")
                # engine.runAndWait()
            
                
            tiamat = [None] * 1 
            


            # if there was an error, stop the game
            if guess["error"]:
                print("ERROR: {}".format(guess["error"]))
                #print (tiamat)
                break

            micOutput = "".format(guess["transcription"])
            print(guess["transcription"])
            i = 0
            for i in range(len(tiamat)):
                #if "guess" in tiamat:
                if guess["transcription"] == "hello Sarah":
                    rand = random.randint(1,4)
                    operator()
                    if rand == 1:
                        for voice in voices:
                            if voice.name[0] == "Microsoft Zira Desktop - English (United States)":
                                engine.setProperty('voice', voice.id)
                                break
                        engine = pyttsx3.init()
                        engine.setProperty('voice',
                                            "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
                        callback()
                        engine.say('Sarah is online.')
                        engine.runAndWait()
                        callback2()
                        bool = 1
                    if rand == 2:
                        for voice in voices:
                            if voice.name[0] == "Microsoft Zira Desktop - English (United States)":
                                engine.setProperty('voice', voice.id)
                                break
                        engine = pyttsx3.init()
                        engine.setProperty('voice',
                                            "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
                        callback()
                        engine.say("Hello")
                        engine.runAndWait()
                        callback2()
                        bool = 1
                    if rand == 3:
                        for voice in voices:
                            if voice.name[0] == "Microsoft Zira Desktop - English (United States)":
                                engine.setProperty('voice', voice.id)
                                break
                        engine = pyttsx3.init()
                        engine.setProperty('voice',
                                            "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
                        callback()
                        engine.say("Ready to get some math done")
                        engine.runAndWait()
                        callback2()
                        bool = 1
                    if rand == 4:
                        for voice in voices:
                            if voice.name[0] == "Microsoft Zira Desktop - English (United States)":
                                engine.setProperty('voice', voice.id)
                                break
                        engine = pyttsx3.init()
                        engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
                        callback()
                        engine.say("Ready to help")
                        engine.runAndWait()
                        callback2()
                        bool = 1
                if guess["transcription"] == "turn off": 
                    engine = pyttsx3.init()
                    engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
                    callback()
                    engine.say("Shutting Down")
                    engine.runAndWait()
                    callback3()
                    sys.exit()
        while bool == 1:
            PROMPT_LIMIT = 5
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()

            for j in range(PROMPT_LIMIT):
                guess = getMicOutput(recognizer, microphone)
                if guess["transcription"]:
                    break 
                if not guess["success"]:
                    break
                print("I didn't catch that. What did you say?\n")
                engine = pyttsx3.init()
                engine.setProperty('voice',
                                            "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
                callback()
                engine.say("I didn't catch that. What did you say?")
                engine.runAndWait()
                callback2()
            
                    
            x = (guess["transcription"])
            tiamat = [None] * 1 
            #print (x)
            t = x.split()
            i=0
            while i < len(t):

                #print(is_number(t[i]))
                #print("t" + t[i])
                if(hasNumbers(t[i])):
                    t[i] = t[i].replace("th", " ")
                if is_number(t[i]):
                    #print(t[i])
                    t[i] = num2words.num2words(t[i])
                    t[i] = t[i].replace("-", " ")
                    t[i] = t[i].replace(",", " ")
                
            
                if t[i] == "+":
                    t[i] = t[i].replace("+", "plus")
                if t[i] == "*":
                    t[i] = t[i].replace("*", "times")
                if t[i] == "/":
                    t[i] = t[i].replace("/", "over")
                if t[i] == "-":
                    t[i] = t[i].replace("-", "minus")
                
                    
                i+= 1
                
        
            
            p=0
            y=""
            while p < len(t):
                y += str(t[p]) + " "
                p+=1
            print("P:" + y)
            print((createBasicProblem(str(y))))
            
            
            # tiamat.append(t)
            #print(t)
            
            if(hasNumbers((createBasicProblem(str(y))))):
                try:
                    print((createBasicProblem(str(y))))
                    print(eval(str(createBasicProblem(str(y)))))
                    engine = pyttsx3.init()
                    engine.setProperty('voice',
                                            "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
                    callback()
                    engine.say(eval(str(createBasicProblem(str(y)))))
                    engine.runAndWait()
                    callback2()
                    equationSaved=y
                    bool = 2
                
                except SyntaxError:
                    print("BOIII")
                    engine = pyttsx3.init()
                    engine.setProperty('voice',
                                            "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
                    callback()
                    engine.say("Are you sure you are saying the equation properly, try again")
                    engine.runAndWait()
                    callback2()
            else:
                    print(str(y))
        while bool == 2:
            PROMPT_LIMIT = 5
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()

            for j in range(PROMPT_LIMIT):
                guess = getMicOutput(recognizer, microphone)
                if guess["transcription"]:
                    break 
                if not guess["success"]:
                    break
                print("I didn't catch that. What did you say?\n")
                engine = pyttsx3.init()
                engine.setProperty('voice',
                                            "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
                callback()
                engine.say("I didn't catch that. What did you say?")
                engine.runAndWait()
                callback2()
            
                
            tiamat = [None] * 1 
            


            # if there was an error, stop the game
            if guess["error"]:
                print("ERROR: {}".format(guess["error"]))
                #print (tiamat)
                break

            micOutput = "".format(guess["transcription"])
            print(guess["transcription"])
            i = 0
            for i in range(len(tiamat)):
                #if "guess" in tiamat:
                print(guess["transcription"].find("exit"))
                if guess["transcription"].find("again") > -1:
                    print((createBasicProblem(str(equationSaved))))
                    print(eval(str(createBasicProblem(str(equationSaved)))))
                    engine = pyttsx3.init()
                    callback()
                    engine.setProperty('voice',
                                            "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
                    engine.say(eval(str(createBasicProblem(str(equationSaved)))))
                    callback2()
                    engine.runAndWait()
                elif guess["transcription"].find("exit") > -1:
                    
                    engine = pyttsx3.init()
                    engine.setProperty('voice',
                                            "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
                    callback()
                    engine.say("Goodbye, come back soon!")
                    callback3()
                    engine.runAndWait()
                    bool = 0
                else:
                    engine = pyttsx3.init()
                    engine.setProperty('voice',
                                            "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
                    callback()
                    engine.say("What is your next problem")
                    callback2()
                    engine.runAndWait()
                    bool = 1
        

window = tk.Tk()


window.title("S.A.R.A.H")

window.geometry("1920x1080")
window.attributes("-fullscreen", True)


image = tk.PhotoImage(file="../SARAH/Hibernation.png")
smaller_image = image.subsample(5, 5)  
panel = tk.Label(window, image = smaller_image)


panel.pack(side = "bottom", fill = "both", expand = "yes")
panel.configure(background="black")

def callback():  
    img2 = tk.PhotoImage(file="../SARAH/Online.png")
    smaller_image = img2.subsample(5, 5)  
    panel.configure(background = "black", image=smaller_image)
    panel.image = smaller_image

def callback2():  
    img2 = tk.PhotoImage(file="C:\\Users\\qadada\\Videos\\Talking.png")
    smaller_image = img2.subsample(5, 5)  
    panel.configure(background = "black", image=smaller_image)
    panel.image = smaller_image 

def callback3():  
    img2 = tk.PhotoImage(file="C:\\Users\\qadada\\Videos\\Hibernation.png")
    smaller_image = img2.subsample(5, 5)  
    panel.configure(background = "black", image=smaller_image)
    panel.image = smaller_image 


timer = threading.Timer(0.1, mainProgram, args=(bool,)) 
timer.start() 
window.mainloop()  
     
