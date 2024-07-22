import pygame

#creer une classe pour les enemies
class Enemy(pygame.sprite.Sprite):
    def __init__(self, health, animation_list, x, y,speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.health = health
        self.speed = speed
        self.animation_list = animation_list
        self.frame_index = 0
        self.action = 0
        #obtenir l'animation à afficher en fonction de l'action
        self.update_time = pygame.time.get_ticks()
        
        #selectopnner l'image de départ
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
    
    #mettre à jour l'ennemi
    def update(self, surface):
        
        self.update_animation()
        
        #dessiner l'image dans la fenetre
        surface.blit(self.image, self.rect)
        
        
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
                self.frame_index = 0

    def draw(self, surface):
        # Dessiner l'image dans la fenêtre
        surface.blit(self.image, self.rect)