import pygame
from setting import Setting
from position import Position
from colors import Colors

class Block:
    def __init__(self,id):
        self.setting = Setting()
        self.id = id
        self.cells = {}
        self.row_offset = 0
        self.colume_offset = 0
        self.rotation_state = 0
        self.cell_size = self.setting.cell_size
        self.colors = Colors.get_cell_colors()

    def move(self, row, colume):
        self.row_offset += row
        self.colume_offset += colume

    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotate(self):
        self.rotation_state -= 1
        if self.rotation_state == - 1:
            self.rotation_state = len(self.cells) - 1

    def get_cell_position(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.colume + self.colume_offset)
            moved_tiles.append(position)

        return moved_tiles

    def draw(self,screen, offset_x, offset_y):
        tiles = self.get_cell_position()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.colume * self.cell_size + offset_x, tile.row * self.cell_size + offset_y, self.cell_size -1, self.cell_size -1)
			
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
        

    