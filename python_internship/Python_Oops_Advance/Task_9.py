print("\n--- Create a MusicPlayer class and subclass Spotify to override play method. ---")

class MusicPlayer():
    def __init__(self):
        pass

    def play(self):
        print("Music player class is playing ")

class Spotify(MusicPlayer):
    def play(self):
        print("Spotify is playing ")

player = MusicPlayer()
player.play()

spotify_player = Spotify()
spotify_player.play()
