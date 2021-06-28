import sys
from spotify import Song

'''Information about headers in datafile
0: track name
1: artist name
2: genre
3: beats per minute
4: energy
5: danceability
6: length'''
__name__ == '__main__'
if __name__ == '__main__':
    input_file = 'top50.csv'
    output_file = 'top50_mod.csv'
    relative_bpm = int(sys.argv[1])  # read keyboard input
    
    # load songs (from input_file)
    all_songs = Song.load_songs(input_file)

    # change speed of all songs
    for i in range(len(all_songs)):
        all_songs[i].change_speed(relative_bpm)

    
    
    # save songs (to output_file)
    Song.save_songs(all_songs, output_file)

