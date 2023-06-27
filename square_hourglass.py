import pygame
from pygame.locals import *
from random import randint

def get_points(n_points, widith, height):
    points = [[randint(0, widith), randint(0, height)] for _ in range(n_points)]
    return points

def chaos(pts, ac_pos, prev_pt):
    selected_pt = randint(0, len(pts)-1)
    while selected_pt - prev_pt in (2, -2):
        selected_pt = randint(0, len(pts)-1)

    new_ac_pos = ac_pos[0] - (ac_pos[0] - pts[selected_pt][0])//2, ac_pos[1] - (ac_pos[1] - pts[selected_pt][1])//2
    return new_ac_pos, selected_pt


pygame.init()

widith, height = 600, 600
screen = pygame.display.set_mode((widith, height))

# pts = get_points(4, widith, height)
pts = (50, 50), (widith-50, 50), (50, height-50), (widith-50, height-50)

prev_pt = -1
actual_pos = [randint(0, widith), randint(0, height)]
chaos_pts = [actual_pos]

fps = 5
clock = pygame.time.Clock()
while True:
    clock.tick(fps)
    screen.fill('BLACK')

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                fps += 5
            if event.key == K_DOWN:
                fps -= 5
        if event.type == pygame.QUIT:
            pygame.quit()

    for pt in pts:
        pygame.draw.circle(screen, (255, 255, 255), pt, 3)
    
    for pt in chaos_pts:
        pygame.draw.rect(screen, (255, 255, 0), (pt, (1,1)))

    actual_pos, prev_pt = chaos(pts, actual_pos, prev_pt)    
    chaos_pts.append(actual_pos)

    pygame.display.update()