import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_TOKEN')

class Chatbot:
    def __init__(self):
        self.prompt = """You are a chatbot who goes by the name of Frederick, Fred for close friends. You are very happy and always reply with a funny pun.
       
Josh: Hey Frederick, how are you doing?

Frederick (you): I'm doing well, thanks for asking. How about you?"""


    def extend_prompt(self, author, message):
        self.prompt += "\n{}: {}".format(author, message)
        if author is not '': self.prompt += "\nFrederick (you): "


    def generate_response(self):
        res = openai.Completion.create(
            engine = "text-davinci-002",
            prompt = self.prompt,
            temperature = 0.7,
            top_p = 1,
            max_tokens = 200,
            frequency_penalty = 0,
            presence_penalty = 0
        )

        msg = res.choices[0].text
        while msg[0] == ':': msg = msg[1:]

        self.extend_prompt('', msg)
        return msg


    def print_prompt(self):
        print('########################################')
        print(self.prompt)
        print('########################################')
        return self.prompt