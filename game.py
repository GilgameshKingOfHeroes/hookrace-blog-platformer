import sys
import sdl2.ext
from time import time
from sdl2.ext import Color, Renderer, Resources, Window
from basic2d import Point2d, Vector2d
from controller import Input, Controller
from stopwatch import Stopwatch
from player import Player
from tilemap import Map, Tile
# Objective 4: Import Player from player module
# YOUR CODE HERE...

# Objective 5: Import Map and Tile from tilemap module
# YOUR CODE HERE...


UPDATES_PER_SECOND = 50
SECONDS_PER_UPDATE = 1.0 / UPDATES_PER_SECOND
WINDOW_SIZE = (1600, 1100)
WINDOW_TITLE = "Jin's Brotherly Paradise"
# Objective 1: Create the title and size variables
# YOUR CODE HERE...


class Game:
    def __init__(self, resources: Resources) -> None:
        self.camera = Vector2d(0, 0)
        self.stopwatch = Stopwatch(resources)

        # Objective 4: Create a Player
        # YOUR CODE HERE...
        self.player=Player(resources)

        # Objective 5: Create a Map
        # YOUR CODE HERE...
        self.map=Map(resources)

    def update(self, controller: Controller) -> None:
        if controller.has_input(Input.RESTART):
            self.stopwatch.reset()

        # Objective 4: Put the player back at the start
        # YOUR CODE HERE...

        # Objective 6: Call the player update method
        # YOUR CODE HERE...

        # Objective 7: Call the move_camera function with a focus on the player position
        # YOUR CODE HERE...

        # Objective 8: Update the stopwatch according to the player tile
        # YOUR CODE HERE...

    def render(self, renderer: Renderer) -> None:
        # Objective 4: Render the player
        # YOUR CODE HERE...
        self.player.render(renderer, self.camera)

        # Objective 5: Render the tilemap
        # YOUR CODE HERE...
        self.map.render(renderer, self.camera)

        self.stopwatch.render(renderer)


def move_camera(camera: Vector2d, focus: Point2d) -> None:
    # Objective 7: Find the correct value for half the window width
    # YOUR CODE HERE...
    half_win_width = 0

    # Objective 7: Uncomment and try out the different camera movements

    #1. always in center:
    camera.x = focus.x - half_win_width

    # 2. follow once leaves center:
    # left_area = focus.x - half_win_width - 100
    # right_area = focus.x - half_win_width + 100
    # camera.x = min(max(camera.x, left_area), right_area)

    # 3. fluid
    # dist = camera.x - focus.x + half_win_width
    # camera.x -= 0.05 * dist


def main() -> int:
    sdl2.ext.init()
    resources = Resources(__file__, "resources")
    controller = Controller()

    window = Window(WINDOW_TITLE, WINDOW_SIZE)
    window.show()

    renderer = Renderer(window)
    color = Color(r=215, g=215, b=255)
    renderer.color = color


    # Objective 3: Set up the game
    # YOUR CODE HERE...
    game = Game(resources)

    # Game Loop, draws each frame
    last_time = time()
    lag = 0.0
    while True:
        now = time()
        lag += now - last_time
        last_time = now

        controller.handle_input()
        if controller.has_input(Input.QUIT):
            break

        while lag >= SECONDS_PER_UPDATE:
            lag -= SECONDS_PER_UPDATE
        # Objective 3: Update the game the appropriate number of frames
        # YOUR CODE HERE...

        renderer.clear()
        # Objective 3: Render the game
        # YOUR CODE HERE...
        game.render(renderer)

        renderer.present()
    sdl2.ext.quit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
