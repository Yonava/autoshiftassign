import pygame
import os

pygame.init()

WIDTH, HEIGHT = 960, 540
window = (WIDTH, HEIGHT)


# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
GRAY = (125, 125, 125)
DARK_RED = (100, 0, 0)
LIGHT_GRAY = (210, 210, 210)
YELLOW = (244, 232, 104)
DARK_BLUE = (0, 0, 150)

logo = pygame.image.load(os.path.join('caneslove', 'logo.png'))
logo = pygame.transform.scale(logo, (int((logo.get_width()/4)), int((logo.get_height()/4))))
pygame.image.load(os.path.join('caneslove', 'schedule.jpg'))

github_url = 'github.com/yonava'
FPS = 60
clock = pygame.time.Clock()
WIN = pygame.display.set_mode(window)
pygame.display.set_caption('Raising Canes Shift Assign (c714)')
pygame.display.set_icon(logo)
schedule = pygame.transform.scale(pygame.image.load(os.path.join('caneslove', 'schedule.jpg')), window)
base_font = pygame.font.SysFont('Gadugi Bold', 40)
big_font = pygame.font.SysFont('Gadugi Bold', 120)
fineprint_font = pygame.font.SysFont('Arial', 20)

crew_text = ''
crew_rating_int = ''
am_pm = ''

# main_menu buttons
build_schedule_button = base_font.render('Generate New Schedule', False, ORANGE)
add_crew_button = base_font.render('Add Crew', False, GREEN)
del_crew_button = base_font.render('Remove Crew', False, RED)
build_version = fineprint_font.render('asa release v1.0: by Yona V-A (yonava.com/github)', False, BLACK)

# build_sheet buttons
am_button = big_font.render('AM', False, YELLOW)
pm_button = big_font.render('PM', False, BLUE)
joyce_button = base_font.render('Joyce', False, BLACK)
aidee_button = base_font.render('Aidee', False, BLACK)
isiah_button = base_font.render('Isiah', False, BLACK)
ismael_button = base_font.render('Ismael', False, BLACK)
continue_button = base_font.render('Continue', False, GREEN)

# generate_schedule buttons
exit_button = base_font.render('Return To Main Menu', False, BLACK)

# main_menu sprites
build_button_hitbox = pygame.Rect(((WIDTH/2)-(build_schedule_button.get_width()/2)), (HEIGHT/2-30), (build_schedule_button.get_width()), (build_schedule_button.get_height()))
add_crew_hitbox = pygame.Rect(((WIDTH/2)-(add_crew_button.get_width()/2)), (HEIGHT/2+30), (add_crew_button.get_width()), (add_crew_button.get_height()))
del_crew_hitbox = pygame.Rect(((WIDTH/2)-(del_crew_button.get_width()/2)), (HEIGHT/2+60), (del_crew_button.get_width()), (del_crew_button.get_height()))
version_hitbox = pygame.Rect(((WIDTH/2)-(build_version.get_width()/2)), (HEIGHT-30), (build_version.get_width()), (build_version.get_height()))

# build_sheet sprites
am_hitbox = pygame.Rect((0, 0, (WIDTH/2), HEIGHT))
pm_hitbox = pygame.Rect(((WIDTH/2), 0, (WIDTH/2), HEIGHT))
joyce_hitbox = pygame.Rect(((75)-(joyce_button.get_width()/2)), (HEIGHT/2), (joyce_button.get_width()), (joyce_button.get_height()))
aidee_hitbox = pygame.Rect(((WIDTH*.25+75)-(aidee_button.get_width()/2)), (HEIGHT/2), (aidee_button.get_width()), (aidee_button.get_height()))
isiah_hitbox = pygame.Rect(((WIDTH*.5+75)-(isiah_button.get_width()/2)), (HEIGHT/2), (isiah_button.get_width()), (isiah_button.get_height()))
ismael_hitbox = pygame.Rect(((WIDTH*.75+75)-(ismael_button.get_width()/2)), (HEIGHT/2), (ismael_button.get_width()), (ismael_button.get_height()))
continue_hitbox = pygame.Rect(((WIDTH/2)-(continue_button.get_width()/2)), (HEIGHT-50), (continue_button.get_width()), (continue_button.get_height()))

