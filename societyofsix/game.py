import arcade
from societyofsix import constants as c
from societyofsix import utilities, sprites

class Game(arcade.Window):
    """ main application class, initiates window """
    def __init__(self):
        super().__init__(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, "Society of Six")
        self.done = False
        
        # debugging properties
        self.fps = utilities.FPSCounter()
        self.debug = False
        # sprite lists
        self.spritelist_player = None

        # player
        self.sprite_player = None

    def setup(self):
        """
        Setup the game, create sprites and other game items.
        Seperated from initialisation logic so that it can be called to restart. 
        """
        # Setup the background
        arcade.set_background_color((255,255,255))
        # Setup Sprite lists
        self.spritelist_player = arcade.SpriteList()
        
        # Setup the player sprite
        self.sprite_player = sprites.Player(c.SPRITE_PLAYER_FILE, c.SPRITE_SCALE)
        self.sprite_player.center_x = 50
        self.sprite_player.center_y = 50
        self.spritelist_player.append(self.sprite_player)

    def update(self, delta_time):
        if not self.done:
            self.spritelist_player.update()

    def on_draw(self):
        arcade.start_render()
        # call list draw methods here
        self.sprite_player.draw()

        if self.debug:
            """ debuging information """
            arcade.draw_text(
                "FPS: {}".format(self.fps.get_fps()),
                20,
                c.SCREEN_HEIGHT - 20,
                (0,0,0),
                12
        )

    def on_key_press(self, key, modifiers):
        if key == arcade.key.Q:
            arcade.close_window()
        if key == arcade.key.F:
            if self.debug == False:
                self.debug = True
            else:
                self.debug = False