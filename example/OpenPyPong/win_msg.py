import my_engine.entity as ent
import my_engine.game as game
import my_engine.scene as parent_scene
import my_engine.screen_print as sp


class WinMsg(ent.Entity):
    def __init__(self, ent_type: str, game: "game.Game", parent_scene: "parent_scene.Scene") -> None:
        super().__init__(ent_type, game, parent_scene)

        self.set_image("media/images/background.png")
        self.set_x_position(0)
        self.set_y_position(0)

        # set title text
        self.title = sp.ScreenPrinter(game)
        self.title.set_font_size(28)
        self.title.set_font("media/font/retro_font.ttf")

        # set start text
        self.start_text = sp.ScreenPrinter(game)
        self.start_text.set_font_size(18)
        self.start_text.set_font("media/font/retro_font.ttf")

        # set exit text
        self.exit_text = sp.ScreenPrinter(game)
        self.exit_text.set_font_size(18)
        self.exit_text.set_font("media/font/retro_font.ttf")

    def draw(self):
        super().draw()
        self.title.print("You won!", x_pos=75, y_pos=40)
        self.start_text.print("Play again", x_pos=90, y_pos=100)
        self.exit_text.print("Return to title", x_pos=60, y_pos=130)