# generate_schedule sprites
exit_hitbox = pygame.Rect(((WIDTH/2)-(exit_button.get_width()/2)), (HEIGHT-30), (exit_button.get_width()), (exit_button.get_height()))

def build_sheet():

    requirement_am_pm = True
    tick_delay = 0

    while requirement_am_pm:
        
        tick_delay += 1
        
        global am_pm
        clock.tick(FPS)
        WIN.fill(DARK_BLUE)
        pygame.draw.rect(WIN, YELLOW, ((WIDTH/2), 0, (WIDTH/2), HEIGHT))

        if am_hitbox.collidepoint(pygame.mouse.get_pos()) and tick_delay > 10:
            pygame.draw.rect(WIN, BLACK, am_hitbox)
            if pygame.mouse.get_pressed()[0]:
                am_pm = 'AM'
                requirement_am_pm = False
        WIN.blit(am_button, (((WIDTH/4)-(am_button.get_width()/2)),((HEIGHT/2)-(am_button.get_height()/2))))
        
        if pm_hitbox.collidepoint(pygame.mouse.get_pos()) and tick_delay > 10:
            pygame.draw.rect(WIN, BLACK, pm_hitbox)
            if pygame.mouse.get_pressed()[0]:
                am_pm = 'PM'
                requirement_am_pm = False
        WIN.blit(pm_button, (((WIDTH*.75)-(pm_button.get_width()/2)),((HEIGHT/2)-(pm_button.get_height()/2))))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.update()
    
    build_sheet2()
    


def build_sheet2():
    
    requirement_mod = True
    tick_delay = 0
    tick_delay1 = -120
    
    joyce_score = 0
    aidee_score = 0
    isiah_score = 0
    ismael_score = 0

    while requirement_mod:
    
        tick_delay += 1
        tick_delay1 += 1
        WIN.fill(WHITE)
        clock.tick(FPS)

        
        pygame.draw.rect(WIN, BLUE, (200, tick_delay-50, 100, tick_delay*2))
        pygame.draw.rect(WIN, (85, 200, 255), (tick_delay1, tick_delay1*.5, 300, 200))
        pygame.draw.rect(WIN, (100, 100, 255), (tick_delay, 150, 300, 200))
        if tick_delay > 1000:
            tick_delay = 0
            tick_delay1 = -120


        if joyce_hitbox.collidepoint(pygame.mouse.get_pos()) and tick_delay > 10:
            pygame.draw.rect(WIN, GRAY, joyce_hitbox)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                joyce_score += 1
        WIN.blit(joyce_button, (((75)-(joyce_button.get_width()/2)),(HEIGHT/2)))

        if aidee_hitbox.collidepoint(pygame.mouse.get_pos()) and tick_delay > 10:
            pygame.draw.rect(WIN, GRAY, aidee_hitbox)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                aidee_score += 1
        WIN.blit(aidee_button, (((WIDTH*.25+75)-(aidee_button.get_width()/2)),(HEIGHT/2)))

        if isiah_hitbox.collidepoint(pygame.mouse.get_pos()) and tick_delay > 10:
            pygame.draw.rect(WIN, GRAY, isiah_hitbox)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                isiah_score += 1
        WIN.blit(isiah_button, (((WIDTH*.5+75)-(isiah_button.get_width()/2)),(HEIGHT/2)))

        if ismael_hitbox.collidepoint(pygame.mouse.get_pos()) and tick_delay > 10:
            pygame.draw.rect(WIN, GRAY, ismael_hitbox)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                ismael_score += 1
        WIN.blit(ismael_button, (((WIDTH*.75+75)-(ismael_button.get_width()/2)),(HEIGHT/2)))

        if joyce_score % 2 == 1:
            pygame.draw.rect(WIN, GRAY, joyce_hitbox)
            WIN.blit(joyce_button, (((75)-(joyce_button.get_width()/2)),(HEIGHT/2)))
            joyce_on_shift = 'Joyce'
        else: joyce_on_shift = ''

        if aidee_score % 2 == 1:
            pygame.draw.rect(WIN, GRAY, aidee_hitbox)
            WIN.blit(aidee_button, (((WIDTH*.25+75)-(aidee_button.get_width()/2)),(HEIGHT/2)))
            aidee_on_shift = 'Aidee'
        else: aidee_on_shift = ''

        if isiah_score % 2 == 1:
            pygame.draw.rect(WIN, GRAY, isiah_hitbox)
            WIN.blit(isiah_button, (((WIDTH*.5+75)-(isiah_button.get_width()/2)),(HEIGHT/2)))
            isiah_on_shift = 'Isiah'
        else: isiah_on_shift = ''

        if ismael_score % 2 == 1:
            pygame.draw.rect(WIN, GRAY, ismael_hitbox)
            WIN.blit(ismael_button, (((WIDTH*.75+75)-(ismael_button.get_width()/2)),(HEIGHT/2)))
            ismael_on_shift = 'Ismael'
        else: ismael_on_shift = ''

        if continue_hitbox.collidepoint(pygame.mouse.get_pos()) and tick_delay > 10:
            pygame.draw.rect(WIN, GRAY, continue_hitbox)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(250)
                mods = base_font.render(f"{joyce_on_shift} {aidee_on_shift} {isiah_on_shift} {ismael_on_shift}", False, BLACK)
                generate_schedule(mods)
        WIN.blit(continue_button, (((WIDTH/2)-(continue_button.get_width()/2)),(HEIGHT-50)))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        WIN.blit(big_font.render('Select MODs', False, BLACK),((75)-(joyce_button.get_width()/2),(HEIGHT/2-100)))
        pygame.display.update()


