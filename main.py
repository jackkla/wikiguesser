import random
import wiki_downloader
import sentence_parser
import llm
import sys


def get_random_article(article_list):
    article_title = random.choice(article_list)
    article = wiki_downloader.get_wikipedia_full_text(article_title)
    article_title.replace("_"," ")
    sentences = sentence_parser.split_and_filter_text(article, article_title)
    sentences = [s for s in sentences if article_title.lower() not in s.lower()]
    return article_title, sentences


def article_guessing_game(article_list):
    correct_article, sentences = get_random_article(article_list)
    correct_article = correct_article.replace("_"," ")
    random_sentence = random.choice(sentences)
    print("New sentence: " + random_sentence)

    guesses_left = 3
    while guesses_left > 0:
        guess = input("Which article is this sentence from? (You have {} guesses left): ".format(guesses_left))
        guesses_left -= 1
        guess = guess.lower()
        if guess in sentence_parser.get_redirects(correct_article):
            print("Correct!")
            return
        elif guesses_left >= 1:
            if len(sys.argv) > 1 and sys.argv[1] == "-ai":
                llm_response = llm.ask(correct_article, guess)['message']['content']
                print("AI response: " + llm_response)
                if ("yes" in llm_response.lower()):
                    print("Close enough! - Says the AI :) The answer was {}".format(correct_article))
                    break
            # Generate another random sentence from the same article index
            while True:
                additional_sentence = random.choice(sentences)
                if additional_sentence != random_sentence:
                    break


            print("Incorrect. Here's another sentence from the same article:", additional_sentence)

    print("Out of guesses. The correct answer was:", correct_article)

#Example usage:
with open("articles.txt", "r", errors="ignore") as f:
    article_names = [line.strip() for line in f]
while True:
    article_guessing_game(article_names)

