from textbase import bot, Message
from textbase.models import OpenAI
from typing import List
import sqlite3
import os

# Load your OpenAI API key
OpenAI.api_key = "API key"

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT ="""This is a customer feedback taking bot. It can take feed back related to specefic products and at the same time address consumer concerns. 
first ask the customer for their name and customer id. then confirm their concern/ grievance and suggest solutions. finally ask them if their concern is resolved or not.
It will then also store the query in the database under customer_name, order_id, issue, action_taken, resolved/open. """

@bot()
def on_message(message_history: List[Message], state: dict = None):

    # Generate GPT-3.5 Turbo response
    bot_response = OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history, # Assuming history is the list of user messages
        model="gpt-3.5-turbo",
    )

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }
