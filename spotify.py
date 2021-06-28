import csv

class Song:   
    def __init__(self, track, artist, genre, bpm, energy, danceability, length):
        self.track = track
        self.artist = artist
        self.genre = genre
        self.bpm = bpm
        self.energy = energy
        self.danceability = danceability
        self.length = length

    def __str__(self):  
        #me retorna los objetos como string 
        return self.track + ',' + self.artist + ',' + self.genre + ',' + str(self.bpm) + ',' + str(self.energy) + ',' + str(self.danceability) + ',' + str(self.length)

    def change_speed(self, relative_bpm):
            self.bpm = self.bpm + relative_bpm
            self.energy = self.energy + (2 * relative_bpm)
            self.danceability = self.danceability + (3 * relative_bpm)
            self.length = self.length - relative_bpm

    @staticmethod
    def load_songs(input_file):
        all_songs = [] #Lista que me va a almacenar el contenido de song
        file = open(input_file, encoding='utf8')
        reader = csv.reader(file, delimiter=',')
        #Con este for añadimos linea a linea y columna a columna el contenido de input_file en la lista songs
        #row = [track, artist, genre, bpm, energy, danceability, length ]
        for row in reader:
            track = str(row[0])
            artist = str(row[1])
            genre = str(row[2])
            bpm = int(row[3])
            energy = int(row[4])
            danceability = int(row[5])
            length = int(row[6])
            song = Song(track, artist, genre, bpm, energy, danceability, length)
            all_songs.append(song)
        return all_songs

    @staticmethod
    def save_songs(songs, output_file):
        with open(output_file, 'w', encoding='utf8', newline='\n') as output:
            writer = csv.writer(output, delimiter = '\n', quoting = csv.QUOTE_MINIMAL)
            writer.writerow(songs)
