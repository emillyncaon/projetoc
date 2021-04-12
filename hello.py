import pygame
import os
import random
import csv
game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1'],
            ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','1','1','1'],
            ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]

grass_image = pygame.image.load('Imagens/Tiles/grass.png')
TILE_SIZE = grass_image.get_width()

dirt_image = pygame.image.load('Imagens/Tiles/dirt.png')

def main():
    pygame.init()
    tela=pygame.display.set_mode([600, 400])              #Resolução
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

    #Cores para utilizar
    BG=(135,206,234)
    BRANCO=(255,255,255)

    #Cria um background
    def draw_bg():
        tela.fill(BG)
        pygame.draw.line(tela, BRANCO,(0,400),(800,400))

    


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

    

   
    
    player=PP(200,200,0.3,5)
   



    

    sair=False
    #Estrutura para fechar jogo
    while sair==False:
        tela.fill((146,244,255))
        tile_rects = []
        #Novo
        y = 0
        for row in game_map:
            x = 0
            for tile in row:
              if tile == '1':
                tela.blit(dirt_image, (x * TILE_SIZE, y * TILE_SIZE))
              if tile == '2':
                tela.blit(grass_image, (x * TILE_SIZE, y * TILE_SIZE))
              if tile != '0':
                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
              x += 1
            y += 1
        #_________________________________________________________________________________________

        clock.tick(fps)
        
        
        player.update_animation()  #faz o update a partir dos fps
        player.draw()              #chama jogador      
        

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

        pygame.display.update()          

         
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