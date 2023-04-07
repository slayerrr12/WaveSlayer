Python Voice Assistant using OpenAI

This is a Python script that uses the OpenAI API to generate responses to voice input from the user.

Required Packages
The following packages are required to run the script:

tkinter for the GUI
pyttsx3 for text to speech conversion
speech_recognition for speech to text conversion
openai for natural language processing
Installation
You can install the required packages using pip:

Copy code
pip install tkinter pyttsx3 SpeechRecognition openai
Setup
Before running the script, you need to set up your OpenAI API credentials. You can do this by following the instructions on the OpenAI API documentation: https://beta.openai.com/docs/api-reference/authentication.

Once you have your API key, you can set it as an environment variable by running the following command in your terminal (replace YOUR_API_KEY with your actual API key):

arduino
Copy code
export OPENAI_API_KEY=YOUR_API_KEY
Alternatively, you can set the API key in the script itself by adding the following line at the beginning of the script (replace YOUR_API_KEY with your actual API key):

python
Copy code
import openai
openai.api_key = "YOUR_API_KEY"
Usage
To use the script, simply run the voice_assistant.py file:

Copy code
python voice_assistant.py
A GUI window will appear with a text box and a button. Click the button to start the voice assistant.

The assistant will listen for your voice input and generate a response using the OpenAI API. The response will be displayed in the text box and spoken aloud using text to speech conversion.

Functions
record_audio()
This function uses the Recognizer class from the speech_recognition library to record audio from the user's microphone and convert it to text using Google's Speech Recognition API. It returns the transcribed text.

speak_text()
This function uses the init() and say() methods from the pyttsx3 library to convert the generated response to speech and play it through the computer's speakers.

generate_response()
This function sends a prompt to the OpenAI API and returns the generated response. It uses the Completion class from the openai library to generate a response using the GPT-3 language model. The max_tokens parameter determines the maximum number of tokens that the API will generate, the temperature parameter determines the randomness of the generated response, and the n parameter determines the number of responses to generate.

assistant()
This function is the main function that triggers the voice assistant. It calls the record_audio() function to record the user's audio input, generates a response using the generate_response() function, displays the response in the GUI text box, and speaks the response aloud using the speak_text() function. If the user's input cannot be transcribed, the function displays an error message in the text box
