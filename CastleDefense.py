#importation des librairies

import pygame
import math
from Enemy import Enemy
#initialisation de pygame
pygame.init()

#creation de la fenetre
screen_width = 800

screen_height = 600

#creation de la fenetre
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Castle Defense")

#limiter le nombre d'images par seconde
clock= pygame.time.Clock()
FPS=60

#chargement des images
bg= pygame.image.load("images/bg.png").convert_alpha()

#le chateau avec tout ses points de vie
castle_img_100= pygame.image.load("images/castle/castle_100.png").convert_alpha()

#charger les images des tirs
bullet_img= pygame.image.load("images/bullet.png").convert_alpha()
#changer la taille de l'image
bullet_width= bullet_img.get_width()
bullet_height= bullet_img.get_height()
bullet_img= pygame.transform.scale(bullet_img, (int(bullet_width*0.075), int(bullet_height*0.075)))

##########################              ############################################
                            #ANIMATION
##########################             ############################################
#charger les images des ennemis
enemy_animations = []
enemy_types = ["knight"]
enemy_health = [100]

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
        for i in range(num_of_frames):
            #charger l'image a partir du dossier et l'ajouter a la liste temporaire en utilisant convert_alpha pour la transparence
            img = pygame.image.load(f"images/enemies/{enemy}/{animation}/{i}.png").convert_alpha()
            #changer la taille de l'image en divisant par 2 pour la réduire de moitié
            enemy_width = img.get_width()
            enemy_height = img.get_height()
            img = pygame.transform.scale(img, (int(enemy_width*0.2), int(enemy_height*0.2)))
            #ajouter l'image a la liste temporaire
            temp_list.append(img)
            #ajouter la liste temporaire a la liste des animations
        animation_list.append(temp_list)
        #ajouter l'animation a la liste des animations
    enemy_animations.append(animation_list)
            
        

#définir une couleur
WHITE= (255,255,255)


#la classe chateau
class Castle:
    def __init__(self, image100,x , y, scale):
        self.health=1000
        self.max_health=self.health
        self.fired= False
        
       #changer la taille de l'image
        width = image100.get_width()
        height = image100.get_height()
    
        
        self.image100= pygame.transform.scale(image100, (int(width*scale), int(height*scale)))
        #rect pour l'image du chateau
        self.rect= self.image100.get_rect()
        
        #position du chateau
        self.rect.center= (x,y)
        self.x= x
        self.y= y
    
    #les tirs du chateau
    def shoot(self):
        #obtenir la position de la souris
        position = pygame.mouse.get_pos()
        #calculer l'angle entre le chateau et la souris
        x_distance = position[0] - self.rect.midleft[0]
        y_distance = - (position[1] - self.rect.midleft[1])
        self.angle = math.degrees(math.atan2(y_distance, x_distance))
        
        #creer un tir en maintenant le clic gauche
        if pygame.mouse.get_pressed()[0] and self.fired == False:#le tir est en cours
            self.fired= True
            bullet = Bullet(bullet_img, self.rect.midleft[0], self.rect.midleft[1], self.angle)
            bullet_group.add(bullet)
            
        #réinitialiser le tir
        if pygame.mouse.get_pressed()[0] == False:
            self.fired= False
  
    #dessiner le chateau
    def draw(self):
        self.image = self.image100
        #afficher l'image
        screen.blit(self.image, self.rect)
        
        
#creer la classe bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self,image, x, y, angle):
        #j'appelle le constructeur de la classe mère
        pygame.sprite.Sprite.__init__(self)
        #rect pour l'image du tir
        self.image= image
        self.rect= self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #changer l'angle en radian
        self.angle= math.radians(angle)
        #vitesse du tir en calculant les composantes x et y
        self.speed = 10
        self.dx = math.cos(self.angle) * self.speed
        self.dy = -(math.sin(self.angle) * self.speed)        
    
    #dessiner le tir
    def draw(self, surface):
        surface.blit(self.image, self.rect)
            
        #mettre a jour la position du tir
    def update(self):
        #verifier si le tir sort de l'écran
        if self.rect.right < 0 or self.rect.left > screen_width or self.rect.bottom < 0 or self.rect.top > screen_height:
            self.kill()
        #mouvement du tir
        self.rect.x += self.dx
        self.rect.y += self.dy
        
    
     

#creer un groupe 
bullet_group= pygame.sprite.Group()
enemy_group= pygame.sprite.Group()

        
def draw(self):
        screen.blit(self.img, self.rect)


#creer les ennemis
enemy1= Enemy(enemy_health[0],enemy_animations[0], 200,screen_height - 100, 1)
enemy_group.add(enemy1)
#creer le chateau
castle= Castle(castle_img_100, screen_width - 50, screen_height - 210, 0.3)  










 
#la boucle du jeu
run=True
while run:
    
    clock.tick(FPS)
    
    #dessiner l'arriere plan
    screen.blit(bg, (0,0))
    
    #dessiner le chateau avec la methode draw
    castle.draw()
    
    
    #tirer avec le chateau avec la methode shoot
    castle.shoot()
    
    
    
    #dessiner les tir avec la methode draw
    for bullet in bullet_group:
        bullet.draw(screen)
    bullet_group.update()
    # bullet_group.draw(screen)
    
    #dessiner les ennemis avec la methode draw
    enemy_group.draw(screen)
    
    
    
    # Mettre à jour l'affichage pour refléter les changements
    pygame.display.flip()
    #gestionnaire d'événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        #mettre a jour l'écran
        pygame.display.update()    
        
pygame.quit()
