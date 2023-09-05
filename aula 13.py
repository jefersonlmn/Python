pygame.init()
pygame.mixer.music.load('sondame.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

if vezes ==1:
    pygame.mixer.init()
    pygame.mixer.music.load('solo.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()

elif musicas ==2:

    pygame.init()
    pygame.mixer.music.load('sondame.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()

elif musicas ==3:
    pygame.init()
    pygame.mixer.music.load('bateria.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
else:
    print('Opção Invalida')