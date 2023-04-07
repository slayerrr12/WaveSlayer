import tkinter as tk
from tkinter import Text, Button

import pyttsx3
import speech_recognition as sr


import openai

# Set up the OpenAI API credentials
openai.api_key = "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"

# Initialize the text to speech engine 
engine=pyttsx3.init()


def record_audio():
    """
    Records audio from microphone and returns text.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None
def speak_text(text):
    engine.say(text)
    engine.runAndWait()
def generate_response(prompt):
    """
    Generates a response using OpenAI API and returns it.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]

def assistant():
    """
    Triggers the voice assistant and generates response.
    """
    # record audio and convert to text
    text = record_audio()
    if text:
        # generate response using OpenAI API
        prompt = "User: " + text + "\nAI:"
        response = generate_response(prompt)
    else:
        response = "Sorry, I didn't hear you."
    
    # display response in text box
    response_text.insert(tk.END, response + "\n")

    # convert response to audio and play
    speak_text(response)

# create the GUI
root = tk.Tk()
root.title("Custom Voice Assistant")

# create a text box to display responses
response_text = Text(root, height=10, width=50)
response_text.pack()

# create a button to trigger the assistant
button = Button(root, text="Speak", command=assistant)
button.pack()

root.mainloop()