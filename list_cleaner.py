import re

# Specify the file path
file_path = 'source2.txt'

# Open the file and read its content into a string
with open(file_path, 'r') as file:
    data = file.read()

# Regex pattern to match article names within [[ ]]
pattern = r"\[\[(.*?)\]\]"

# Find all matches
matches = re.findall(pattern, data)

# Filter and clean up matches to get only the article names, remove duplicates, and exclude articles containing "Wikipedia:"
articles = set()  # Using a set to automatically handle duplicates
for match in matches:
    # Split by "|" and take the first part if there's any "|"
    article = match.split("|")[0].strip()

    # Debugging output to see what's being processed
    print(f"Processing article: '{article}'")

    # Exclude articles containing "Wikipedia:"
    if ":" not in article:
        articles.add(article.replace(" ","_"))  # Add to set, which avoids duplicates

# Convert the set back to a sorted list if order matters
articles = sorted(articles)

# Print the list of articles
for article in articles:
    print(article)

# Step 2: Write the list of articles to a text file
with open("articles2.txt", "w") as file:
    for article in articles:
        file.write(article + "\n")
