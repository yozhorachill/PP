import pygame
pygame.init()
clock=pygame.time.Clock()
W=500
H=700
sc=pygame.display.set_mode((W,H))
pygame.display.set_caption("PLAYLIST")

WHITE=(255,255,255)
FPS=60

sc.fill(WHITE)

music_files = ["C:\Users\админ\Desktop\PP2\Travis Scott - MY EYES.mp3", 
               "C:\Users\админ\Desktop\PP2\Lord Huron-The Night We Met.mp3", 
               "C:\Users\админ\Desktop\PP2\o you.mp3"]
current_track_index = 0

meeyes=pygame.image.load("C:\Users\админ\Desktop\PP2\myeyes.jpeg").convert_alpha()
meeyes=pygame.transform.scale(meeyes, (500,200))
thenightwemet=pygame.image.load("C:\Users\админ\Desktop\PP2\thenightwemet.jpg")
thenightwemet=pygame.transform.scale(thenightwemet, (500,200))
ballwoyou=pygame.image.load("C:\Users\админ\Desktop\PP2\bwu.jpeg")
ballwoyou=pygame.transform.scale(ballwoyou, (500,200))

myfont=pygame.font.SysFont('ariel', 110)
text_surface=myfont.render('MY PLAYLIST', 1 , 'Black')

pygame.mixer.init()
pygame.mixer.music.load(music_files[current_track_index])

def next_song():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track_index])
    pygame.mixer.music.play()
    

def last_song():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track_index])
    pygame.mixer.music.play()



playing=False
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_LEFT:
                last_song()

    sc.blit(meeyes, (0,100))
    sc.blit(thenightwemet, (0,300))
    sc.blit(ballwoyou, (0,500))
    sc.blit(text_surface , (5,15))

    pygame.display.flip()  

    clock.tick(FPS)