import pygame
from setting import Setting

class Block:
    def __init__(self,id):
        self.setting = Setting()
        self.id = id
        self.cell = {}
        self.cell_size = self.setting.cell_size
        

    