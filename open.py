import os
import openai
import json
from api_secrets import API_KEY

# Load your API key from an environment variable or secret management service
openai.api_key =API_KEY

text=input("enter the text:")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"meaning of:\n\n{text}",
  temperature=0.7,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
answer=response.choices[0].text.strip()
print(answer)















# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Convert movie titles into emoji.\n\nBack to the Future: 👨👴🚗🕒 \nBatman: 🤵🦇 \nTransformers: 🚗🤖 \nStar Wars:",
#   temperature=0.8,
#   max_tokens=60,
#   top_p=1.0,
#   frequency_penalty=0.0,
#   presence_penalty=0.0,
#   stop=["\n"]
# )
# print(response)






# openai.api_key =API_KEY
# response = openai.Image.create(
#   prompt="a white siamese cat",
#   n=1,
#   size="1024x1024"
# )
# image_url = response['data'][0]['url']








# "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"