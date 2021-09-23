import numpy as np


def make_pairs(corpus):
    for i in range(len(corpus) - 1):
        yield(corpus[i], corpus[i+1])
    

def generate_lyrics(artist, first_word='', n_words = 10):
    with open(f'lyrics/{artist}.txt') as f:
        speech = f.read()

    corpus = speech.split()
    pairs = make_pairs(corpus)

    word_dict = {}

    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]

    if first_word not in corpus:
        first_word = np.random.choice(corpus)

    chain = [first_word]

    for i in range(n_words):
        chain.append(np.random.choice(word_dict[chain[-1]]))
    return (' '.join(chain).lower())

