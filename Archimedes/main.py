import pygame

pygame.init()

dims = [650, 650]
color = [(0, 0, 0), (255, 0, 0), (255, 255, 255)]
center = [dims[0]/2, dims[1]/2]
radius = [150, 7]
start = (center[0], center[1]-radius[0])
end = (center[0], center[1]+radius[0])
circlexy = [center[0], center[1]-radius[0]]
clock = pygame.time.Clock()


screen = pygame.display.set_mode(dims)
pygame.display.set_caption('Archimedes Illision')

def draw_line():
    pygame.draw.line(screen, color[0], start, end, 4)

def draw_smallcirlce():
    pygame.draw.circle(screen, color[2], circlexy, radius[1])

run, move = True, True
factor = 0
speed = 0.1

while run:
    screen.fill(color[0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #moving the small circle
    if circlexy[1] >= start[1] and move == True:
        circlexy[1] += 1
        if circlexy[1] > end[1]:
            move = False
    if circlexy[1] >= end[1] or move == False:
        circlexy[1] -= 1
        if circlexy[1] <= start[1]:
            move = True

    pygame.draw.circle(screen, color[1], center, radius[0])
    draw_line()
    draw_smallcirlce()
    clock.tick(100)
    pygame.display.update()

pygame.quit()