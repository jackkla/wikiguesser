from flask import Flask, render_template, request, session, redirect, url_for
import random
import wiki_downloader
import parser
import re

app = Flask(__name__)
app.secret_key = 'd781bd371c769716cbeb182e0f8f3588a23acc761ef57e60'  # Make sure to replace this with your actual secret key


def get_random_article(article_list):
    article_title = random.choice(article_list)
    article = wiki_downloader.get_wikipedia_full_text(article_title)
    article_title = article_title.replace("_", " ")
    sentences = parser.split_and_filter_text(article, article_title)
    return article_title, sentences


@app.route('/', methods=['GET', 'POST'])
def game():
    if 'guesses_left' in session and session['guesses_left'] == 0:
        session.clear()

    if 'article_list' not in session:
        with open("articles.txt", "r") as f:
            lines = f.readlines()
            random_lines = random.sample(lines, 2)
            session['article_list'] = [line.strip() for line in random_lines]
        print(session['article_list'])

    if 'correct_article' not in session or 'sentences' not in session or 'guesses_left' not in session:
        print(f"correct_article in session? {'correct_article' in session}")
        print(f"sentences in session? {'sentences' in session}")
        print(f"guesses_left in session? {'guesses_left' in session}")
        # Start a new game
        correct_article, sentences = get_random_article(session['article_list'])
        session['correct_article'] = correct_article
        session['redirects'] = parser.get_redirects(session['correct_article'])
        print(correct_article)
        print(session['redirects'])
        session['sentences'] = sentences
        session['guesses_left'] = 3
        first_sentence = random.choice(sentences)
        session['sentences'].remove(first_sentence)
        session['shown_sentences'] = [first_sentence]
        session['incorrect_guesses'] = []

    if request.method == 'POST':
        guess = request.form['guess']
        correct_article = session['correct_article']
        subbed_article = re.sub(" [\(\[].*?[\)\]]", "", correct_article)
        print(subbed_article)
        if guess.lower() in session[
            'redirects'] or guess.lower() == subbed_article.lower() or guess.lower() == correct_article.lower():
            result = "Correct! You've guessed the article."
            return render_template('result.html', result=result, article=correct_article)
        else:
            session['guesses_left'] -= 1
            if guess.lower() not in [g.lower() for g in session['incorrect_guesses']]:
                session['incorrect_guesses'].append(guess)

            if session['guesses_left'] > 0:
                # Generate another random sentence from the same article
                new_sentence = random.choice(session['sentences'])
                session['sentences'].remove(new_sentence)
                session['shown_sentences'].append(new_sentence)
                result = f"Incorrect. You have {session['guesses_left']} guesses left. Here's another sentence:"
            else:
                result = "Out of guesses. Game over!"
                return render_template('result.html', result=result, article=correct_article)

        # Ensure session changes are saved
        session.modified = True
        return render_template('game.html',
                               sentences=session['shown_sentences'],
                               guesses_left=session['guesses_left'],
                               incorrect_guesses=session['incorrect_guesses'],
                               result=result)

    return render_template('game.html',
                           sentences=session['shown_sentences'],
                           guesses_left=session['guesses_left'],
                           incorrect_guesses=session.get('incorrect_guesses', []))


@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('game'))


if __name__ == '__main__':
    app.run(debug=False)