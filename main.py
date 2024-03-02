import pyttsx3

if __name__ == '__main__':
    print("Welcome to my first python project")
    while True:
        myInput = input("Write what you want to say: ")

        # initializing the text-to-speech library:
        speak = pyttsx3.init()
        # speed of speech:
        speak.setProperty('rate', 150)

        # exit condition:
        if myInput.lower() in ["exit"]:
            speak.say("That's all for today. Thank you!")
            speak.runAndWait()
            break

        # speaking function:
        message = f"{myInput}"
        speak.say(message)

        # ensures the program not exit before completing the speaking function:
        speak.runAndWait()
