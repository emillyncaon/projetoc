import pygame
import os
import csv

def main():
    pygame.init()
    tela=pygame.display.set_mode([800, 640])              #Resolução
    pygame.display.set_caption("We have to decide yett!")  #nome jogo(A ser decidido)

    #Variaveis de movimentação
    moving_left = False
    moving_right = False

    #Framerate
    clock=pygame.time.Clock()
    fps=60

    #Gravidade
    GRAVITY=0.5

    #Config Tile 
    ROWS=16
    COLS=150
    tile_size=40
    tile_types=5   #Com todas as imagens, aumentar aqui
    level=1        #Possibilidade de acrescentar mais

    #Criar uma lista de Tiles
    img_list=[]
    for x in range(tile_types):
        img= pygame.image.load(f'Imagens/Tiles/{x}.png')
        img= pygame.transform.scale(img, (tile_size, tile_size))
        img_list.append(img)

    #Cria um background
    def draw_bg():
        tela.fill(BG)
        pygame.draw.line(tela, BRANCO,(0,400),(800,400))

    #Cores para utilizar
    BG=(135,206,234)
    BRANCO=(255,255,255)


    #Funções para jogador
    class PP(pygame.sprite.Sprite):
        def __init__(self, x, y, scale, speed):
                    pygame.sprite.Sprite.__init__(self)
                    self.alive = True
                    self.speed=speed
                    self.direction=1
                    self.vel_y=0
                    self.jump =False
                    self.in_air=True
                    self.flip=False
                    self.animation_list=[]
                    self.frame_index=0
                    self.action = 0
                    self.update_time = pygame.time.get_ticks()
                    temp_list=[]
                    #Lembrar que dependendo da nossa animação do personagem podemos aumentar range
                    #Aqui é feito animação do personagem andando(flip de imagens)
                    for i in range(2):
                        img1 = pygame.image.load(f"Imagens/Personagem/{i}.png")
                        img1 = pygame.transform.scale(img1, (int(img1.get_width() * scale), int(img1.get_height() * scale)))
                        temp_list.append(img1)
                    self.animation_list.append(temp_list)
                    temp_list=[]
                    #Aqui é feito animação do personagem parado(flip de imagens)
                    for i in range(1):
                        img1 = pygame.image.load(f"Imagens/Personagem-Parado/{i}.png")
                        img1 = pygame.transform.scale(img1, (int(img1.get_width() * scale), int(img1.get_height() * scale)))
                        temp_list.append(img1)
                    self.animation_list.append(temp_list)
                    self.image= self.animation_list[self.action][self.frame_index]
                    self.rect = self.image.get_rect()
                    self.rect.center = (x, y)

        #Definições de movimentação
        def move(self, moving_left,moving_right):
            dx=0
            dy=0
            if moving_left:
                dx=-self.speed
                self.flip = True
                self.direction = -1 
            if moving_right:
                dx=self.speed
                self.flip = False
                self.direction = 1
            if (self.jump == True) and (self.in_air == False):
                #ALTURA PULO A SER DEFINIDA COM PERSONAGEM DEFINIDO     
                self.vel_y = -11
                self.jump = False
                self.in_air=True
            
            #Gravidade
            self.vel_y += GRAVITY
            if self.vel_y >10:
                self.vel_y
            dy += self.vel_y

            #Colisao com chão
            if self.rect.bottom +dy >400:
                dy=400-self.rect.bottom
                self.in_air = False


            self.rect.x += dx
            self.rect.y += dy
        
        def update_animation(self):
            #Arrumar COOLDOWN dependendo das novas PNGS para o personagem
            #Isso aqui é feito para quando acabar as imagens voltar para imagem zero e assim ir fazendo o loop
            ANIMATION_COOLDOWN = 100
            self.image=self.animation_list[self.action][self.frame_index]
            if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
            if self.frame_index >=len(self.animation_list[self.action]):
                self.frame_index=0

        def update_action(self, new_action):
            if new_action != self.action:
                self.action = new_action
                self.frame_index=0
                self.update_time=pygame.time.get_ticks()

        def draw(self):
            tela.blit(pygame.transform.flip(self.image, self.flip, False),self.rect)

    #Criação do mapa com tiles
    class World():
        def __init__(self):
            self.obstacle_list=[]

        def process_data(self, data):
            #olhar todos os valores
            for y, row in enumerate(data):
                for x, tile in enumerate(row):
                    if tile>=0:
                        img=img_list[tile]
                        img_rect=img.get_rect()
                        img_rect.x=x*tile_size
                        img_rect.y=y*tile_size
                        tile_data=(img, img_rect)
                        if tile >=0 and tile <=5:
                            self.obstacle_list.append(tile_data)
                        #elif tile >=9 and tile <=10:
                            #pass #Colocar lava ou agua aqui
                        #elif tile >=11 and tile<=14:
                            #pass #Decoração
                        #elif tile==20:
                            #pass #Saida
        def draw(self):
            for tile in self.obstacle_list:
                screen.blit(tile[0],tile[1])

    
    player=PP(200,200,0.3,5)
   
    #Lista csv de tiles para criar o cenário

    world_data= []
    for row in range(ROWS):
        r=[-1]*COLS
        world_data.append(r)

    #Load do mundo a partir do csv
    with open('Imagens/level1.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for x, row in enumerate(reader):
            for y, tile in enumerate(row):
                world_data[x][y]=(tile)
    
    world=World()

    sair=False
    #Estrutura para fechar jogo
    while sair==False:

        clock.tick(fps)
        draw_bg()                  #chama background
        world.draw()               #chama world
        player.update_animation()  #faz o update a partir dos fps
        player.draw()              #chama jogador      
        pygame.display.update()

        if player.alive:
            if moving_left or moving_right:
                player.update_action(0)
            else: 
                player.update_action(1)

            player.move(moving_left,moving_right)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair=True
            #Movimentação
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moving_left= True
                if event.key == pygame.K_d:
                    moving_right=True
                if event.key == pygame.K_w and player.alive:
                    player.jump=True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    moving_left=False
                if event.key == pygame.K_d:
                    moving_right=False           


    pygame.quit()

main()


#1. Escolher personagem
#2. Escolher blocos que vamos usar
#3. Fazer mapa basico
#4. Implementar mapa com scroll
#5. Entrada e conclusão de nível colocar


#Obstaculos
#Tela de entrada
#Fazer os outros 3 niveis
#d