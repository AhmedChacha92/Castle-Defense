#importation des librairies
import pygame
import math
import random
import os

import button
from Enemy import Enemies
# from Allies import AlliesRuntimeError: Execution of 'copyfile' failed - no more attempts left!

#initialisation de pygame
pygame.init()

#creation de la fenetre
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#creation de la fenetre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Castle Defense")

#limiter le nombre d'images par seconde
clock= pygame.time.Clock()
FPS=60


#définir les variables du jeu 
level = 1
high_score = 0
level_difficulty = 0
target_difficulty = 1000
DIFFICULTY_MULTIPLIER = 1.1
game_over = False 
next_level = False
ENEMY_TIMER = 1000#temp de rafraichissement pour les ennemis
last_enemy = pygame.time.get_ticks()#dernier ennemi
enemies_alive = 0
max_towers = 4
TOWER_COST = 2000#coût de la tour
tower_positions = [
[SCREEN_WIDTH - 250, SCREEN_HEIGHT - 200],
[SCREEN_WIDTH - 200, SCREEN_HEIGHT - 150],
[SCREEN_WIDTH - 150, SCREEN_HEIGHT - 150],
[SCREEN_WIDTH - 100, SCREEN_HEIGHT - 150],
]#positions des tours

### en cours de création ###
#max_allies = 10
#ALLY_TIMER = 1000#temp de rafraichissement pour les alliés
#ALLY_COST = 75 #coût de l'allié
#ally_positions = [
#[SCREEN_WIDTH - 250, SCREEN_HEIGHT - 200],
#]
### en cours de création ###

#définir une couleur
WHITE= (255,255,255)
GREEN= (0,255,0)
GREY = (100, 100, 100)


#chargement du meilleur score 
if os.path.exists("score.txt"):
    with open("score.txt", "r") as file:
        highscore = file.read()
        

#charger la police
font = pygame.font.SysFont('Futura', 30)
font_60 = pygame.font.SysFont('Futura', 60)


#chargement des images
bg= pygame.image.load("images/bg.png").convert_alpha()    
#le chateau 
castle_img_100= pygame.image.load("images/castle/castle_100.png").convert_alpha()
castle_img_50= pygame.image.load("images/castle/castle_50.png").convert_alpha()
castle_img_25= pygame.image.load("images/castle/castle_25.png").convert_alpha()

#charger les images des tours 
tower_img_100 = pygame.image.load("images/tower/tower_100.png").convert_alpha()
tower_img_50 = pygame.image.load("images/tower/tower_50.png").convert_alpha()
tower_img_25 = pygame.image.load("images/tower/tower_25.png").convert_alpha()

#charger les images des tirs
bullet_img= pygame.image.load("images/bullet.png").convert_alpha()
bullet_width= bullet_img.get_width()
bullet_height= bullet_img.get_height()
bullet_img= pygame.transform.scale(bullet_img, (int(bullet_width*0.075), int(bullet_height*0.075)))

##########################                      ############################################
                          #charger les ennemies  
##########################                      ############################################

#enemies_animations est une liste qui contient les animations des ennemis
enemy_animations = []
enemy_types = ['purple_goblin','goblin', 'red_goblin']
enemy_health = [75, 100, 100]

#charger les types d'animation des ennemis
animation_types = ["walk", "attack", "death"]
for enemy in enemy_types:
    #charger les animations
    animation_list = []
    for animation in animation_types:
        #reset le compteur des images
        temp_list = []
        #compter le nombre d'images dans le dossier
        num_of_frames = 20
        
        #boucle pour charger les images
        for i in range(num_of_frames):
            #charger l'image a partir du dossier et l'ajouter a la liste temporaire en utilisant convert_alpha pour la transparence
            img = pygame.image.load(f"images/enemies/{enemy}/{animation}/{i}.png").convert_alpha()
            enemy_width = img.get_width()
            enemy_height = img.get_height()
            img = pygame.transform.scale(img, (int(enemy_width*0.2), int(enemy_height*0.2)))
            #ajouter l'image a la liste temporaire
            temp_list.append(img)

        animation_list.append(temp_list)
        #ajouter l'animation a la liste des animations
    enemy_animations.append(animation_list)
            
        
