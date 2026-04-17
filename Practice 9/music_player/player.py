import pygame

class Player:
    def __init__(self, songs):
        self.songs = songs
        self.index = 0
        self.state = "stopped"

        pygame.mixer.init()
        pygame.mixer.music.load(self.songs[self.index])

    def play(self):
        pygame.mixer.music.play()
        self.state = "playing"

    def stop(self):
        pygame.mixer.music.stop()
        self.state = "stopped"

    def next(self):
        self.index = (self.index + 1) % len(self.songs)
        pygame.mixer.music.load(self.songs[self.index])
        pygame.mixer.music.play()
        self.state = "playing"

    def prev(self):
        self.index = (self.index - 1) % len(self.songs)
        pygame.mixer.music.load(self.songs[self.index])
        pygame.mixer.music.play()
        self.state = "playing"

    def get_track_name(self):
        return self.songs[self.index].split("/")[-1]