import pygame
import os
import random
game_map = [['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','1','1','1','1','2','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['0','21','0','1','1','0','0','0','0','0','0','0','0','0','0','0','0','20','0','2','2','2','21','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','20','0','2','2','2','1','1','1','1','1','1','1','1','1','17','17','1','1','1','1','1','1','1','1','1','1''1','1','1','1','1','1','1','1','1','17','17','1','1','1','1','1','1','1','1','1','1'],
           ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','1','1','1','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','1','1','1'],
           ['1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','1','1','1','1','1'],
           ['1','1','2','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','2','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1'],
           ['1','1','1','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1'],
           ['1','1','1','0','0','0','0','0','2','2','16','16','2','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','2','2','16','16','2','1','1','1','1','1','1','1','1','1'],
           ['1','1','1','2','2','2','2','2','1','1','17','17','1','1','1','1','1','1','1','1','1','1','1','1','2','2','2','2','2','1','1','17','17','1','1','1','1','1','1','1','1','1','1'],
           ['1','1','1','1','1','1','1','1','1','1','17','17','1','1','1','1','1','1','1','1','1','1''1','1','1','1','1','1','1','1','1','17','17','1','1','1','1','1','1','1','1','1','1']]



#Inicialização Blocos
tile_size=40
dirt_image = pygame.image.load('Imagens/Tiles/1.png')
dirt_image = pygame.transform.scale(dirt_image, (tile_size, tile_size))
grass_image = pygame.image.load('Imagens/Tiles/2.png')
grass_image = pygame.transform.scale(grass_image, (tile_size, tile_size))
rockdirt_image = pygame.image.load('Imagens/Tiles/3.png')
rockdirt_image = pygame.transform.scale(rockdirt_image, (tile_size, tile_size))
sand_image = pygame.image.load('Imagens/Tiles/4.png')
sand_image = pygame.transform.scale(sand_image, (tile_size, tile_size))
snow_image = pygame.image.load('Imagens/Tiles/5.png')
snow_image = pygame.transform.scale(snow_image, (tile_size, tile_size))
rock_image = pygame.image.load('Imagens/Tiles/6.png')
rock_image = pygame.transform.scale(rock_image, (tile_size, tile_size))
water_image = pygame.image.load('Imagens/Tiles/14.png')
water_image = pygame.transform.scale(water_image, (tile_size, tile_size))
waterf_image = pygame.image.load('Imagens/Tiles/15.png')
waterf_image = pygame.transform.scale(waterf_image, (tile_size, tile_size))
lava_image = pygame.image.load('Imagens/Tiles/16.png')
lava_image = pygame.transform.scale(lava_image, (tile_size, tile_size))
lavaf_image = pygame.image.load('Imagens/Tiles/17.png')
lavaf_image = pygame.transform.scale(lavaf_image, (tile_size, tile_size))
signexit_image = pygame.image.load('Imagens/Tiles/20.png')
signexit_image = pygame.transform.scale(signexit_image, (tile_size, tile_size))
signr_image = pygame.image.load('Imagens/Tiles/21.png')
signr_image = pygame.transform.scale(signr_image, (tile_size, tile_size))
signl_image = pygame.image.load('Imagens/Tiles/22.png')
signl_image = pygame.transform.scale(signl_image, (tile_size, tile_size))

pine1_image = pygame.image.load('Imagens/Background/pine1.png')
pine2_image = pygame.image.load('Imagens/Background/pine2.png')
mountain_image = pygame.image.load('Imagens/Background/mountain.png')
sky_image = pygame.image.load('Imagens/Background/sky.png')

def main():
    pygame.init()
    tela=pygame.display.set_mode([800, 640])              #Resolução
    pygame.display.set_caption("We have to decide yett!")  #nome jogo(A ser decidido)

    #Variaveis de movimentação
    moving_left = False
    moving_right = False

    #Framerate
    clock=pygame.time.Clock()
    fps=120

    #Gravidade
    GRAVITY=0.5

#    def load_map(path):
#      f=open(path + '.txt','r')
#      data=f.read()
#      f.close()
#      data=data.split('\n')
#      game_map=[]
#      for row in data:
#        game_map.append(list(row))
#      return game_map
#
#    game_map=load_map('Imagens/map')

    def draw_bg():
      width=sky_image.get_width()
      for x in range(5):
        tela.blit(sky_image, ((x*width)-bg_scroll*0.5,0))
        tela.blit(mountain_image, ((x*width)-bg_scroll*0.6,100))
        tela.blit(pine1_image, ((x*width)-bg_scroll*0.7,230))
        tela.blit(pine2_image, ((x*width)-bg_scroll*0.8,290))

    #Config Tile
    screen_width=800
    screen_height=640
    ROWS=16
    COLS=150
    tile_size=40
    tile_types=5   #Com todas as imagens, aumentar aqui
    level=1        #Possibilidade de acrescentar mais
    screen_scroll=0
    bg_scroll=0

    #Funções para jogador
    class PP(pygame.sprite.Sprite):
        def __init__(self, x, y, scale, speed):
                    pygame.sprite.Sprite.__init__(self)
                    self.alive = True
                    self.speed=speed
                    self.health = 100
                    self.max_health = self.health
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
                    self.width=self.image.get_width()
                    self.height=self.image.get_height()

      
            
        def update(self):
		                self.update_animation()
		                self.check_alive()
                  
  


        #Definições de movimentação
        def move(self, moving_left,moving_right):
            screen_scroll=0
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


            for g in range(200):
                #check collision in the x direction
                if tile_rects[g].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                #check for collision in the y direction
                if tile_rects[g].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if below the ground, i.e. jumping
                    if self.vel_y < 0:
                        self.vel_y = 0
                        dy = tile_rects[g].bottom - self.rect.top
                    #check if above the ground, i.e. falling
                    elif self.vel_y >= 0:
                        self.vel_y = 0
                        self.in_air = False
                        dy = tile_rects[g].top - self.rect.bottom

            if self.rect.bottom>screen_height:
              self.health = 0
            if self.rect.bottom<0:
              self.health=0

            for l in range(10):
                if tile_lava[l].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    player.health=0
                    dx = 0
                if tile_rects[g].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    if self.vel_y < 0:
                        self.vel_y = 0
                        dy = tile_rects[g].bottom - self.rect.top
                        player.health=0        
                    elif self.vel_y >= 0:
                        self.vel_y = 0
                        self.in_air = False
                        dy = tile_rects[g].top - self.rect.bottom



            self.rect.x += dx
            self.rect.y += dy

        def update_animation(self):
            #Arrumar COOLDOWN dependendo das novas PNGS para o personagem
            #Isso aqui é feito para quando acabar as imagens voltar para imagem zero e assim ir fazendo o loop
            ANIMATION_COOLDOWN = 120
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

        def check_alive(self):
		        if self.health <= 0:
			        self.health = 0
			        self.speed = 0
			        self.alive = False
			        self.update_action(3)
        
        def draw(self):
            tela.blit(pygame.transform.flip(self.image, self.flip, False),self.rect)






    player=PP(320,0,1.8,5)

    lava_group = pygame.sprite.Group()

    sair=False
    #Estrutura para fechar jogo
    while sair==False:
        
        #scroll[0] += 1/5*player.rect.x-scroll[0]
    
        if (player.rect.right > 390):
          player.rect.x -= player.speed
          screen_scroll += - player.speed
          bg_scroll -= - player.speed
        if (player.rect.right < 280):
          player.rect.x += player.speed
          screen_scroll -= - player.speed
          bg_scroll += - player.speed


        draw_bg()
        tile_rects = []
        tile_lava = []
        y = 0
        for row in game_map:
            x = 0
            for tile in row:
              if tile == '1':
                tela.blit(dirt_image, ( x * tile_size+screen_scroll, y * tile_size))
              if tile == '2':
                tela.blit(grass_image, (x * tile_size+screen_scroll, y * tile_size))
              if tile == '3':
                tela.blit(rockdirt_image, (x * tile_size+screen_scroll, y * tile_size))
              if tile == '4':
                tela.blit(sand_image, (x * tile_size+screen_scroll, y * tile_size))
              if tile == '5':
                tela.blit(snow_image, (x * tile_size+screen_scroll, y * tile_size))
              if tile == '6':
                tela.blit(rock_image, (x * tile_size+screen_scroll, y * tile_size))
              if tile == '14':
                tela.blit(water_image, (x * tile_size+screen_scroll, y * tile_size))
              if tile == '15':
                tela.blit(waterf_image, (x * tile_size+screen_scroll, y * tile_size))
              if tile == '16':
                tela.blit(lava_image, (x * tile_size+screen_scroll, y * tile_size))
                #lava_group.add()
              if tile == '17':
                tela.blit(lavaf_image, (x * tile_size+screen_scroll, y * tile_size))              
              if tile == '20':
                tela.blit(signexit_image, (x * tile_size+screen_scroll, y * tile_size))
              if tile == '21':
                tela.blit(signr_image, (x * tile_size+screen_scroll, y * tile_size))
              if tile == '22':
                tela.blit(signl_image, (x * tile_size+screen_scroll, y * tile_size))
               
              if (tile<'7')and(tile!='0') and (tile !='16') and (tile != '17'):
                tile_rects.append(pygame.Rect(x * tile_size+screen_scroll, y * tile_size, tile_size, tile_size))

              if (tile=='16')or(tile=='17'):
                tile_lava.append(pygame.Rect(x * tile_size+screen_scroll, y * tile_size, tile_size, tile_size))
              x += 1
            y += 1

        clock.tick(fps)
        
        player.update_animation()  #faz o update a partir dos fps
        player.update()
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