from textblob import TextBlob


def main():
    string = 'fucking what the fuck bro'
    wiki = TextBlob(string)

    # Sentence sentiment
    value = wiki.sentiment
    print(f'Sentence Sentiment {value}')

    # each  word in sentence sentiment+
    words = wiki.words
    eachWordValue = [(x , TextBlob(x).sentiment) for x in words ]
    pprint.pprint(eachWordValue)

