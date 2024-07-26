import pygame
import os

#creer une classe pour les enemies
class Enemies(pygame.sprite.Sprite):
    def __init__(self, health, animation_list, x, y,speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.speed = speed
        self.health = health
        self.last_attack = pygame.time.get_ticks()#derniere attaque
        self.attack_cooldown = 1000
        self.animation_list = animation_list#liste des animations
        self.frame_index = 0
        self.action = 0 #0: marcher, 1: attaquer 2: mourir
        #obtenir l'animation à afficher en fonction de l'action
        self.update_time = pygame.time.get_ticks()
        
        #selectopnner l'image de départ
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect(0, 0, 25, 40)
        self.rect.center = (x, y)
        

    #mettre à jour l'ennemi 
    def update(self, surface, targets, bullet_group): 
        if self.alive:#si l'ennemi est en vie
            if pygame.sprite.spritecollide(self, bullet_group, True):#si l'ennemi est en collision avec une balle
                #réduire la santé de l'ennemi
                self.health -= 50
                if self.health < 0:
                    self.health = 0
                    self.alive = False
                    self.update_action(2)
                    
                
            #verifier si l'ennemi est parvenu au chateau
            if self.rect.right > targets.rect.left:
                self.update_action(1)
               
                ### en cours de développement ###
                #si l'ennemi entre en collision avec un allié
                ### en cours de développement ###
            
            #déplacer l'ennemi
            if self.action == 0:
                #mettre à jour la position du rectangle
                self.rect.x += self.speed    
                
            #attaquer
            if self.action == 1:
                #vérfier si l'ennemi peut attaquer
                if pygame.time.get_ticks() - self.last_attack > self.attack_cooldown:
                    targets.health -= 25
                    if targets.health < 0:
                        targets.health = 0
                    self.last_attack = pygame.time.get_ticks()#derniere attaque
            #mort
            if self.health == 0:
                targets.money += 100
                targets.score += 100
                self.update_action(2)#mourir
                self.alive = False#ennemi mort
                
        self.update_animation()
        
        #dessiner l'image dans la fenetre et l'animation
        surface.blit(self.image, (self.rect.x - 10, self.rect.y - 15))

    


        
    def update_animation(self):
        #définir le temps de rafraichissement de l'animation
        ANIMATION_COOLDOWN = 50
        
        #mettre à jour l'image dépendant de l'action
        self.image = self.animation_list[self.action][self.frame_index]
        
        #vérfier si le temps de rafraichissement est atteint
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            
            #si l'animation est terminée alors revenir à l'image de départ 
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 2:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
                
                
    def update_action(self, new_action):
        #vérfier si l'action est différente de la nouvelle action
        if new_action != self.action:
            self.action = new_action
            #mettre à jour l'animation
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()