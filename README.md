# 310-Group-Project

## Project Description 

Our project is going to be an interactive chatbot that takes on the role of a would-be Atlantis explorer. The chatbot will only talk about things regarding Atlantis and will excitedly talk to the user about his upcoming adventure. The link to our GitHub repo is as follows https://github.com/edouarde1/310-Group-Project. 

## How to Run the Chat Bot 

1. Download our GitHub repo 
2. Open the repo using VSCode or Terminal 
3. run `run_me_first.sh` (If you are uncomfortable running a bash script refer to dependencies.) 
4. Run gui.py 

## Dependencies
This bot requires nltk, pyspechecker, and stanza in order to run properly. If you do not run first-time-setup.sh you will have to do the following
    
    pip install nltk
    pip install pyspellchecker
    pip install stanza
    
Then you have to run run_me_first.py so python can install the additional libraries. 

## Dataset 

#### corpus.txt
This txt file is pulled from the [Wikipedia page for Atlantis](https://en.wikipedia.org/wiki/Atlantis). This txt file was used as the corpus for our chat bot.
All these words are tokenized with NLTK and then implemented to a dictionary as keys as a JSON file. 


## Classes and Functions 

### Bot 
This directory includes all the files for the bot. 


### main.py
This is the main file where our program is executed. 

#### get_response(response, keywords)
This function recieves the keyword dictionary, asks for user input, and returns chat bot responses. User input is processed using `get_query_objects()`, which extracts nouns and proper nouns. A for-loop iterates through each processed noun in a list and detects if the word exists in entity_dict.json. If there is a match, that means there is a chat bot response for the keyword. If there is no keyword detected in the user response, then the bot returns "Sorry can't help provide any information that relates to [*whatever related noun the user entered*]". 

Parameters:
- response: a string input by the user acting as the key for keywords
- entity_dict: a .json file generated from entity_dict.py
  
Returns:
- output: a string containing the bots response

#### spell_check(input)
Takes a string and returns a string with closest related permutation that is part of the english language.

 Parameter:
 - input: a string input  

 Returns:
 - correct: a corrected string output 
    

### data_load.py

#### data_load(filepath):
Loads text from a file.

 Parameters:
 - filepath: file to path to retrieve text from 

 Returns:
  - contents: string of raw text
  

#### preproc(filepath)
Extracts the nouns and proper pouns from the user query. Takes a user query and runs string 
through Stanza's Dependency Parser. More information about this library is found here: 
(https://stanfordnlp.github.io/stanza/depparse.html)[https://stanfordnlp.github.io/stanza/depparse.html]

Parameters:
 - query: a string 

 Returns:
- obj_list: a list nouns and proper nouns from the user query 


#### dependencyParser(sentence)
Helper utility used to extract the depencies from a sentence. Runs the dp pipeline object 
in order to run depparse, lemma, and pos tagginig.

Parameters: 
 - sentence: a string 


### unitTest.py 

#### test_spell_check
Tests functionality of `spell_check()` function in bot.py

#### test_get_response()
Tests functionality of `get_response(query)` function in bot.py

#### test_load_data()
Tests functionality of `load_data()` 

## New Features

### Spell Checking

Spell checking was used in order to improve the overall robustness of our chatbot. Incorrectly spelt words are recognized by our system, and replaced with what is assumed to be the most likley word that the user intended to input. This allows our bot to handle a wide variety of cases that it previously was unable to.

### Synonym Detection

Synonym detection was used in our chatbot in order to improve the greeting function. Rather than hardcode a large if statement containing some number of standard greetings, we used synonym detection to recognize when a greeting word was input, in order to then output the bots standard greeting.

### POS Tagging, Tokenization & Segmentation

In order to better suit the keyword style bot that we have created, we needed to implement a way of understanding sentences that were input, and extract the necessary information required to generate a query that the bot can use to get a response. To do this, we used POS tagging, tokenization, and segmentation. These systems work together to process questions asked, and provide us with a query in the form of \<Noun\> \<Descriptor\> which we use to generate much more intricate and conversational dialogue.
