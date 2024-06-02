import pygame
import pypboy
import config

from pypboy.modules.data import entities

class Module(pypboy.SubModule):

    label = "World Map"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mapgrid = entities.Map(480, pygame.Rect(0, 0, config.WIDTH - 8, config.HEIGHT - 80))
        mapgrid.fetch_map(config.MAP_FOCUS, 0.01)
        self.add(mapgrid)
        mapgrid.rect[0] = 4
        mapgrid.rect[1] = 40

    def handle_resume(self):
        self.parent.pypboy.header.headline = "DATA"
        self.parent.pypboy.header.title = "Belfast City"
        super().handle_resume()
