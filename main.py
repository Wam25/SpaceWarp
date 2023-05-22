import pyxel
import json
from player import Player
from rooms import Room

class App:
    def __init__(self):
        self.gamestate = 0
        self.player = Player(0, 48, 0)
        self.current_screen = 0
        self.offset_x = 0
        self.load_mask('ressources/mask.json')
        
        pyxel.init(128, 128, title='SpaceWarp')
        pyxel.load("ressources/assets.pyxres")
        pyxel.run(self.update, self.draw)
        
    def load_mask(self, file_name):
        with open(file_name, 'r') as file:
            mask = json.load(file)
            self.rooms = [Room(i) for i in mask]

    def update(self):
        if pyxel.btn(pyxel.KEY_S):
            self.gamestate = 1

        if self.gamestate == 0:
            return

        self.player.move(self.rooms[self.current_screen], self.current_screen)
        self.update_screen_position()
        self.rooms[self.current_screen].update_room(self.player.x, self.player.y)
        
        if self.player.alive == 0:
            self.player.reset(self.rooms[self.current_screen].spawn_x, self.rooms[self.current_screen].spawn_y)
            self.player.alive = 1

    def update_screen_position(self):
        if self.player.x == 124:
            self.offset_x += 128
            self.current_screen += 1
            self.player.x -= 128
            # self.player.y -= 2
            self.rooms[self.current_screen].spawn_x = self.player.x + 4
            self.rooms[self.current_screen].spawn_y = self.player.y
        elif self.player.x == -5 and self.current_screen != 0:
            self.offset_x -= 128
            self.current_screen -= 1
            self.player.x += 128
            # self.player.y -= 2
            self.rooms[self.current_screen].spawn_x = self.player.x - 4
            self.rooms[self.current_screen].spawn_y = self.player.y


    def draw(self):
        if self.gamestate == 0:
            pyxel.cls(0)
            pyxel.bltm(0, 0, 0, 0, 0, 128, 128)
            pyxel.text(42, 64, '(S)tart', 7)
        else:
            pyxel.cls(0)
            pyxel.bltm(0, 0, 2, self.offset_x, 0, 128, 128)
            self.rooms[self.current_screen].draw_room()
            self.player.draw_player()

App()