class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"{self.title} - {self.artist}; {self.duration}"
    
class Playlist:
    def __init__(self, name):
        self.name = name
        self.song_list = []
    
    def add_song(self, song):
        """Adds a song to the list, but doesn't get added twice!"""
        if song not in self.song_list:
            self.song_list.append(song)
        else:
            print(f"'{song}' already exists in the playlist!")

    def remove_song(self, song_title):
        """Removes a song from the playlist if it exists."""
        if song_title in self.song_list:
            self.song_list.remove(song_title)

    def search_song(self, song_title):
        """Find and return the song from playlist if it exists."""
        if song_title in self.song_list:
            return f"Title: {song_title}"
        else:
            return f"'{song_title}' was not found in the playlist!"
        
    def __str__(self):
        return 

song_1 = Song("Ohona", "Janina", "4:30")
print(song_1)

my_playlist = Playlist("My Playlist")
my_playlist.add_song("Husn")
my_playlist.add_song("Meghomilone")
my_playlist.add_song("Ace of speads")
my_playlist.add_song("Tu haye Kaha")
my_playlist.add_song("Husn")
print(my_playlist.song_list)

my_playlist.remove_song("Husn")
print(my_playlist.song_list)

print(my_playlist.search_song("Husn"))
print(my_playlist.search_song("Tu haye Kaha"))