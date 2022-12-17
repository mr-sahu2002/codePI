# import nltk
# nltk.download()

from rake_nltk import Rake
rake_nltk_var = Rake()

text = """ Keywords play an important role when reading a long text to understand the subject and context of the text. Search engines also analyze an article’s keywords before indexing it. In this article, I will walk you through how to extract keywords using Python.

Well, we can also train a machine learning model that will extract keywords, but here I am just going to walk you through how to use a Python library for this task so that even beginners can understand how extracting keywords work before training a machine learning model."""

rake_nltk_var.extract_keywords_from_text(text)
keyword_extracted = rake_nltk_var.get_ranked_phrases()
print(keyword_extracted)


