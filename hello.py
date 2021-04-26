import pygame
import os
import random
#import button

game_map = [['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','0','0','0','0','2','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','21','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','20','0','2','2','2','21','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','20','0','2','2','2','1','1','1','1','1','1','1','1','1','17','17','1','1','1','1','1','1','1','1','1','1''1','1','1','1','1','1','1','1','1','17','17','1','1','1','1','1','1','1','1','1','1'],
           ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','1','1','1','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','1','1','1'],
           ['1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','1','1','1','1','1'],
           ['1','1','2','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','2','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1'],
           ['1','1','1','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1'],
           ['1','1','1','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','2','2','16','16','2','1','1','1','1','1','1','1','1','1'],
           ['1','1','1','2','2','2','2','2','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','2','2','2','2','2','1','1','17','17','1','1','1','1','1','1','1','1','1','1'],
           ['1','1','1','1','1','1','1','1','1','1','17','17','1','1','1','1','1','1','1','1','1','1''1','1','1','1','1','1','1','1','1','17','17','1','1','1','1','1','1','1','1','1','1']]

game_map2 = [['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','0','0','0','0','0','0','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','0','0','0','0','0','0','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','0','0','0','0','0','0','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','0','0','0','0','2','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','21','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','20','0','2','2','2','21','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','20','0','2','2','2','1','1','1','1','1','1','1','1','1','17','17','1','1','1','1','1','1','1','1','1','1''1','1','1','1','1','1','1','1','1','17','17','1','1','1','1','1','1','1','1','1','1'],
           ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','1','1','1','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','1','1','1'],
           ['1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','1','1','1','1','1'],
           ['1','1','2','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','2','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1'],
           ['1','1','1','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1'],
           ['1','1','1','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','2','2','16','16','2','1','1','1','1','1','1','1','1','1'],
           ['1','1','1','2','2','2','2','2','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','2','2','2','2','2','1','1','17','17','1','1','1','1','1','1','1','1','1','1'],
           ['1','1','1','1','1','1','1','1','1','1','17','17','1','1','1','1','1','1','1','1','1','1''1','1','1','1','1','1','1','1','1','17','17','1','1','1','1','1','1','1','1','1','1']]

