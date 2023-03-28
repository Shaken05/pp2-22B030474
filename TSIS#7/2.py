import pygame

pygame.init()

# Set the window size
win_width = 400
win_height = 300

# Create the window
win = pygame.display.set_mode((win_width, win_height))

# Load the music files
music_files = ['music1.mp3', 'music2.mp3', 'music3.mp3']

# Set the initial song index
current_song_index = 0

# Load the first song
pygame.mixer.music.load(music_files[current_song_index])

# Set the volume
pygame.mixer.music.set_volume(0.5)

# Start playing the music
pygame.mixer.music.play()

# Main game loop
while True:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Pause or unpause the music
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_LEFT:
                # Play the previous song
                current_song_index -= 1
                if current_song_index < 0:
                    current_song_index = len(music_files) - 1
                pygame.mixer.music.load(music_files[current_song_index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_RIGHT:
                # Play the next song
                current_song_index += 1
                if current_song_index >= len(music_files):
                    current_song_index = 0
                pygame.mixer.music.load(music_files[current_song_index])
                pygame.mixer.music.play()

    # Update the screen
    win.fill((255, 255, 255))
    pygame.display.update()
