from lyrics import get_lyrics
from markov import generate_lyrics
from os.path import exists



artist = input("Enter the artist as shown in Genius: ")
# n_songs = input('Enter how many songs you would like in the corpus or press enter for 10: ')
# n_words = input("""Enter the number of words you want the output to be
#  or press enter for 10: """)
prompt = input('Enter a prompt or press enter for 10 random sentances: ')


if exists(f'lyrics/{artist.lower()}.txt') == False:
    get_lyrics(artist)

if prompt == '':
    for i in range(10):
        print(generate_lyrics(artist, prompt))
else:
    print(prompt + ' ' + generate_lyrics(artist, prompt))