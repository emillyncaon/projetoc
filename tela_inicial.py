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
jogar_img = pygame.transform.scale(jogar_img, (int(jogar_img.get_width() * 1), int(jogar_img.get_height() * 1)))
sobre_img = pygame.image.load('imagens_tela_inicial/sobre.png')
comojogar_img = pygame.image.load('imagens_tela_inicial/comojogar.png')
personagem1_img = pygame.image.load('imagens_tela_inicial/personagem1.png')
personagem1_img = pygame.transform.scale(personagem1_img, (int(personagem1_img.get_width() * 4), int(personagem1_img.get_height() * 4)))
personagem2_img = pygame.image.load('imagens_tela_inicial/personagem2.png')
personagem2_img = pygame.transform.scale(personagem2_img, (int(personagem2_img.get_width() * 4), int(personagem2_img.get_height() * 4)))

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
jogar_button = Button(tela_width // 2 - 50, tela_height // 1 - 200, jogar_img)
comojogar_button = Button(tela_width // 1 - 275, tela_height // 1 - 200, comojogar_img)
sobre_button = Button(tela_width // 2 - 235, tela_height // 1 - 193, sobre_img)
personagem1_button = Button(tela_width // 2 - 150, tela_height // 2 - 75, personagem1_img)
personagem2_button = Button(tela_width // 2 + 20, tela_height // 2 - 75, personagem2_img)


flag=0
run = True
while run: 
    
    clock.tick(fps)
    tela.blit(fundo_img, (0, 0))

    if main_menu == True:
        #draw menu
        if jogar_button.draw():
            if (flag==1):
                main_menu = False
        if sobre_button.draw():
            if (flag==0):
                run = False
        if comojogar_button.draw():
            if (flag==0):
                main_menu = False
        if personagem1_button.draw():
            flag = 1
        if personagem2_button.draw():
            flag = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()


