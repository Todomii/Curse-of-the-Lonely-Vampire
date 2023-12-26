from utils.pg import pg
from utils.build_map import build_map
from config.keybinds import *
from constants.backgrounds import background
from classes.CameraGroup import CameraGroup

class Play:
    def __init__(self, game, tilemap : [], camera : CameraGroup) -> None:
        self.game = game
        self.tilemap = tilemap
        self.camera = camera
        self.player = None
        self.enemies = []
        self.create_tilemap()
        
    def run_play(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game.exit_game()
            if event.type == pg.KEYDOWN:
                if event.key == INVENTORY_KEY:
                    self.game.show_inventory()
                if event.key == pg.K_ESCAPE:
                    self.game.pause_game()
                    
    def draw_play(self) -> None:
        self.game.screen.blit(background, (0,0))
        enemies_within_range = filter(lambda enemy: pg.math.Vector2(self.player.x, self.player.y).distance_to((enemy.x, enemy.y)) < self.player.character.equipped.range * 100 and enemy.alive, self.enemies)
        self.player.custom_update(list(enemies_within_range))
        self.camera.update()
        self.camera.custom_draw(self.player)
        
    def create_tilemap(self) -> None:
        build_map(self)