##########################                      ############################################
                            #ANIMATION ALLIES  
##########################                      ############################################

### en cours de création ###
### en cours de création ###

"""la création des alliés sera un bon gros pas pour la suite du jeu. 
Ainsi nous pourrons invoquer des alliés qui aideront le chateau à se défendre contre les ennemis.
chaque allié aura une action spécifique, il pourra attaquer de prêt ou de loin.
Mais ces alliés couterons de l'argent, et le chateau devra les acheter pour les utiliser.
avec biensure un temp de rafraichissement pour chaque apparaition d'un allié.

les alliés auront une barre de vie, et pourront être attaqué par les ennemis.
et ils n'arrêteront pas d'attaquer les ennemis jusqu'à leurs morts. et la fin du niveau.
une fois passé a un autre niveau, les alliés seront réinitialisés et le chateau devra les racheter pour les utiliser.

Dans la prochaine mise à jour il y aura deux  types d'alliés les guérrier et les archer , ils auron une action spécifique."""


### en cours de création ###
### en cours de création ###

#image du bouton de lancement de la vague
### en cours de création ###
#image de la réparation du chateau
repair_img= pygame.image.load("images/repair.png").convert_alpha()
#image de l'armure en plus pour le chateau 
armour_img= pygame.image.load("images/armour.png").convert_alpha()

#définir le font du texte de jeu
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))
 
