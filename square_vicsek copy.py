from ast import If
from re import I
import pygame
from pygame.locals import *
from random import randint

def get_points(n_points, widith, height):
    pts = []
    center = widith//2, height//2
    for x in range(widith):
        for y in range(height):
            if int(((x-center[0])**2+(y-center[1])**2)**0.5) == 250:
                pts.append((x, y))
    return pts

def chaos(pts, ac_pos):
    selected_pt = randint(0, len(pts)-1)
    new_ac_pos = ac_pos[0] - 2*(ac_pos[0] - pts[selected_pt][0])//3, ac_pos[1] - 2*(ac_pos[1] - pts[selected_pt][1])//3
    return new_ac_pos


pygame.init()

widith, height = 600, 600
screen = pygame.display.set_mode((widith, height))

pts = get_points(3, widith, height)
# pts = (50, 50), (widith-50, 50), (50, height-50), (widith-50, height-50), (widith//2, height//2) 
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

    actual_pos =chaos(pts, actual_pos)    
    chaos_pts.append(actual_pos)

    pygame.display.update()