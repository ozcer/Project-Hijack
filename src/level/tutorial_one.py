from src.const import *
from src.game_objects.dynamic.player import Player
from src.game_objects.interactible.goal import Goal
from src.game_objects.interactible.warp_consumable import WarpConsumable
from src.game_objects.terrain.background_block import BackgroundBlock
from src.game_objects.terrain.ground import Ground
from src.level.level import Level


class TutorialOne(Level):
    
    def __init__(self, game):
        name = "Make Space If There Is None"
        super().__init__(game, name=name)
    
    def build(self):
        player = Player(self.game, pos=(200, 900), warp_charges=0)
        self.game.add_entity(player, "one")
        self.game.camera.follow(player)
        bottom_left_pos = (0, 1000)
        room_width = 12
        room_height = 5
    
        block_at = 7
    
        # Floor
        block_pos = build_row(Ground, self.game, bottom_left_pos, block_at)
        bottom_right_pos = build_row(Ground, self.game, block_pos, room_width - block_at + 1)
    
        # Left Guard
        top_left_pos = build_column(Ground, self.game, bottom_left_pos, room_height, reverse=True)
        # Right Guard
        build_column(Ground, self.game, bottom_right_pos, room_height, reverse=True)
    
        # Ceiling
        top_right_pos = build_row(Ground, self.game, top_left_pos, room_width)
    
        # Background
        build_array(BackgroundBlock, self.game, top_left_pos, (room_width, room_height), world="three")
    
        # blockade
        build_column(Ground, self.game, block_pos, room_height, reverse=True, world="one")
    
        # warp charge
        pos = get_end_pos(Ground, block_pos, (3, room_height - 2), xreverse=True, yreverse=True)
        charge = WarpConsumable(self.game, pos=pos)
        self.game.add_entity(charge)
    
        # goal
        pos = get_end_pos(Ground, bottom_right_pos, (2, 2), xreverse=True, yreverse=True)
        goal = Goal(self.game, pos=pos)
        self.game.add_entity(goal)