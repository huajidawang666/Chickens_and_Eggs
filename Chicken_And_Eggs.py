import pygame, sys, random, time
from pygame.locals import *

#Get available fonts
#print(pygame.font.get_fonts())


#Prepare for logs
timenow = time.localtime(time.time())

date = str(timenow.tm_year) + '_' + str(timenow.tm_mon) + '_' + str(timenow.tm_mday) + '_' + str(timenow.tm_hour) + '_' + str(timenow.tm_min) + '_' + str(timenow.tm_sec)
file = open('./log/log_'+date+'.txt', mode='w')


#Initialize
WIDTH_X = 1280
HEIGHT_Y = 720

n = 0

posx = [WIDTH_X/2]
posy = [HEIGHT_Y/2]

#Initialize Screen
pygame.init()

surface = pygame.display.set_mode(size=(WIDTH_X,HEIGHT_Y),flags=pygame.RESIZABLE)
pygame.display.set_caption("Chicken And Eggs")

egg = pygame.image.load("./egg.png").convert()
chicken = pygame.image.load("./chicken.png").convert()
count = pygame.image.load("./Count.png").convert()

font_name = pygame.font.match_font('simsun')
font = pygame.font.Font(font_name, 40)
text = font.render(f'{n-1}', True, 'black')

INGAME_WIDTH_X, INGAME_HEIGHT_Y = pygame.display.get_surface().get_size()

egg.set_colorkey((0,0,0))
chicken.set_colorkey((0,0,0))
count.set_colorkey((255,255,255))

surface.fill((60,194,251))

surface.blit(chicken, (INGAME_WIDTH_X/2 - 100, INGAME_HEIGHT_Y/2 - 175))
surface.blit(count, (INGAME_WIDTH_X - 120, 20))

pygame.init()

#Redraw screen
def draw():
    global n
    global posx
    global posy
    global INGAME_WIDTH_X
    global INGAME_HEIGHT_Y

    text = font.render(f'{n-1}', True, 'black')
    surface.fill((60,194,251))
    for i in range(1, n):
        surface.blit(egg, (posx[i] - 50, posy[i] - 50))
    surface.blit(chicken, (posx[n] - 100, posy[n] - 175))
    surface.blit(count, (INGAME_WIDTH_X - 120, 20))
    surface.blit(text, (INGAME_WIDTH_X - 95, 25))
    

#Watch for key input
def add_egg():
    global n
    global posx
    global posy
    global INGAME_WIDTH_X
    global INGAME_HEIGHT_Y

    n = n + 1
    INGAME_WIDTH_X, INGAME_HEIGHT_Y = pygame.display.get_surface().get_size()

    RANDOM_X = random.randint(50, INGAME_WIDTH_X - 50)
    RANDOM_Y = random.randint(50, INGAME_HEIGHT_Y - 50)
    posx.append(RANDOM_X)
    posy.append(RANDOM_Y)


def del_egg():
    global n
    global posx
    global posy
    global INGAME_WIDTH_X
    global INGAME_HEIGHT_Y

    n = n - 1
    posx.pop()
    posy.pop()


#Game body
def run_game():
    global n
    global posx
    global posy
    global INGAME_WIDTH_X
    global INGAME_HEIGHT_Y

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                file.write('Totle eggs: ' + str(n-1))
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_0:
                    file.write('Added egg' + str(n) + ': At x=' + str(posx[n]) + ' y=' + str(posy[n]) + '\n')
                    add_egg()
                    draw()
                
                if event.key == pygame.K_BACKSPACE and n >= 2:
                    file.write('Deleted egg' + str(n) + ': At x=' + str(posx[n]) + ' y=' + str(posy[n]) + '\n')
                    del_egg()
                    draw()
            elif event.type == VIDEORESIZE:
                INGAME_WIDTH_X, INGAME_HEIGHT_Y = pygame.display.get_surface().get_size()
                draw()

                

        pygame.display.flip()

run_game()

