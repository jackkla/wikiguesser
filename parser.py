import re
import random

def split_and_filter_text(text, article_name):
  """Splits text by newline or ". " and filters sentences by length.

  Args:
    text: The text string to process.

  Returns:
    A list of sentences that meet the criteria.
  """

  # Split text into sentences using regex
  article_name = article_name.replace("_"," ")
  re_query = r"\n|\.\s+"
  sentences = re.split(re_query, text, flags=re.IGNORECASE)



  # Filter sentences based on word count
  long_sentences = [sentence for sentence in sentences if len(sentence.split()) >= 15]
  if len(long_sentences) > 5:
    random.shuffle(long_sentences)
    long_sentences = long_sentences[0:4]
  return long_sentences

# Example usage with a text string
text = """This is a sample text. 
This is another sentence. This one is quite long, don't you think, but it could be longer. 
This is a shorter sentence."""

import requests


def get_redirects(article_title):
  # Step 1: Get the page ID of the article
  url = f"https://en.wikipedia.org/w/api.php"
  params = {
    "action": "query",
    "titles": article_title,
    "format": "json"
  }
  response = requests.get(url, params=params)
  data = response.json()

  # Extract the page ID
  page_id = list(data['query']['pages'].keys())[0]

  if page_id == "-1":
    return f"Article '{article_title}' does not exist."

  # Step 2: Get the redirects to this page
  params = {
    "action": "query",
    "prop": "redirects",
    "pageids": page_id,
    "rdprop": "title",
    "format": "json",
    "rdlimit": "max"
  }
  response = requests.get(url, params=params)
  data = response.json()

  # Extract the list of redirects
  redirects = data['query']['pages'][page_id].get('redirects', [])

  # Return the list of redirect titles
  return [redirect['title'].lower() for redirect in redirects]


