import pygame

pygame.init()
tela = pygame.display.set_mode([800, 640])
pygame.display.set_caption("We have to decide yet!") #nome jogo

#framerat
clock = pygame.time.Clock()
fps=120

tela_width = 800
tela_height = 640

#variavel jogo
main_menu = True

#load images
fundo_img = pygame.image.load('imagens_tela_inicial/fundo.png')
jogar_img = pygame.image.load('imagens_tela_inicial/jogar.png')
sobre_img = pygame.image.load('imagens_tela_inicial/sobre.png')
comojogar_img = pygame.image.load('imagens_tela_inicial/comojogar.png')

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        #draw button
        tela.blit(self.image, self.rect)

        return action

#buttons
jogar_button = Button(tela_width // 2 - 50, tela_height // 3 - 50, jogar_img)
comojogar_button = Button(tela_width // 2 - 65, tela_height // 4 - 65, comojogar_img)
sobre_button = Button(tela_width // 2 - 50, tela_height // 2 - 80, sobre_img)



run = True
while run: 
    
    clock.tick(fps)

    tela.blit(fundo_img, (0, 0))


    if main_menu == True:
        if jogar_button.draw():
            main_menu = False
        if sobre_button.draw():
            run = False
        if comojogar_button.draw():
            main_menu = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()


