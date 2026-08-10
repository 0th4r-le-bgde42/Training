from pyray import *
import random
import math
from pyray import Texture

class ParticuleCoeur:
    def __init__(self, x: float, y: float, source_rect: Rectangle, texture: Texture2D):
        self.pos_x = x
        self.pos_y = y
        self.source_rect = source_rect  # La zone du cœur original à copier
        self.texture = texture
        
        # Physique de l'explosion
        angle = random.uniform(0, 2 * math.pi)
        vitesse = random.uniform(1.0, 4.0)
        self.vel_x = math.cos(angle) * vitesse
        self.vel_y = math.sin(angle) * vitesse - random.uniform(1.0, 3.0) # Un petit élan vers le haut (gravité style)
        
        # Durée de vie et transparence
        self.alpha = 1.0
        self.vitesse_disparition = random.uniform(0.01, 0.03)

    def update(self) -> bool:
        """Met à jour la particule. Retourne False si elle est morte."""
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.vel_y += 0.15 # Gravité qui fait retomber les morceaux
        
        self.alpha -= self.vitesse_disparition
        return self.alpha > 0.0

    def draw(self) -> None:
        # On applique la transparence sur la particule
        couleur = fade(PURPLE, self.alpha)
        # On dessine le petit morceau de texture
        dest_rect = Rectangle(self.pos_x, self.pos_y, self.source_rect.width, self.source_rect.height)
        draw_texture_pro(self.texture, self.source_rect, dest_rect, Vector2(0, 0), 0.0, couleur)


class GestionnaireParticules:
    def __init__(self):
        self.particules = []

    def declencher_explosion(self, x: float, y: float, texture: Texture2D) -> None:
        """Découpe la texture en une grille de particules et les propulse."""
        # Nombre de morceaux horizontaux et verticaux (plus c'est haut, plus c'est fin)
        decoupe_x = 8
        decoupe_y = 8
        
        part_width = texture.width / decoupe_x
        part_height = texture.height / decoupe_y

        for i in range(decoupe_x):
            for j in range(decoupe_y):
                # Définir le rectangle source dans le fichier image
                source_rect = Rectangle(i * part_width, j * part_height, part_width, part_height)
                # Position de départ à l'écran
                spawn_x = x + (i * part_width)
                spawn_y = y + (j * part_height)
                
                self.particules.append(ParticuleCoeur(spawn_x, spawn_y, source_rect, texture))

    def update_and_draw(self) -> None:
        """Met à jour et dessine toutes les particules actives."""
        # On filtre pour ne garder que les particules vivantes
        self.particules = [p for p in self.particules if p.update()]
        
        for p in self.particules:
            p.draw()
class T():
    def __init__(self):
        self.heart = load_image("heart.png")
        image_resize(self.heart, 100, 100)
        self.texture_heart = load_texture_from_image(self.heart)
        unload_image(self.heart)
        self.x = int(width / 2)
        self.y = int(height / 2)

width = 2000
height = 1000

init_window(width, height, "CAMERA 2D")

set_target_fps(60)

test = T()

g =GestionnaireParticules()
boom = False

while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    if is_key_pressed(KEY_Q):
        g.declencher_explosion(test.x, test.y, test.texture_heart)
        boom = True

    # if boom is True:
    g.update_and_draw()
    draw_texture(test.texture_heart, test.x, test.y, PURPLE)

    end_drawing()

close_window()