# import nltk
# nltk.download()
from colorama import Fore, Back, Style
from rake_nltk import Rake
rake_nltk_var = Rake()


text = '''
Once upon a time ther was a girl who fell in love with a boy, but the boy did not love her back.this made the girl verysad, so started dating another boy. He was very handsome.
'''

#extracting the keyword from the content or text
rake_nltk_var.extract_keywords_from_text(text)
keyword_extracted = rake_nltk_var.get_ranked_phrases()

print(Back.RED +"KEYWORDS:")
# print(keyword_extracted)
for i in keyword_extracted:
    print(Fore.RED + f">{i}")

print("--------------------------------------------------------------------------")











