# Customer Support Chatbot

This chatbot is built using textbase ai. 
Basic features/ functionality include-

1. Attends to customers just like a customer support representative. gives the conversation the human touch, instead of pre-recorded automated responses.
   
2. More than half of the customer concerns will be solved by the chatbot. Which will decrease the requirement for customer support reps.
   
3. This can also be extended to prepare a report/ summary of the customer concerns/ complaints/ queries by storing them in a database. This will help to analyse common problems users are facing.

A detailed walkthrough of the chatbot is attached herewith, for reference- 

**Installation**

Make sure you have python version >=3.9.0

1. Through pip

pip install textbase-client

2. Local installation

Clone the repository and install the dependencies using Poetry (you might have to install Poetry first). As follows-                                                                                  git clone https://github.com/cofactoryai/textbase -> cd textbase -> poetry shell -> poetry install


if installed locally -> poetry run python textbase/textbase_cli.py test

if installed through pip -> textbase-client test

Response: Path to the main.py file: examples/openai-bot/main.py
