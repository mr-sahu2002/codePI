#import all the required library
import os
import openai
from api_secrets import API_KEY
from extract_key import keyword_extracted,text
from colorama import Fore, Back, Style

# Load your API key from an environment variable or secret management service
openai.api_key =API_KEY

#array of keywords
keyword=keyword_extracted

print(Back.GREEN +"MEANING:")
# find the meaning for each key word
for i in keyword:
    #give a response to the user in json format
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"meaning of:\n\n{i}",
    temperature=0.7,
    max_tokens=64,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )

    # extract the text from the json file
    answer=response.choices[0].text.strip()
    print(Fore.GREEN +f"{i} : {answer}")
    print("-------------------------------------------------------------------------------------")

print("=====================================================================================")

#text or paragraph summary
print(Back.YELLOW +"SUMMARY:")
summary = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Summarize this for a second-grade student:\n\n{text}",
    temperature=0.7,
    max_tokens=64,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )

answer=summary.choices[0].text.strip()
print(Fore.YELLOW +answer)






















