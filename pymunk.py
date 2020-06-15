import pymunk
from pymunk import Vec2d
import pymunk.pygame_util

surf = pygame.Surface((600, 600))
draw_options1 = pymunk.pygame_util.DrawOptions(surf) 

# Setup the base Pymunk Space.
space1 = pymunk.Space()  
space1.gravity = 0,-1000
space1.sleep_time_threshold = 0.5

template_box = pymunk.Poly.create_box(pymunk.Body(), (20,20))
template_box.mass = 1
template_box.friction = 1

for x in range(1):
    for y in range(1):
        box = template_box.copy()
        box.body.position = 200+x*30, 10+y*20
        space1.add(box, box.body)
        print('teste')
