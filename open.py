# import openai
# from api_secrets import API_KEY

# openai.api_key="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"

# prompt= "say this is a test"

# response=openai.Completion.create(engine="text-danvinci-004",prompt=prompt,max_tokens=6)
# print(response)
import os
import openai
from api_secrets import API_KEY

# Load your API key from an environment variable or secret management service
openai.api_key =API_KEY

response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)
print(response)


# openai.api_key =API_KEY
# response = openai.Image.create(
#   prompt="a white siamese cat",
#   n=1,
#   size="1024x1024"
# )
# image_url = response['data'][0]['url']








# "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"