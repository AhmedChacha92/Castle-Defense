import pygame

#création de la classe du boutton
class Button():
    #initialisation de la classe du boutton ses les paramètres
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
        #redimensionner l'image du boutton
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        #obtenir le rectangle de l'image du boutton et le positionner
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

    #méthode pour dessiner le boutton sur l'écran
	def draw(self, surface):
		action = False
		#obtenir la position de la souris
		pos = pygame.mouse.get_pos()

		#vérfier si la souris est sur le boutton
		if self.rect.collidepoint(pos):
            #vérfier si le boutton est cliqué
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                #le boutton est cliqué
				self.clicked = True
                #retourner l'action
				action = True
        #vérfier si le boutton n'est pas cliqué
		if pygame.mouse.get_pressed()[0] == 0:
            #le boutton n'est pas cliqué
			self.clicked = False

		#dessiner le boutton sur l'écran
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action