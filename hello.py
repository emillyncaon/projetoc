import pygame
import os
import csv

def main():
    pygame.init()
    tela=pygame.display.set_mode([800, 640])
    pygame.display.set_caption("We have to decide yet!") #nome jogo

    #Variaveis de movimentação
    moving_left = False
    moving_right = False


    #framerat
    clock=pygame.time.Clock()
    fps=60

    #varivaeis jogo
    GRAVITY=0.5
    Linhas=16
    Colunas=150
    tile_size=40
    tile_types=5
    level=1

    #Tiles na lista
    img_list=[]
    for x in range(tile_types):
        img= pygame.image.load(f'C:/Users/gusta/Documents/PETEEL/Projeto/Imagens/Tiles/{x}.png')
        img= pygame.transform.scale(img, (tile_size, tile_size))
        img_list.append(img)

    def draw_bg():
        tela.fill(BG)
        pygame.draw.line(tela, BRANCO,(0,400),(800,400))

    #cor
    BG=(135,206,235)
    BRANCO=(255,255,255)

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
                    for i in range(2):
                        img1 = pygame.image.load(f"C:/Users/gusta/Documents/PETEEL/Projeto/Imagens/Personagem/{i}.png")
                        img1 = pygame.transform.scale(img1, (int(img1.get_width() * scale), int(img1.get_height() * scale)))
                        temp_list.append(img1)
                    self.animation_list.append(temp_list)
                    temp_list=[]
                    for i in range(1):
                        img1 = pygame.image.load(f"C:/Users/gusta/Documents/PETEEL/Projeto/Imagens/Personagem-Parado/{i}.png")
                        img1 = pygame.transform.scale(img1, (int(img1.get_width() * scale), int(img1.get_height() * scale)))
                        temp_list.append(img1)
                    self.animation_list.append(temp_list)
                    self.image= self.animation_list[self.action][self.frame_index]
                    self.rect = self.image.get_rect()
                    self.rect.center = (x, y)

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
            
            #Gravidade aqui
            self.vel_y += GRAVITY
            if self.vel_y >10:
                self.vel_y
            dy += self.vel_y

            #colisao com chão
            if self.rect.bottom +dy >400:
                dy=400-self.rect.bottom
                self.in_air = False


            self.rect.x += dx
            self.rect.y += dy
        
        def update_animation(self):
            #ARRUMAR COOLDOWN QUANDO COLOCAR AS PNS PERMANENTES
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
                        if tile >=0 and tile <=8:
                            self.obstacle_list.append(tile_data)
                        elif tile >=9 and tile <=10:
                            pass #Colocar lava ou agua aqui
                        elif tile >=11 and tile<=14:
                            pass #decoração
                        elif tile==20:
                            pass #saida
        def draw(self):
            for tile in self.obstacle_list:
                screen.blit(tile[0],tile[1])

    
    player=PP(200,200,0.3,5)
   
    #lista de tiles para criar o cenário

    world_data= []
    for row in range(Linhas):
        r=[-1]*Colunas
        world_data.append(r)

    #load in level data to create world
    with open('C:/Users/gusta/Documents/PETEEL/Projeto/Imagens/level1.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for x, row in enumerate(reader):
            for y, tile in enumerate(row):
                world_data[x][y]=(tile)
    
    world=World()




    sair=False
    #Estrutura para fechar jogo
    while sair==False:
        clock.tick(fps)
        draw_bg()
        world.draw()
        player.update_animation()
        player.draw()      
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