import pygame



class Tile:
    Size = 32
    def Load_Texture(file, Size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (Size, Size))
        surface = pygame.Surface((Size, Size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap, (0,0))
        return surface

    Grass = Load_Texture("graphics\\grass-tile-3.png", Size)