#fonction pour décrire le statut du jeu
def show_info():
	draw_text('Money: ' + str(castle.money), font, GREY, 10, 10)
	draw_text('Score: ' + str(castle.score), font, GREY, 180, 10)
	draw_text('High Score: ' + str(high_score), font, GREY, 180, 30)
	draw_text('Level: ' + str(level), font, GREY, SCREEN_WIDTH // 2, 10)
	draw_text('Health: ' + str(castle.health) + " / " + str(castle.max_health), font, GREY, SCREEN_WIDTH - 230, SCREEN_HEIGHT - 50)
	draw_text('1000', font, GREY, SCREEN_WIDTH - 220 , 70)
	draw_text(str(TOWER_COST), font, GREY, SCREEN_WIDTH - 150, 70)
	draw_text('500', font, GREY, SCREEN_WIDTH - 70 , 70)
        
        
        
        
#la classe chateau
class Castle():
	def __init__(self, image100, image50, image25, x, y, scale):
		self.health = 1000
		self.max_health = self.health
		self.fired = False
		self.money = 0
		self.score = 0
        #initialiser l'image du chateau
		width = image100.get_width()
		height = image100.get_height()
        #redimensionner l'image du chateau
		self.image100 = pygame.transform.scale(image100, (int(width * scale), int(height * scale)))
		self.image50 = pygame.transform.scale(image50, (int(width * scale), int(height * scale)))
		self.image25 = pygame.transform.scale(image25, (int(width * scale), int(height * scale)))
		self.rect = self.image100.get_rect()
		self.rect.x = x
		self.rect.y = y


	def shoot(self):
		pos = pygame.mouse.get_pos()
		x_dist = pos[0] - self.rect.midleft[0]
		y_dist = -(pos[1] - self.rect.midleft[1])
		self.angle = math.degrees(math.atan2(y_dist, x_dist))
		#get mouseclick
		if pygame.mouse.get_pressed()[0] and self.fired == False and pos[1] > 70:
			self.fired = True
			bullet = Bullet(bullet_img, self.rect.midleft[0], self.rect.midleft[1], self.angle)
			bullet_group.add(bullet)
		#reset mouseclick
		if pygame.mouse.get_pressed()[0] == False:
			self.fired = False



	def draw(self):
		#check which image to use based on health
		if self.health <= 250:
			self.image = self.image25
		elif self.health <= 500:
			self.image = self.image50
		else:
			self.image = self.image100

		screen.blit(self.image, self.rect)

	def repair(self):
		if self.money >= 1000 and self.health < self.max_health:
			self.health += 500
			self.money -= 1000
			if castle.health > castle.max_health:
				castle.health = castle.max_health

	def armour(self):
		if self.money >= 500:
			self.max_health += 250
			self.money -= 500


#création d'une classe tower pour l'ajout des tours qui défendent le chateau
class Tower(pygame.sprite.Sprite):
	def __init__(self, image100, image50, image25, x, y, scale):
		pygame.sprite.Sprite.__init__(self)
        #initialiser les variables de la tour
		self.got_target = False
		self.angle = 0
		self.last_shot = pygame.time.get_ticks()
        #initialiser l'image de la tour
		width = image100.get_width()
		height = image100.get_height()
        #redimensionner l'image de la tour
		self.image100 = pygame.transform.scale(image100, (int(width * scale), int(height * scale)))
		self.image50 = pygame.transform.scale(image50, (int(width * scale), int(height * scale)))
		self.image25 = pygame.transform.scale(image25, (int(width * scale), int(height * scale)))
		self.image = self.image100
		self.rect = self.image100.get_rect()
		self.rect.x = x
		self.rect.y = y

    #fonction pour dessiner la tour
	def update(self, enemy_group):
		self.got_target = False
        #vérifier si l'ennemi est en vie
		for e in enemy_group:
			if e.alive:
				target_x, target_y = e.rect.midbottom
				self.got_target = True
				break
        #calculer l'angle de la tour
		if self.got_target:
			x_dist = target_x - self.rect.midleft[0]
			y_dist = -(target_y - self.rect.midleft[1])
			self.angle = math.degrees(math.atan2(y_dist, x_dist))
            #vérifier si la tour peut tirer
			shot_cooldown = 1000
			#tirer 
			if pygame.time.get_ticks() - self.last_shot > shot_cooldown:
				self.last_shot = pygame.time.get_ticks()
				bullet = Bullet(bullet_img, self.rect.midleft[0], self.rect.midleft[1], self.angle)
				bullet_group.add(bullet)

		#Vérifier quelle image utiliser en fonction de la santé
		if castle.health <= 250:
			self.image = self.image25
		elif castle.health <= 500:
			self.image = self.image50
		else:
			self.image = self.image100

#creer la classe bullet
class Bullet(pygame.sprite.Sprite):
	def __init__(self, image, x, y, angle):#initialiser les variables de la balle
		pygame.sprite.Sprite.__init__(self)
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.angle = math.radians(angle)#convertir l'angle en radians
		self.speed = 10
        #calculer la vitesse de la balle
		self.dx = math.cos(self.angle) * self.speed
		self.dy = -(math.sin(self.angle) * self.speed)


	def update(self):
        #vérifier si la balle est hors de l'écran
		if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
			self.kill()			

		#déplacer la balle
		self.rect.x += self.dx
		self.rect.y += self.dy

        
#création d'une class pour le viseur 
class Crosshair():
    def __init__(self, scale):
        image = pygame.image.load('images/crosshair.png').convert_alpha()
        width = image.get_width()
        height = image.get_height()
        
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()


        #cacher le curseur de la souris pour laisser le viseur
        pygame.mouse.set_visible(False)
        
        
    #fonction pour dessiner le viseur sur l'écran
    def draw(self):
        mx, my = pygame.mouse.get_pos()#obtenir la position de la souris
        self.rect.center = (mx, my)#définir le centre du viseur sur la position de la souris
        screen.blit(self.image, self.rect)#dessiner le viseur sur l'écran
		
        
        
#creer le chateau
castle = Castle(castle_img_100, castle_img_50, castle_img_25, SCREEN_WIDTH - 250, SCREEN_HEIGHT - 300, 0.2)

#créer le viseur 
crosshair = Crosshair(0.025)

#diviser le viseur par 2 pour le réduire de moitié
crosshair_width = crosshair.image.get_width() // 2


#créer les boutons 
repair_button = button.Button(SCREEN_WIDTH - 220, 10, repair_img, 0.5)
tower_button = button.Button(SCREEN_WIDTH - 140, 10, tower_img_100, 0.1)
armour_button = button.Button(SCREEN_WIDTH - 75, 10, armour_img, 1.5)

#creer les groupes de sprites
tower_group = pygame.sprite.Group()
bullet_group= pygame.sprite.Group()
enemy_group= pygame.sprite.Group()
allies_group = pygame.sprite.Group()

#creer les alliés
###### en cours de création ##
#### en cours de création ####


#la boucle du jeu
run=True
while run:
    
    clock.tick(FPS)
    #si le jeu est en cours
    if game_over == False:
            screen.blit(bg, (0, 0))

            #dessiner le chateau
            castle.draw()
            castle.shoot()
            #dessiner la ou les  tours
            tower_group.draw(screen)
            tower_group.update(enemy_group)

            #dessiner le crosshair
            crosshair.draw()

            #dessiner les tirs
            bullet_group.update()
            bullet_group.draw(screen)

            #dessiner les ennemis
            enemy_group.update(screen, castle, bullet_group)
            
            #Dessiner les alliés
            ### en cours de création ###
            ### en cours de création ###
            #montrer les détails  
            show_info()
            
            #dessiner les boutons d'actions
            if repair_button.draw(screen):
                castle.repair()
            if tower_button.draw(screen):
                #vériier si le joueur a assez d'argent pour acheter une tour
                if castle.money >= TOWER_COST and len(tower_group) < max_towers:
                    tower = Tower(
                        tower_img_100,
                        tower_img_50,
                        tower_img_25,
                        tower_positions[len(tower_group)][0],
                        tower_positions[len(tower_group)][1],
                        0.2
                        )#ajouter la tour au groupe de tours
                    tower_group.add(tower)#ajouter la tour au groupe de tours
                    
                    castle.money -= TOWER_COST#soustraie le coût de la tour
            if armour_button.draw(screen):
                castle.armour()
                
                
        #créations des ennemis en systeme de vagues 
		#vérifier si le nombre d'ennemis est inférieur à la cible
            if level_difficulty < target_difficulty:
                if pygame.time.get_ticks() - last_enemy > ENEMY_TIMER:#créer les ennemis de manière aléatoire
                    e = random.randint(0, len(enemy_types) -1)#choisir un ennemi aléatoire
                    enemy = Enemies(enemy_health[e], enemy_animations[e], -100, SCREEN_HEIGHT - 100, 1)
                    enemy_group.add(enemy)
                    last_enemy = pygame.time.get_ticks()#dernier ennemi
                    #augmenter la difficulté du niveau des ennemis
                    level_difficulty += enemy_health[e]
                    
            
            #si tout les énnemis ont été crées
            if level_difficulty >= target_difficulty:
                #calculer le nombre d'ennemis en vie
                enemies_alive = 0
                #boucle pour vérifier si les ennemis sont en vie
                for e in enemy_group:
                    if e.alive == True:
                        enemies_alive += 1
                #si tout les ennemis sont morts       
                if enemies_alive == 0 and next_level == False:
                    #passer au niveau suivant
                    next_level = True
                    #réinitialiser le temps du niveau
                    level_reset_time = pygame.time.get_ticks()
            
            #passage à un autre niveau
            if next_level == True:
                #dessiner le texte du niveau
                draw_text('LEVEL COMPLETE!', font_60, WHITE, 200, 300)
                #mettre à jour le meilleur score
                if castle.score > high_score:
                    high_score = castle.score
                    with open('score.txt', 'w') as file:
                        file.write(str(high_score))
                if pygame.time.get_ticks() - level_reset_time > 1500:
                    next_level = False
                    level += 1
                    last_enemy = pygame.time.get_ticks()
                    target_difficulty *= DIFFICULTY_MULTIPLIER
                    level_difficulty = 0
                    enemy_group.empty()
            
            #vérifier si le joueur a perdu
            if castle.health <= 0:
                game_over = True
    else:
        #la partie est terminée
        draw_text('GAME OVER!', font, GREY, 300, 300)
        draw_text('PRESS "A" TO PLAY AGAIN!', font, GREY, 250, 360)
        pygame.mouse.set_visible(True)
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            #réinitialiser les variables du jeu pour recommencer
            game_over = False
            level = 1
            target_difficulty = 1000
            level_difficulty = 0
            last_enemy = pygame.time.get_ticks()
            enemy_group.empty()
            tower_group.empty()
            castle.score = 0
            castle.health = 1000
            castle.max_health = castle.health
            castle.money = 0
            pygame.mouse.set_visible(False)
            

        #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display window
    pygame.display.update()
        
pygame.quit()
