import pyttsx3  # This module helps convert text to speech
import speech_recognition as sr  # For speech recognition
import webbrowser  # For opening websites
import datetime  # For getting the current date and time
import pyjokes  # For generating jokes
import os  # For working with files and directories
import time  # For adding delays

def sptext():
    """
    Function to convert speech to text and store it in a variable.
    """
    recognizer = sr.Recognizer()  # Create a recognizer object
    with sr.Microphone() as source:  # Use the microphone as the audio source
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise to improve recognition
        audio = recognizer.listen(source)  # Listen to the source
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)  # Recognize speech using Google Web Speech API
            print(data)  # Print the recognized text
            return data
        except sr.UnknownValueError:
            print("Can't Understand")
            return ""

def speechtx(x):
    """
    Function to convert text to speech.
    """
    engine = pyttsx3.init()  # Initialize the text-to-speech engine
    voices = engine.getProperty('voices')  # Get the available voices
    engine.setProperty('voice', voices[1].id)  # Set the voice to female (index 1)
    engine.setProperty('rate', 120)  # Set the speech rate
    engine.say(x)  # Convert the text to speech
    engine.runAndWait()  # Wait until speaking is done

if __name__ == '__main__':
    # Initial check for the activation phrase 'hey alexa'
    if 'hey alexa' in sptext().lower():
        while True:
            data1 = sptext().lower()  # Convert spoken text to lowercase and store it in data1

            if "your name" in data1:
                # If the user asks for the assistant's name
                name = "My name is Alexa"
                speechtx(name)  # Convert the response text to speech

            elif "old are " in data1:
                # If the user asks for the assistant's age
                age = "I am 10 years old"
                speechtx(age)  # Convert the response text to speech

            elif 'time' in data1:
                # If the user asks for the current time
                current_time = datetime.datetime.now().strftime("%I:%M %p")  # Get the current time in 12-hour format
                speechtx(current_time)  # Convert the time to speech

            elif 'youtube' in data1:
                # If the user asks to open YouTube
                webbrowser.open("https://www.youtube.com/")  # Open YouTube in the web browser

            elif 'joke' in data1:
                # If the user asks for a joke
                joke_1 = pyjokes.get_joke(language="en", category="neutral")  # Get a neutral joke
                print(joke_1)  # Print the joke
                speechtx(joke_1)  # Convert the joke to speech

            elif 'play song' in data1:
                # If the user asks to play a song
                add = r"C:\Users\Soldier\Desktop\Songs"  # Path to the directory containing songs
                listsong = os.listdir(add)  # List all files in the directory
                print(listsong)  # Print the list of songs
                if listsong:
                    os.startfile(os.path.join(add, listsong[0]))  # Open the first song in the list
                else:
                    print("No songs found in the directory.")
                    speechtx("No songs found in the directory.")
                
            elif 'exit' in data1:
                # If the user says 'exit', end the program
                speechtx("Thank you")
                break  # Exit the loop

            time.sleep(5)  # Wait for 5 seconds before the next iteration
            
    else:
        print("Thanks")
