import speech_recognition as sr
import random
import pyttsx3

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
        audio = recognizer.listen(source, 999999, 1.4)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
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

if __name__ == "__main__":
    engine = pyttsx3.init()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    print("Say hello to S.A.R.A.H the Speech And Recognition Arithmetic Helper")
    HELLO = ["turn on sarah", "hello sarah", "wake up sarah", "get up sarah", "good morning sarah", "hi sarah", "good afternoon sarah", "good evening sarah",
             "what's new sarah", "hey sarah", "what's up sarah", "howdy sarah", "g'day sarah", "morning sarah"]
    bool = 0;
    while bool == 0:
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

      print(guess)
      # if there was an error, stop the game
      if guess["error"]:
          print("ERROR: {}".format(guess["error"]))
          break

      # show the user the transcription



      micOutput = "".format(guess["transcription"])
      i = 0
      for i in range(len(HELLO)):
        if guess["transcription"].lower() == HELLO[i]:
             rand = random.randint(1,5);
             if rand == 1:
                 for voice in voices:
                     if voice.name[0] == "Microsoft Zira Desktop - English (United States)":
                         engine.setProperty('voice', voice.id)
                         break
                 engine = pyttsx3.init()
                 engine.setProperty('voice',
                                    "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
                 engine.say('Sarah is online.')
                 engine.runAndWait()
                 bool = 1
             if rand == 2:
                 for voice in voices:
                     if voice.name[0] == "Microsoft Zira Desktop - English (United States)":
                         engine.setProperty('voice', voice.id)
                         break
                 engine = pyttsx3.init()
                 engine.setProperty('voice',
                                    "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
                 engine.say("Hello")
                 engine.runAndWait()
                 bool = 1
             if rand == 3:
                 for voice in voices:
                     if voice.name[0] == "Microsoft Zira Desktop - English (United States)":
                         engine.setProperty('voice', voice.id)
                         break
                 engine = pyttsx3.init()
                 engine.setProperty('voice',
                                    "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
                 engine.say("Ready to get some math done")
                 engine.runAndWait()
                 bool = 1
             if rand == 4:
                 for voice in voices:
                     if voice.name[0] == "Microsoft Zira Desktop - English (United States)":
                         engine.setProperty('voice', voice.id)
                         break
                 engine = pyttsx3.init()
                 engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
                 engine.say("Ready to help")
                 engine.runAndWait()
                 bool = 1






