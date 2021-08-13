import pygame
import os

pygame.init()

logo = pygame.image.load(os.path.join('caneslove', 'logo.png'))
schedule_raw = pygame.image.load(os.path.join('caneslove', 'schedule.jpg'))

WIDTH, HEIGHT = 960, 540
window = (WIDTH, HEIGHT)
win = pygame.display.set_mode(window)
pygame.display.set_caption('Raising Canes Shift Assign (c714)')
pygame.display.set_icon(logo)
schedule = pygame.transform.scale(schedule_raw, window)
base_font = pygame.font.SysFont('Arial', 20)
mod_text = ''
crew_text = ''
crew_rating_int = ''

def main_menu():
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # TODO: if pygame.mouse.get_pressed()[0] and 
        
    



        pygame.display.update()
    pygame.quit





if __name__ == "__main__":
    main_menu()