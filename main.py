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
'Allosaurus': ['12 m long', '2,000 kg', 'Diet: Meat', 'Group: Theropoda', 'Period: Late Jurassic'],
'Ankylosaurus': ['7 m long', '4,000 kg', 'Diet: Plants', 'Group: Ankylosauria', 'Period: Late Cretaceous'],
'Archaeopteryx' : ['0.5 m long', '0.5 - 1 kg', 'Diet: Meat', 'Group: Avialae', 'Period: Late Jurassic'],
'Argentinosaurus' : ['35 m long', '70,000 kg', 'Diet: Plants', 'Group: Titanosauria', 'Period: Late Cretaceous'],
'Baryonyx': ['10 m long', '2,000 kg', 'Diet: Meat/Fish', 'Group: Theropoda', 'Period: Early Cretaceous'],
'Brachiosaurus': ['30m long', '40,000 kg', 'Diet: Plants', 'Group: Sauropoda', 'Period: Late Jurassic'],
'Carnotaurus': ['7.6 m long', '1,350 kg', 'Diet: Meat', 'Group: Abelisauridae', 'Period: Late Cretaceous'],
'Compsognathus': ['0.6 m tall and 1 m long', '7 lbs', 'Diet: Meat', 'Group: Theropoda', 'Period: Late Jurassic'],
'Dilophosaurus': ['1.5 m tall and 7 m long', '880 lbs', 'Diet: Meat', 'Group: Theropoda', 'Period: Early Jurassic'],
'Diplodocus': ['6.5 m tall and 27 m long', '88,000 lbs', 'Diet: Plants', 'Group: Sauropoda', 'Period: Late Jurassic'],
'Eoraptor': ['1 m tall and 1.5 m long', '22 lbs', 'Diet: Meat/Plants', 'Group: Theropoda', 'Period: Late Triassic'],
'Gallimimus': ['3 m tall and 6 m long', '1,100 lbs', 'Diet: Omnivore', 'Group: Ornithomimidae', 'Period: Late Cretaceous'],
'Giganotosaurus': ['4.5 m tall and 13 m long', '8,800 lbs', 'Diet: Meat', 'Group: Theropoda', 'Period: Early Cretaceous'],
'Gobisaurus': ['3 m tall and 6 m long', '2,200 lbs', 'Diet: Plants', 'Group: Ankylosauria', 'Period: Late Cretaceous'],
'Iguanodon': ['4 m tall and 10 m long', '9,900 lbs', 'Diet: Plants', 'Group: Ornithopoda', 'Period: Early Cretaceous'],
'Maiasaura': ['3 m tall and 9 m long', '3,500 lbs', 'Diet: Plants', 'Group: Hadrosauridae', 'Period: Late Cretaceous'],
'Megalosaurus': ['3 m tall and 9 m long', '1,540 lbs', 'Diet: Meat', 'Group: Theropoda', 'Period: Middle Jurassic'],
'Microraptor': ['0.4 m tall and 1.2 m long', '4.4 lbs', 'Diet: Meat', 'Group: Dromaeosauridae', 'Period: Early Cretaceous'],
'Oviraptor': ['1 m tall and 2 m long', '55 lbs', 'Diet: Omnivore', 'Group: Oviraptorosauria', 'Period: Late Cretaceous'],
'Parasaurolophus': ['4 m tall and 10 m long', '2,200 lbs', 'Diet: Plants', 'Group: Hadrosauridae', 'Period: Late Cretaceous'],
'Sarcosuchus': ['3.5 m tall and 11-12 m long', '8,800 lbs', 'Diet: Meat', 'Group: Crocodylomorpha', 'Period: Early Cretaceous'],
'Spinosaurus': ['4 m tall and 15-18 m long', '22,000 lbs', 'Diet: Fish', 'Group: Theropoda', 'Period: Early Cretaceous'],
'Stegosaurus': ['4 m tall and 9 m long', '5,500 lbs', 'Diet: Plants', 'Group: Ornithischia', 'Period: Late Jurassic'],
'Styracosaurus': ['2.5 m tall and 5.5 m long', '2,200 lbs', 'Diet: Plants', 'Group: Ceratopsia', 'Period: Late Cretaceous'],
'Supersaurus': ['12-16 m tall and 33-34 m long', '110,000 lbs', 'Diet: Plants', 'Group: Sauropoda', 'Period: Late Jurassic'],
'Therizinosaurus': ['5 m tall and 10 m long', '11,000 lbs', 'Diet: Plants', 'Group: Therizinosauria', 'Period: Late Cretaceous'],
'Triceratops': ['3 m tall and 9 m long', '12,000 lbs', 'Diet: Plants', 'Group: Ceratopsia', 'Period: Late Cretaceous'],
'Troodon': ['2.5 m tall and 3 m long', '110 lbs', 'Diet: Meat', 'Group: Theropoda', 'Period: Late Cretaceous'],
'Tyrannosaurus Rex': ['6 m tall and 12.3-12.8 m long', '15,500 lbs', 'Diet: Meat', 'Group: Theropoda', 'Period: Late Cretaceous'],
'Utahraptor': ['2 m tall and 6-7 m long', '1,100 lbs', 'Diet: Meat', 'Group: Dromaeosauridae', 'Period: Early Cretaceous'],
'Velociraptor': ['0.5-0.7 m tall and 1.8-2 m long', '33-73 lbs', 'Diet: Meat', 'Group: Dromaeosauridae', 'Period: Late Cretaceous'],
'Dimorphodon': ['1 m tall and 2.5 m long', '6.6 lbs', 'Diet: Fish/Insectivore', 'Group: Pterosauria', 'Period: Early Jurassic'],
'Pteranodon': ['6 m tall and 10-12 m long', '44-99 lbs', 'Diet: Fish', 'Group: Pterosauria', 'Period: Late Cretaceous'],
'Pterodactylus': ['0.8 m tall and 1.2-1.5 m long', '550 lbs', 'Diet: Meat', 'Group: Pterosauria', 'Period: Late Jurassic'],
'Quetzalcoatlus': ['15 m tall and 10-11 m long', '550 lbs', 'Diet: Meat/Fish', 'Group: Pterosauria', 'Period: Late Cretaceous'],
'Dunkleosteus': ['1.3 m tall and 6 m long', '990 lbs', 'Diet: Meat', 'Group: Placodermi', 'Period: Late Devonian'],
'Elasmosaurus': ['1.8 m tall and 14 m long', '2,200 lbs', 'Diet: Fish', 'Group: Plesiosauria', 'Period: Late Cretaceous'],
'Helicoprion': ['1 m tall and 3.5 m long', '1,100 lbs', 'Diet: Meat', 'Group: Chondrichthyes', 'Period: Early Permian'],
'Ichthyosaurus': ['1.2-1.5 m tall and 2-4 m long', '220-440 lbs', 'Diet: Fish', 'Group: Ichthyosauria', 'Period: Early Jurassic'],
'Megalodon': ['2.5-3 m tall and 16-18 m long', '88,000 lbs', 'Diet: Meat', 'Group: Lamniformes', 'Period: Miocene'],
'Mosasaurus': ['15-18 m tall and 12-14 m long', '44,000 lbs', 'Diet: Meat/Fish', 'Group: Mosasauridae', 'Period: Late Cretaceous'],
'Plesiosaurus': ['2.5 m tall and 4.5-5 m long', '1,100 lbs', 'Diet: Fish', 'Group: Plesiosauria', 'Period: Early Jurassic']
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