import wikipediaapi
import parser
import csv

def get_wikipedia_full_text(article_title):
    """
    Retrieves the full text of a Wikipedia article, including the summary and all sections.

    Args:
        article_title (str): The title of the Wikipedia article.

    Returns:
        str: The full text of the Wikipedia article.
    """
    # Create a Wikipedia API client
    wiki = wikipediaapi.Wikipedia(
        user_agent='Wikiguess (jacobklausner@gmail.com)',
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )

    # Get the page object for the specified article
    page = wiki.page(article_title)

    # Retrieve the full text of the article
    full_text = page.text

    return full_text
#
# # Read article names from file
# with open("articles.txt", "r") as f:
#     article_names = [line.strip() for line in f]
#
# # Create a dictionary to store the full text of each article
# article_texts = {}
# print(article_names)
#
# # Retrieve and save the full text for each article
# for article_name in article_names:
#     print(article_name)
#     full_text = get_wikipedia_full_text(article_name)
#     sentences = parser.split_and_filter_text(full_text, article_name)
#     sentences = [s for s in sentences if article_name.lower() not in s.lower()]
#     article_texts[article_name] = sentences
#
#
# with open('data.csv', 'w', newline='') as csvfile:
#     fieldnames = article_texts.keys()
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow(article_texts)
