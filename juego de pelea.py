from typing import Any
from pygame import *
import random


class Jugador(sprite.Sprite):

    def __init__(self, nombre_jugador, imagen_jugador, jugador_x, jugador_y,velocidad, score): 
        sprite.Sprite.__init__(self)
        self.nombre = nombre_jugador
        self.imagen = transform.scale(image.load(imagen_jugador),(80,80))
        self.x = jugador_x
        self.y = jugador_y
        self.velocidad = velocidad
        self.score = score



        self.rect = self.imagen.get_rect()
        self.rect.x = jugador_x
        self.rect.y = jugador_y



    def move(self, dx, dy):

        self.rect.x += dx * self.velocidad

        self.rect.y += dy * self.velocidad

    def reset(self):
        window.blit(self.imagen,(self.rect.x, self.rect.y))


class Heroe(Jugador):
    def update(self):
        keys = key.get_pressed()
                #UP
        if keys[K_w] and self.rect.y > 5:
            self.move(0, -1)
                #DOWN
        if keys[K_s] and self.rect.y < wind_height - 80:
            self.move(0, 1)
                #RIGHT
        if keys[K_d]  and self.rect.x < wind_width - 80:
            self.move(1, 0)
                #LEFT
        if keys[K_a] and self.rect.x > 5:
            self.move(-1, 0)



class Enemigo(Jugador):

    def update(self):

        dx = random.choice([-5,5])
        dy = random.choice([-5,5])
        self.move(dx, dy)
        






all_sprites = sprite.Group()
enemies = sprite.Group()    


wind_width = 700
wind_height = 500
window = display.set_mode((wind_width,wind_height))
display.set_caption("Mortal Kombat en maquinitas")
background = transform.scale(image.load("C:/Users/Sotomayor/Downloads/mapa.png"),(700,500))
SubZero = Heroe("SubZero", "C:/Users/Sotomayor/a/93564-subzero-profession-ii-mythologies-costume-mortal-kombat.png", 5, wind_height -80, 20, 0)
Scorpion = Enemigo("Scorpion","C:/Users/Sotomayor/a/Scorpiontobias.png", wind_width -80, 200 , 20, 0)


all_sprites.add(SubZero, Scorpion)
enemies.add(Scorpion)

clock = time.Clock()
FPS = 100
run = True

player_turn = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.fill((0, 0, 0))
    
    window.blit(background,(wind_width,wind_height))


    all_sprites.update()
   

    hits = sprite.spritecollide(SubZero, enemies, False)


    if hits:
        print("¡Colisión entre el jugador y el enemigo!")
        if player_turn:
            SubZero.score += 1
        else:
            Scorpion.score += 1
        player_turn = not player_turn



    all_sprites.draw(window)
    display.flip()
    clock.tick(FPS)


print(f"Puntaje del jugador: {SubZero.score}")
print(f"Puntaje del enemigo: {Scorpion.score}")


   
