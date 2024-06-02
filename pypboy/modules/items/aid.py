import pypboy
import pygame
import game
import config

class Module(pypboy.SubModule):

    label = "Aid"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)