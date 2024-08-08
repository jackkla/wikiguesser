import re

def split_and_filter_text(text, article_name):
  """Splits text by newline or ". " and filters sentences by length.

  Args:
    text: The text string to process.

  Returns:
    A list of sentences that meet the criteria.
  """

  # Split text into sentences using regex
  re_query = r"\n|\.\s+"
  sentences = re.split(re_query, text, flags=re.IGNORECASE)

  # Filter sentences based on word count
  long_sentences = [sentence for sentence in sentences if len(sentence.split()) >= 10]

  return long_sentences

# Example usage with a text string
text = """This is a sample text. 
This is another sentence. This one is quite long, don't you think, but it could be longer. 
This is a shorter sentence."""