def generate_schedule(mods):
    
    generate = True
    while generate:
    
        WIN.blit(schedule, (0, 0))
        
        am_pm_render = base_font.render(am_pm, False, BLACK)
        WIN.blit(am_pm_render, (360, 63))
        WIN.blit(mods, (530, 65))
        
        if exit_hitbox.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, exit_hitbox)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(100)
                generate = False
        WIN.blit(exit_button, (((WIDTH/2)-(exit_button.get_width()/2)),(HEIGHT-30)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()
   
    main_menu()

def main_menu():
    
    tick_delay = 0
    tick_delay1 = 0
    running = True
    while running:
        
        # basic main_menu config
       
        tick_delay += 1
        WIN.fill(WHITE)
        pygame.draw.rect(WIN, DARK_RED, (tick_delay, tick_delay, tick_delay/2, tick_delay))
        pygame.draw.rect(WIN, (60, 0, 0), (800 -tick_delay, 800 -tick_delay, 800 -tick_delay, 800-tick_delay))
        pygame.draw.rect(WIN, (140, 0, 0), (tick_delay, 0, tick_delay, 300))
        pygame.draw.rect(WIN, DARK_RED, (0, tick_delay1, tick_delay1/2, tick_delay1))
        pygame.draw.rect(WIN, (60, 0, 0), (800 -tick_delay1, 800 +tick_delay1, tick_delay1*2, tick_delay1))
        pygame.draw.rect(WIN, (140, 0, 0), (tick_delay1, 0, tick_delay1, 300))
        if tick_delay > 1000:
            tick_delay = 0
        if tick_delay1 > 1300:
            tick_delay1 = 0 
        if tick_delay > 300:
            tick_delay1 += 1

        pygame.draw.rect(WIN, LIGHT_GRAY, ((WIDTH/2-170), 30, 340, 400),15)
        clock.tick(FPS)
        WIN.blit(logo, (((WIDTH/2)-(logo.get_width()/2)),(50)))

        # mouse hover / click detection

        if build_button_hitbox.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, build_button_hitbox)
            if pygame.mouse.get_pressed()[0]:
                build_sheet()
        WIN.blit(build_schedule_button, (((WIDTH/2)-(build_schedule_button.get_width()/2)),(HEIGHT/2-30)))
        
        if add_crew_hitbox.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, add_crew_hitbox)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(100)
                print('ok')
        WIN.blit(add_crew_button, (((WIDTH/2)-(add_crew_button.get_width()/2)),(HEIGHT/2+30)))

        if del_crew_hitbox.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, del_crew_hitbox)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(100)
                print('ok')
        WIN.blit(del_crew_button, (((WIDTH/2)-(del_crew_button.get_width()/2)),(HEIGHT/2+60)))

        if version_hitbox.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(WIN, GRAY, version_hitbox)
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(100)
                print(github_url)
        WIN.blit(build_version, (((WIDTH/2)-(build_version.get_width()/2)),(HEIGHT-30)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
    pygame.display.update()

if __name__ == "__main__":
    main_menu()