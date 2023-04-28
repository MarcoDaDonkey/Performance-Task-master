#importing necessary modules
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from sys import exit
import random
import time

#defining important varliables
x = 1200
y = 800
user_text = ''

#initializing pygame and creating window with a title
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption('Dino Collector Performance Task')

#creating different sized fonts
font = pygame.font.Font('freesansbold.ttf', 100)
smaller_font = pygame.font.Font('freesansbold.ttf', 40)
slightly_smaller_font = pygame.font.Font('freesansbold.ttf', 50)
a_lot_smaller_font = pygame.font.Font('freesansbold.ttf', 25)

#defining text that will show in the game
title_text = font.render('Dino Collector', True, (255, 255, 255))
title_text_rect = title_text.get_rect()
title_text_rect.center = (x // 2, 200)

start_text = smaller_font.render('Press Space to Start', True, (255, 255, 255))
start_text_rect = start_text.get_rect()
start_text_rect.center = (x // 2, 500)

dino_egg = pygame.transform.scale(pygame.image.load('dinosaur_egg.png'), (380, 400)).convert()
dino_egg_rect = dino_egg.get_rect()
dino_egg_rect.center = (x // 2, 360)

water_dino_egg = pygame.transform.scale(pygame.image.load('water_dinosaur_egg.png'), (420, 400)).convert()
water_dino_egg_rect = water_dino_egg.get_rect()
water_dino_egg_rect.center = (1000, 360)

air_dino_egg = pygame.transform.scale(pygame.image.load('air_dino_egg.png'), (420, 400)).convert()
air_dino_egg_rect = air_dino_egg.get_rect()
air_dino_egg_rect.center = (200, 360)

my_dino_text = slightly_smaller_font.render('View Dinos', True, (255, 255, 255))
my_dino_text_rect = my_dino_text.get_rect()
my_dino_text_rect.center = (x // 2, 700)

back_text = slightly_smaller_font.render('Back', True, (255, 255, 255))
back_text_rect = back_text.get_rect()
back_text_rect.center = (x // 2, 600)

land_text = slightly_smaller_font.render('Land Egg', True, (255, 255, 255))
land_text_rect = land_text.get_rect()
land_text_rect.center = (x // 2, 600)

water_text = slightly_smaller_font.render('Water Egg', True, (255, 255, 255))
water_text_rect = water_text.get_rect()
water_text_rect.center = (1000, 600)

air_text = slightly_smaller_font.render('Air Egg', True, (255, 255, 255))
air_text_rect = air_text.get_rect()
air_text_rect.center = (200, 600)

#locating mouse position at all times
mouse = pygame.mouse.get_pos()

#dino dictionary that contains information
dino_dictionary = {
'Allosaurus': ['8.5 m tall and 9.7 m long', '4,400 Ibs', 'Diet: Meat', 'Group: Therapod', 'Period: Late Jurassic'],
'Ankylosaurus' : ['5.4m tall and 8.5m long', '17500 Ibs', 'Diet: PLants', 'Group: Thyreophora', 'Period: Late Cretaceous'],
'Archaeopteryx' : [],
'Argentinosaurus' : [],
'Baryonyx': [],
'Brachiosaurus': [],
'Carnotaurus': [],
'Compsognathus': [],
'Dilophosaurus': [],
'Diplodocus': [],
'Eoraptor': [],
'Gallimimus': [],
'Giganotosaurus': [],
'Gobisaurus': [],
'Iguanodon': [],
'Maiasaura': [],
'Megalosaurus': [],
'Microraptor': [],
'Oviraptor': [],
'Pachycephalosaurus': [],
'Parasaurolophus': [],
'Sarcosuchus': [],
'Spinosaurus': [],
'Stegosaurus': [],
'Styracosaurus': [],
'Supersaurus': [],
'Therizinosaurus': [], 
'Triceratops': [],
'Troodon': [],
'Tyrannosaurus Rex': [],
'Utahraptor': [],
'Velociraptor': [],
'Dimorphodon': [],
'Pteranodon': [],
'Pterodactylus': [],
'Quetzalcoatlus': [],
'Dunkleosteus': [],
'Elasmosaurus': [],
'Helicoprion': [], 
'Ichthyosaurus': [],
'Megalodon': [], 
'Mosasaurus': [],
'Plesiosaurus': []
  }

#dino list for random selection
dino_list = ['Allosaurus', 'Ankylosaurus', 'Archaeopteryx', 'Argentinosaurus', 'Baryonyx',
'Brachiosaurus', 'Carnotaurus', 'Compsognathus', 'Dilophosaurus', 'Diplodocus',
'Eoraptor', 'Gallimimus', 'Giganotosaurus', 'Gobisaurus', 
'Iguanodon', 'Maiasaura', 'Megalosaurus', 'Microraptor',
'Oviraptor', 'Pachycephalosaurus', 'Parasaurolophus',
'Sarcosuchus', 'Spinosaurus', 'Stegosaurus', 'Styracosaurus', 'Supersaurus',
'Therizinosaurus', 'Triceratops', 'Troodon', 'Tyrannosaurus Rex', 'Utahraptor', 'Velociraptor',
'Dimorphodon', 'Pteranodon', 'Pterodactylus', 'Quetzalcoatlus',
'Dunkleosteus', 'Elasmosaurus', 'Helicoprion', 'Ichthyosaurus', 'Megalodon', 'Mosasaurus', 'Plesiosaurus']

#defining player dino list
player_dinos = []

#defining initial game state
game_state = 'title'

#defining time that is necessary for some text to linger
last_hatch_time = 0
hatch_text_duration = 5
player_dino_time = 0
player_dino_duration = 5
number_of_eggs = 0

#function that hatches the dinos
def hatch_dino(current_dino):
  global number_of_eggs
  global last_hatch_time
  global newDino
  if number_of_eggs <= 8:
    hatch_text = smaller_font.render('You hatched a '+ dino_list[current_dino], True, (255, 255, 255))
    hatch_text_rect = hatch_text.get_rect()
    hatch_text_rect.center = (x // 2, 60)
    screen.blit(hatch_text, hatch_text_rect)
    newDino = dino_list[current_dino]
    number_of_eggs += 1
    
    if len(player_dinos) < 9:
      player_dinos.append(newDino)
      last_hatch_time = time.time()
    return newDino and number_of_eggs


#event loop
while True:
  for event in pygame.event.get():
    #closes out of the window and ends program when the x is pressed
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    #screen that shows the egg to hatch dinos
    if game_state == 'hatch_screen':
      screen.fill((0, 0, 0))
      
      screen.blit(dino_egg, dino_egg_rect)
      screen.blit(water_dino_egg, water_dino_egg_rect)
      screen.blit(air_dino_egg, air_dino_egg_rect)

      screen.blit(land_text, land_text_rect)
      screen.blit(water_text, water_text_rect)
      screen.blit(air_text, air_text_rect)

      my_dino_button = pygame.draw.rect(screen, (0, 200, 100), pygame.Rect(x // 2 - 150, 650, 300, 100))
      screen.blit(my_dino_text, my_dino_text_rect)
      
      #creating a button that activates with user input
      if event.type == pygame.MOUSEBUTTONDOWN:
        if dino_egg_rect.collidepoint(event.pos): 
          hatch_dino(random.randint(0, 31))
        elif my_dino_button.collidepoint(event.pos):
          game_state = 'view_dino_screen'
        elif water_dino_egg_rect.collidepoint(event.pos):
          hatch_dino(random.randint(36, 42))
        elif air_dino_egg_rect.collidepoint(event.pos):
          hatch_dino(random.randint(32, 35))
      
      #allows text to linger on screen for more than a frame
      if time.time() - last_hatch_time < hatch_text_duration:
        hatch_text = smaller_font.render('You hatched a '+ newDino, True, (255, 255, 255))
        hatch_text_rect = hatch_text.get_rect()
        hatch_text_rect.center = (x // 2, 60)
        screen.blit(hatch_text, hatch_text_rect)
    
    #initial screen that moves to "hatch screen" when space button is pressed
    if game_state == 'title': 
      screen.fill((0, 200, 100))
      screen.blit(title_text, title_text_rect)
      screen.blit(start_text, start_text_rect)
      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        game_state = 'hatch_screen'
    
    #screen that shows all your dinos that you have hatched
    if game_state == 'view_dino_screen':
      screen.fill((0, 0, 0))
      
      if number_of_eggs > 0:
        back_text_button = pygame.draw.rect(screen, (0, 200, 100), pygame.Rect(x // 2 - 150, 550, 300, 100))
        screen.blit(back_text, back_text_rect)

      for dino_print in range(len(player_dinos)):
        player_dinos_text = smaller_font.render(player_dinos[dino_print], True, (255, 255, 255))
        player_dinos_text_rect = player_dinos_text.get_rect()
        player_dinos_text_rect.center = (x // 2, 100 + 50 * dino_print)
        screen.blit(player_dinos_text, player_dinos_text_rect)
      if event.type == pygame.MOUSEBUTTONDOWN:
        if back_text_rect.collidepoint(event.pos):
          game_state = 'hatch_screen'

      if number_of_eggs == 0:
        no_dino_text = smaller_font.render('Please hatch a dino.', True, (255, 255, 255))
        no_dino_text_rect = no_dino_text.get_rect()
        no_dino_text_rect.center = (x // 2, 110)
        screen.blit(no_dino_text, no_dino_text_rect)
      
      input_rect = pygame.Rect(-150 + x // 2, 25, 300, 40)
      pygame.draw.rect(screen, (0, 200, 100), input_rect)
      text_surface = a_lot_smaller_font.render(user_text, True, (255, 255, 255))
      screen.blit(text_surface, input_rect)

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
          user_text = user_text[:-1]
        elif event.key == pygame.K_RETURN:
          game_state = 'dino_stats'
        else:
          user_text += event.unicode

    if game_state == 'hatch_screen':
      if len(player_dinos) == 9:
        limit_text = smaller_font.render("You have reached the maximum limit of dinos!", True, (255, 255, 255))
        limit_text_rect = limit_text.get_rect()
        limit_text_rect.center = (x // 2, 110)
        screen.blit(limit_text, limit_text_rect)
    
    if game_state == 'dino_stats':
      screen.fill((0, 0, 0))
      
      if user_text in dino_dictionary and user_text in player_dinos:
        current_dino_stats_text = font.render(user_text, True, (255, 255, 255))
        current_dino_stats_text_rect = current_dino_stats_text.get_rect()
        current_dino_stats_text_rect.center = (x // 2, 100)
        screen.blit(current_dino_stats_text, current_dino_stats_text_rect)
        
        dino_size = smaller_font.render(dino_dictionary[user_text][0], True, (255, 255, 255))
        dino_size_rect = dino_size.get_rect()
        dino_size_rect.center = (x // 2, 300)
        screen.blit(dino_size, dino_size_rect)

        dino_weight = smaller_font.render(dino_dictionary[user_text][1], True, (255, 255, 255))
        dino_weight_rect = dino_weight.get_rect()
        dino_weight_rect.center = (x // 2, 400)
        screen.blit(dino_weight, dino_weight_rect)

        dino_diet = smaller_font.render(dino_dictionary[user_text][2], True, (255, 255, 255))
        dino_diet_rect = dino_diet.get_rect()
        dino_diet_rect.center = (x // 2, 500)
        screen.blit(dino_diet, dino_diet_rect)
        
        dino_group = smaller_font.render(dino_dictionary[user_text][3], True, (255, 255, 255))
        dino_group_rect = dino_group.get_rect()
        dino_group_rect.center = (x // 2, 600)
        screen.blit(dino_group, dino_group_rect)
        
        dino_period = smaller_font.render(dino_dictionary[user_text][3], True, (255, 255, 255))
        dino_period_rect = dino_period.get_rect()
        dino_period_rect.center = (x // 2, 700)
        screen.blit(dino_period, dino_period_rect)
      else:
        game_state = 'dino_stats'
        print("You did not enter a dino you have or a dino that exits. Reopen the game and try again.")
        exit()

    pygame.display.update()
    clock.tick(60)