from utils.pg import pg
from constants.images import sword_img

class Item:
    def __init__(self, name: str, description: str, durability: int, damage: int, range: int, cooldown: int, is_consumable: bool, amount: int, type = "Mele", image = sword_img) -> None:
        self.image = image
        self.name = name
        self.description = description
        self.durability_max = durability
        self.durability = durability
        self.damage = damage
        self.range = range
        self.cooldown = cooldown
        self.is_consumable = is_consumable
        self.amount = amount
        self.type = type
        self.last = pg.time.get_ticks()
        
    def reduce_durability(self, value: int) -> None:
        self.durability -= value
        