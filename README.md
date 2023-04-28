# AI-CHATBOT

This is a simple AI chatbot project built using Python and natural language processing techniques. The chatbot uses a pre-trained language model to understand and generate responses to user input.

## Requirements

To run this chatbot, you will need to have Python 3.x installed on your system. You will also need to install the following packages:

- `tensorflow`
- `nltk`

You can install these packages using the following command:

```
pip install tensorflow nltk
```

## Usage

To start the chatbot, simply run the `chatbot.py` script using Python:

```
python chatbot.py
```

Once the chatbot is running, you can start a conversation by typing in your message and pressing Enter. The chatbot will generate a response based on the message you have provided.

## Customization

If you want to customize the chatbot to better fit your needs, you can modify the `intents.json` file. This file contains the training data for the language model, and defines the various intents that the chatbot can recognize.

You can add new intents or modify existing ones by editing this file. Once you have made changes to the `intents.json` file, you will need to retrain the language model by running the `train_chatbot.py` script:

```
python train_chatbot.py
```

This will generate a new set of model files that the chatbot will use to generate responses.

## Credits

This project was created by [slayerrr12](https://github.com/slayerrr12). The pre-trained language model used in this project was provided by [OpenAI](https://openai.com/).
