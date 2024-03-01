import pyttsx3

if __name__ == '__main__':
    while True:
        print("Welcome to my first python project")
        myInput = input("Write what you want to say: ")

        engine = pyttsx3.init() #initializing the text-to-speech engine
        engine.setProperty('rate', 150) # Set the Speed of speech

        if myInput == "exit":
            engine.say("That's all for today. Thank you!")
            break

        message = f"{myInput}"
        engine.say(message)

        engine.runAndWait()
