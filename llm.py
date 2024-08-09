import ollama

def ask(answer_phrase, user_phrase):
    response = ollama.chat(model='llama3.1', messages=[
        {
            'role': 'user',
            'content': '''
            Your job is to use your intelligence to determine if a player deserves to win a guessing game or not. You must be very strict with this, and lean towards not giving credit if you are unsure. You must respond in the format of a clear "yes" or "no", followed by the reasoning you used. The game is as follows. The player is given a random sentence from an article. The player must guess the name of the article. The game is automated by a computer, which means that we have a problem where the player may make a guess that is very similar in meaning to the correct answer, but not literally identical because of grammatical differences or trivial semantic differences. In this case, the computer would not give credit to the player, but we want to identify these situations and give them credit anyway, using your intelligence. Your job is to determine if the player's guess is identical to the actual answer, ignoring grammatical differences. Here are a few examples for you, with the answer first, and the player's guess second:

"alcohol" and "wine". No, "wine" is a specific type of alcohol, and "alcohol" refers to all alcohols.
"bread" and "yeast". No, "bread" is a significantly different product made with "yeast" as an ingredient.
"martial arts" and "martial law". No, "martial law" shares the word martial with "martial arts" but the actual meaning of each term is significantly different.
"hats" and "hat". Yes, "hats" is plural of "hat".
"companies" and "company". Yes, "companies" is plural of "company".
"george washington" and "washington". No, "george washington" refers to a specific person only. "washington" CAN refer to that same person, but it can also refer to the state of washington, or the district of columbia, or many other things.

Now, use your intelligence to solve this: "{}" and "{}".'''.format(answer_phrase.lower(), user_phrase.lower()),
        },
    ])
    return response