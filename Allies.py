import pygame
import os


class Allies(pygame.sprite.Sprite):
    def __init__(self, health, animation_list, x, y,speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.speed = speed
        self.health = health
        #derniere attaque
        self.last_attack = pygame.time.get_ticks()
        #temp de rafraichisse de l'attaque
        self.attack_cooldown = 1000
        self.animation_list = animation_list
        self.frame_index = 0
        self.action = 0
        #obtenir l'animation à afficher en fonction de l'action
        self.update_time = pygame.time.get_ticks()
       
        #selectionner l'image de départ
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect(0, 0, 25, 40)
        self.rect.center = (x, y)
        

    #barre de vie de l'allié 
    
    
     
    def draw_health_bar(self, surface):
        #faire apparaitre la barre de vie si la santé de l'allié est inférieur à 100
        if self.health < 100:
            BAR_LENGTH = 40
            BAR_HEIGHT = 3
            #calculer la longueur de la barre de vie en fonction de la santé de l'allié
            fill = (self.health / 100) * BAR_LENGTH
            outline_rect = pygame.Rect(self.rect.centerx - BAR_LENGTH/2, self.rect.centery - 30, BAR_LENGTH, BAR_HEIGHT)
            fill_rect = pygame.Rect(self.rect.centerx - BAR_LENGTH/2, self.rect.centery - 30, fill, BAR_HEIGHT)
            pygame.draw.rect(surface, (255,0,0), outline_rect, 1)
            pygame.draw.rect(surface, (0,255,0), fill_rect)
    # prendre des dégâts
    def take_damage(self):
        self.health -= 20
        if self.health < 0:
            self.health = 0
            self.update_action(2)
            
    #mettre à jour l'allié
    def update(self, surface, target, enemies_group):
        if self.alive:
            #vérfier si l'allié est en collision avec une attaque ennemi
            if pygame.sprite.spritecollide(self, enemies_group, False):
                #réduire la santé de l'allié
                self.health -= 20
                if self.health < 0:
                    self.health = 0
                
             # Vérifier si l'allié est en collision avec l'ennemi
            if pygame.sprite.collide_rect(self, target):
            # Arrêter l'allié et le faire attaquer
               self.update_action(1)
               #si l'énnemi est mort alors l'allié marche
            if target.health <= 0:
                     self.update_action(0)
        
            #déplacer l'allié
            if self.action == 0:
                #mettre à jour la position du rectangle
                self.rect.x -= self.speed
                
            #attack
            if self.action == 1:
                #vérfier si l'allié peut attaquer
                if pygame.time.get_ticks() - self.last_attack > self.attack_cooldown:
                    target.health -= 5
                    #si les points de vie de l'ennemi sont inférieurs à 0 alors les points de vie sont égaux à 0
                    if target.health < 0:
                        target.health = 0
                    #mettre à jour le temps de la dernière attaque
                    self.last_attack = pygame.time.get_ticks()
                #si les points de vie de l'ennemi sont inférieurs à 0 alors l'allié marche
                if target.health <= 0:
                    self.update_action(0)
                #si les points de ve de l'allié sont inférieurs à 0 alors l'allié est mort
                if self.health <= 0:
                    self.update_animation(2) 
                
        self.update_animation()
    
        pygame.draw.rect(surface, (255,255,255), self.rect,1)
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
        #vérfier si la nouvelle action est différente de l'ancienne
        if new_action != self.action:
            self.action = new_action
            #sélectionner la nouvelle image
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
        
          