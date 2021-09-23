import lyricsgenius
import re

def get_lyrics(artist, songs = 10):
    """Generates a text file that contains the top lyrics of an artist

    Args:
        artist (string): The artist that you would like the lyrics for
        songs (int, optional): The max number of songs you would like within the text file. Defaults to 10.
    """

    with open('authentication.txt') as f:
        client_access_token = f.read()

    LyricsGenius = lyricsgenius.Genius(client_access_token)

    musician = LyricsGenius.search_artist(artist, max_songs=songs)

    total_lyrics = ''
    for song in musician.songs:
        total_lyrics = total_lyrics + (song.lyrics[:-30])
    x = re.sub('\[.*\]', '', total_lyrics)

    with open(f'lyrics/{artist}.txt' , 'w') as f:
        f.write(x)