game_map3 = [['1','0','1','1','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','0','1','0','0','1','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','0','1','1','1','1','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','0','1','0','1','1','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','0','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','0','0','0','0','0','0','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','0','0','0','0','0','0','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','0','0','0','0','2','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0'],
           ['1','21','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','20','0','2','2','2','21','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','20','0','2','2','2','1','1','1','1','1','1','1','1','1','17','17','1','1','1','1','1','1','1','1','1','1''1','1','1','1','1','1','1','1','1','17','17','1','1','1','1','1','1','1','1','1','1'],
           ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','1','1','1','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','1','1','1'],
           ['1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','1','1','1','1','1'],
           ['1','1','2','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','2','0','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1'],
           ['1','1','1','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','2','1','1','1','1','1','1','1','1'],
           ['1','1','1','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','2','2','16','16','2','1','1','1','1','1','1','1','1','1'],
           ['1','1','1','2','2','2','2','2','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','2','2','2','2','2','1','1','17','17','1','1','1','1','1','1','1','1','1','1'],
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

#Imagem do botão restart
#restart_image = pygame.image.load('Imagens/Outros/Restart.png')


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

    def draw_bg():
      if level==1:
        width=sky_image.get_width()
        for x in range(5):
          tela.blit(sky_image, ((x*width)-bg_scroll*0.5,0))
          tela.blit(mountain_image, ((x*width)-bg_scroll*0.6,100))
          tela.blit(pine1_image, ((x*width)-bg_scroll*0.7,230))
          tela.blit(pine2_image, ((x*width)-bg_scroll*0.8,290))
      if level==2:
        width=sky_image.get_width()
        for x in range(5):
          tela.blit(sky_image, ((x*width)-bg_scroll*0.5,0))
          tela.blit(mountain_image, ((x*width)-bg_scroll*0.6,100))
          tela.blit(pine1_image, ((x*width)-bg_scroll*0.7,230))
          tela.blit(pine2_image, ((x*width)-bg_scroll*0.8,290))
      if level==3:
        width=sky_image.get_width()
        for x in range(5):
          tela.blit(sky_image, ((x*width)-bg_scroll*0.5,0))
          tela.blit(mountain_image, ((x*width)-bg_scroll*0.6,100))
          tela.blit(pine1_image, ((x*width)-bg_scroll*0.7,230))
          tela.blit(pine2_image, ((x*width)-bg_scroll*0.8,290))
    
    ##Função para resetar o nível!
    #def reset_level():
    #  
    #  #criar uma lista vazia do mundo
    #  game_map=[]

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
    passagem=False

    #Funções para jogador
    class PP(pygame.sprite.Sprite):
        def __init__(self, char_type, x, y, scale, speed):
                    pygame.sprite.Sprite.__init__(self)
                    self.alive = True
                    self.speed=speed
                    self.char_type = char_type
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
                        img1 = pygame.image.load(f"Imagens/{char_type}/{i}.png")
                        img1 = pygame.transform.scale(img1, (int(img1.get_width() * scale), int(img1.get_height() * scale)))
                        temp_list.append(img1)
           
                    self.animation_list.append(temp_list)
                    temp_list=[]
                    #Aqui é feito animação do personagem parado(flip de imagens)
                    for i in range(1):
                        img1 = pygame.image.load(f"Imagens/{self.char_type}-Parado/{i}.png")
                        img1 = pygame.transform.scale(img1, (int(img1.get_width() * scale), int(img1.get_height() * scale)))
                        temp_list.append(img1)
                    self.animation_list.append(temp_list)
                    self.image= self.animation_list[self.action][self.frame_index]
                    self.rect = self.image.get_rect()
                    self.rect.center = (x, y)
                    self.width=self.image.get_width()
                    self.height=self.image.get_height()
                    
                    #AI Variaveis
                    self.move_counter=0
                    self.idling=False
                    self.idling_counter=0

        def update(self):
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


            if self.char_type=='Personagem':
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

            if self.char_type=='Professor':            
             for g in range(200):
                 #check collision in the x direction
                 if tile_rects_ini[g].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                     dx = 0
                 #check for collision in the y direction
                 if tile_rects_ini[g].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                     #check if below the ground, i.e. jumping
                     if self.vel_y < 0:
                         self.vel_y = 0
                         dy = tile_rects[g].bottom - self.rect.top
                     #check if above the ground, i.e. falling
                     elif self.vel_y >= 0:
                         self.vel_y = 0
                         self.in_air = False
                         dy = tile_rects[g].top - self.rect.bottom
          
            #Checagem Lava -- Mudei a condição do arthur um puco
            if self.char_type=='Personagem':
               for g in range(10):
                   #check collision in the x direction
                   if tile_lava[g].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                       dx = 0
                       self.health=0
                   #check for collision in the y direction
                   if tile_lava[g].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                       dy=0
                       self.health=0
               if self.rect.y>650:
                 self.health=0
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

        def ai(self):
          if player.alive:
            if self.idling==False and random.randint(1, 200)==1:
              self.update_action(1)
              self.idling=True
              self.idling_counter=50
            if self.idling==False:
              if self.direction==1:
                ai_moving_right=True
              else:
                ai_moving_right=False
              ai_moving_left=not ai_moving_right
              self.move(ai_moving_left,ai_moving_right)
              self.move_counter += 1 
              self.update_action(0)
              
              if self.move_counter >tile_size:
                self.direction*= -1
                self.move_counter*=-1
            else:
              self.idling_counter -= 1
              if self.idling_counter <=0:
                self.idling=False

        def draw(self):
            tela.blit(pygame.transform.flip(self.image, self.flip, False),(self.rect.x,self.rect.y))

        def drawAI(self):
            tela.blit(pygame.transform.flip(self.image, self.flip, False),(self.rect.x+screen_scroll,self.rect.y))

    #Jogador - Chamar
    player=PP('Personagem',300,0,1.8,5)

    #inimigos LEVEL1 - chamar
    inimigo=PP('Professor',300,500,1.8,4)
    inimigo2=PP('Professor',900,200,1.8,4)

    sair=False
    #Estrutura para fechar jogo
    while sair==False:
    
        #ScreenScrool dinâmica
        if (player.rect.right > 390):
          player.rect.x -= player.speed
          screen_scroll += - player.speed
          bg_scroll -= - player.speed
        if (player.rect.right < 280):
          player.rect.x += player.speed
          screen_scroll -= - player.speed
          bg_scroll += - player.speed

        #Troca de MAPA de acordo com o nível
        if level==1:
          variavel=game_map
        if level==2:
          variavel=game_map2
        if level==3:
          variavel=game_map3
        
        #Leitura dos NIVEIS
        draw_bg()
        tile_rects = []
        tile_lava = []
        tile_rects_ini = []
        tile_rects_placa=[]
        y = 0
        for row in variavel:
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
              if tile == '17':
                tela.blit(lavaf_image, (x * tile_size+screen_scroll, y * tile_size))              
              if tile == '20':
                tela.blit(signexit_image, (x * tile_size+screen_scroll, y * tile_size))
              if tile == '21':
                tela.blit(signr_image, (x * tile_size+screen_scroll, y * tile_size))
              if tile == '22':
                tela.blit(signl_image, (x * tile_size+screen_scroll, y * tile_size))
              #TileRect Append
              if (tile == '1')or(tile == '2')or(tile == '3')or(tile == '4')or(tile == '5')or(tile == '6'):
                tile_rects.append(pygame.Rect(x * tile_size+screen_scroll, y * tile_size, tile_size, tile_size))
              #TileLava Append
              if (tile=='17'):
                tile_lava.append(pygame.Rect(x * tile_size+screen_scroll, y * tile_size, tile_size, tile_size))
              #TileInimigos Append
              if (tile == '1')or(tile == '2')or(tile == '3')or(tile == '4')or(tile == '5')or(tile == '6'):
                tile_rects_ini.append(pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size))
              #placa Passa missão
              if (tile=='21'):
                tile_rects_placa.append(pygame.Rect(x * tile_size+screen_scroll, y * tile_size, tile_size, tile_size))
              x += 1
            y += 1

        #inimigos do LEVEL 1
        if level==1:
          inimigo.update_animation()
          inimigo.ai()
          inimigo.drawAI()

          inimigo2.update_animation()
          inimigo2.ai()
          inimigo2.drawAI()

        #JOGADOR
        player.update_animation()  #faz o update a partir dos fps
        player.update()
        player.draw()              #chama jogador

        #TROCA LEVELS
        for g in range(2):
           #check collision in the x direction
           if tile_rects_placa[g].colliderect(player.rect.x, player.rect.y, player.width, player.height):
              screen_scroll=0
              bg_scroll=0
              passagem=True
           #check for collision in the y direction
           if tile_rects_placa[g].colliderect(player.rect.x, player.rect.y, player.width, player.height):
              passagem=True
              screen_scroll=0
              bg_scroll=0
 
        if passagem==True:
          level +=1
          passagem=False
                
        print(player.health) 

        #CHOQUE Com Inimigos

        if inimigo.rect.colliderect(player.rect.x, player.rect.y, player.width, player.height):
              player.health=0        


        #Teste Nivel
        if player.alive:
            if moving_left or moving_right:
                player.update_action(0)
            else: 
                player.update_action(1)
            player.move(moving_left,moving_right)

        #FPS
        clock.tick(fps)

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