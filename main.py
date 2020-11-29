import pygame
import shaders

from pygame.locals import *
from gl import *


delta_time = 0.0

pygame.init()
clock = pygame.time.Clock()
screenSize = (960, 540)
screen = pygame.display.set_mode(screenSize, DOUBLEBUF | OPENGL)

renderer = Renderer(screen)
renderer.camera_position.z = 10
renderer.point_light.z = 10
max_zoom_in = 10
max_zoom_out = 30

renderer.set_shaders(shaders.vertex_shader, shaders.fragment_shader)

renderer.model_lists.append(F1('models/formula1.obj', 'textures/formula1.bmp'))

def formula1():
    max_zoom_in = 10
    max_zoom_out = 200
    renderer.camera_position.x = 0
    renderer.camera_position.y = 5
    renderer.camera_position.z = 30 

    pygame.mixer.music.load('music/f1Theme.mp3')
    pygame.mixer.music.play(0)
    pygame.mixer.music.set_volume(0.5)

def topGun():
    max_zoom_in = 15
    max_zoom_out = 60
    renderer.camera_position.x = 0
    renderer.camera_position.y = 0
    renderer.camera_position.z = 20

    pygame.mixer.music.load('music/topGun.mp3')
    pygame.mixer.music.play(0)
    pygame.mixer.music.set_volume(0.5)

def halloween():
    max_zoom_in = 30
    max_zoom_out = 50
    renderer.camera_position.x = 0
    renderer.camera_position.y = 0
    renderer.camera_position.z = 20

    pygame.mixer.music.load('music/halloween.mp3')
    pygame.mixer.music.play(0)
    pygame.mixer.music.set_volume(0.5)


def reanult():
    max_zoom_in = 10
    max_zoom_out = 30
    renderer.camera_position.x = 0
    renderer.camera_position.y = 1
    renderer.camera_position.z = 15

    pygame.mixer.music.load('music/halo.mp3')
    pygame.mixer.music.play(0)
    pygame.mixer.music.set_volume(0.5)

pygame.mouse.set_pos(480, 270)
isPlaying = True
onMouse = False

formula1()

while isPlaying:
    mx, my = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    #   CAMERA TRANSLATION
    if keys[pygame.K_d]:
        renderer.camera_position.x += 10 * delta_time
    
    if keys[pygame.K_a]:
        renderer.camera_position.x -= 10 * delta_time
    
    if keys[pygame.K_w]:
        if renderer.camera_position.z <= max_zoom_in:
            renderer.camera_position.z = max_zoom_in
    
        else:
            renderer.camera_position.z -= 10 * delta_time

    if keys[pygame.K_s]:
        if renderer.camera_position.z >= max_zoom_out:
            renderer.camera_position.z = max_zoom_out
        
        else:
            renderer.camera_position.z += 10 * delta_time

    if keys[pygame.K_UP]:
        renderer.camera_position.y += 10 * delta_time
    
    if keys[pygame.K_DOWN]:
        renderer.camera_position.y -= 10 * delta_time

    #   CAMERA ROLL
    if keys[pygame.K_q]:
        renderer.camera_rotation.z -= 10 * delta_time

    if keys[pygame.K_e]:
        renderer.camera_rotation.z += 10 * delta_time

    #   CAMERA PITCH
    if keys[pygame.K_r]:
        renderer.camera_rotation.x += 10 * delta_time

    if keys[pygame.K_f]:
        renderer.camera_rotation.x -= 10 * delta_time

    #   CAMERA YAW
    if keys[pygame.K_x]:
        renderer.camera_rotation.y += 10 * delta_time

    if keys[pygame.K_z]:
        renderer.camera_rotation.y -= 10 * delta_time   

    if keys[pygame.K_1]:
        pygame.mixer.music.stop()
        renderer.model_lists.clear()
        formula1()
        renderer.model_lists.append(F1('models/formula1.obj', 'textures/formula1.bmp'))
    
    if keys[pygame.K_2]:
        pygame.mixer.music.stop()
        renderer.model_lists.clear()
        topGun()
        renderer.model_lists.append(Jet('models/jet.obj', 'textures/jet.bmp'))

    if keys[pygame.K_3]:
        pygame.mixer.music.stop()
        renderer.model_lists.clear()
        halloween()
        renderer.model_lists.append(Pumpkin('models/pumpkin.obj', 'textures/pumpkin.png'))

    if keys[pygame.K_4]:
        pygame.mixer.music.stop()
        renderer.model_lists.clear()
        reanult()
        renderer.model_lists.append(Renault('models/renault.obj', 'textures/renault.bmp'))

    if keys[pygame.K_y]:
        onMouse = True
    
    if keys[pygame.K_n]:
        onMouse = False


    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isPlaying = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_o:
                renderer.filled_mode()
            elif ev.key == pygame.K_p:
                renderer.wireframe_mode()
            elif ev.key == pygame.K_ESCAPE:
                isPlaying = False
    
    while onMouse:
        renderer.camera_rotation.y = mx * 0.4
        renderer.camera_rotation.x = my * 0.4

    renderer.render()

    pygame.display.flip()
    clock.tick(60)
    delta_time = clock.get_time() / 1000


pygame.quit()
