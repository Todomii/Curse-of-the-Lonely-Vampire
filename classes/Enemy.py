from utils.pg import pg
from classes.Monster import Monster

class Enemy(pg.sprite.Sprite):
    def __init__(self, game, pos: (), monster : Monster, scale = 1) -> None:
        self.game = game
        self.monster = monster
        self.health_points = self.monster.health_points
        self.x = pos[0]
        self.y = pos[1]
        self.scale = scale
        witdth = self.monster.image.get_width()
        height = self.monster.image.get_height()
        self.image = pg.transform.scale(self.monster.image, (int(witdth * self.scale), int(height * self.scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)
        self.velX = 0
        self.velY = 0
        self.alive = True
        super().__init__(self.game.enemy_sprites)
        
    def reduce_health_points(self, value : int) -> None:
        self.health_points -= value
        if self.health_points <= 0:
            self.die()
        
    def draw(self) -> None:
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def die(self) -> None:
        self.alive = False
        self.game.enemy_sprites.remove(self)
        del self
        
    def update(self) -> None:
        pass