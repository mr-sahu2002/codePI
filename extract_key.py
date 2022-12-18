# import nltk
# nltk.download()
from colorama import Fore, Back, Style
from rake_nltk import Rake
rake_nltk_var = Rake()


text = '''python is a object oriented language use to develop web application, mobile apps & machine learning projects'''

#extracting the keyword from the content or text
rake_nltk_var.extract_keywords_from_text(text)
keyword_extracted = rake_nltk_var.get_ranked_phrases()

print(Back.RED +"KEYWORDS:")
# print(keyword_extracted)
for i in keyword_extracted:
    print(Fore.RED + f">{i}")

print("--------------------------------------------------------------------------")











