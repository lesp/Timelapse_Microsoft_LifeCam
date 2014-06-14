import pygame.camera
import pygame.image
import time
import datetime




def pic():
    while True:
        a = str(datetime.datetime.now())
        a = a[0:19]
        pygame.camera.init()
        cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
        cam.start()
        img = cam.get_image()
        pygame.image.save(img, (a)+".bmp")
        time.sleep(10)
        cam.stop()
        pygame.camera.quit()
