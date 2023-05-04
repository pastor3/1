import pygame
import random 

# ініціалізація Pygame 
pygame.init() 

# встановлюємо розмір поверхні
display_width = 800 
display_height = 600 

# встановлюємо розмір клітинок
cell_width = 40 
cell_height = 30# кольори
white = (255, 255, 255, 0) 
black = (0, 0, 0, 0) 

# створюємо поверхню гри 
game_display = pygame.display.set_mode((display_width, display_height)) 
pygame.display.set_caption('Гра з призами')

# завантажуємо фонове зображення
bg = pygame.image.load("phone1.jpg") 
game_display.blit(bg,(0,0))

# створюємо клас для призів 
class Prize:
    def __init__(self, x, y, speed, image): 
        self.x = x
        self.y = y 
        self.speed = speed
        self.image = image 

    def move(self): 
        self.x += self.speed[0]
        self.y += self.speed[1] 

        # змініть його напрямок руху 
        if self.x < 0 or self.x > display_width - 70 or self.y < 0 or self.y > display_height - 50:
            self.speed = (-self.speed[0]+2, -self.speed[1]+1) 

    def draw(self): 
        game_display.blit(self.image, (self.x, self.y))

# завантажуємо зображення призів
ljashch = pygame.image.load('prize1.png') 
ljashch1 = pygame.transform.scale(ljashch,(70,50)) 

korop = pygame.image.load('prize2.png')
korop1 = pygame.transform.scale(korop,(70,50)) 

karas = pygame.image.load('prize3.png')
karas1 = pygame.transform.scale(karas,(35,25)) 

jorsh = pygame.image.load('prize4.png')
jorsh1 = pygame.transform.scale(jorsh,(35,25)) 

plitka = pygame.image.load('prize5.png') 
plitka1 = pygame.transform.scale(plitka,(35,25)) 

# зображення призів
prize_images = [ljashch1,korop1,karas1,jorsh1,plitka1]

def prize_window(prize_info):
    # створення вікна
    prize_win = pygame.display.set_mode((400, 200))
    
    # створення кнопки
    restart_button = pygame.draw.rect(prize_win, (0, 0, 255), (50, 100, 300, 50))
    font = pygame.font.SysFont(None, 36)
    text = font.render("Restart", True, (255, 255, 255))
    prize_win.blit(text, (150, 110))
    
    # виведення повідомлення про приз
    message = font.render(prize_info, True, (0, 0, 0))
    prize_win.blit(message, (50, 50))
    
    # показ вікна 
    pygame.display.flip()
    
    # очікування дій користувача 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # перезапуск гри при натисканні на кнопку
                if restart_button.collidepoint(event.pos):
                    return True
    return False

# створюємо список призів
prizes = []
for i in range(30):
    prize_image = random.choice(prize_images)
    prize_x = random.randint(0, (display_width // cell_width) - 1) * cell_width
    prize_y = random.randint(0, (display_height // cell_height) - 1) * cell_height
    prize_speed = (random.randint(-5, 5), random.randint(-5, 5))
    prize = Prize(prize_x, prize_y, prize_speed, prize_image)
    prizes.append(prize)

# завантажуємо зображення поплавка
float_img = pygame.image.load('float.bmp')
popl = pygame.transform.scale(float_img,(4,28)) 

# координати поплавка 
float_cell = [0,-28]
def reset_game():
    # очищення вікна
    game_display.fill((255,255,255))
    
    # ініціалізація змінних
    ...
    
    # запуск головного циклу
    game_loop()

# цикл гри
game_exit = False 
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:                 
                # отримуємо координати кліку
                x, y = pygame.mouse.get_pos()
                                    
                    

                # змінюємо координати поплавка 
                cell_x = x // cell_width
                cell_y = y // cell_height 
                if cell_x != float_cell[0] or cell_y != float_cell[1]:
                    float_cell[0] = cell_x
                    float_cell[1] = cell_y

                    # перевіряємо, чи є приз в клітинці поплавка 
                    prize_rect = ljashch1.get_rect(topleft = (prize_x, prize_y))
                    popl_rect = popl.get_rect(topleft = ((float_cell[0] * cell_width)+20, float_cell[1] * cell_height))
                    if prize_rect.colliderect(popl_rect):
                        # додано виведення інформації про приз і очікування взаємодії користувача
                        prize_info = "Вітаємо: " + str(random.randint(1, 100)) + " грн!"
                        if prize_window(prize_info):
                            # якщо користувач натиснув "Restart", перезапускаємо гру
                            reset_game()
                        else:
                            # інакше, закриваємо гру
                            pygame.quit()
                            sys.exit()                    

    # рух призів 
    for prize in prizes:
        prize.move()

    # мережа клітинок
    for x in range(0, display_width, cell_width):
        for y in range(0, (display_height//2), cell_height):
            pygame.draw.rect(game_display, (100,100,100,0), (x, y, cell_width, cell_height), 0) 
            game_display.blit(bg,(0,0))

    # малюємо призи
    for prize in prizes:
        prize.draw()

    # малюємо поплавок 
    game_display.blit(popl, ((float_cell[0] * cell_width)+20, float_cell[1] * cell_height))

    pygame.display.update()

# завершення гри
pygame.quit()
quit()