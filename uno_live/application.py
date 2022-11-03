import pygame

from uno_live.data import GEOM, RSC

FPS = RSC['FPS']


class Application:
    def __init__(self):
        pygame.init()
        size = GEOM['display']
        self.display = pygame.display.set_mode(size)
        pygame.display.set_caption(RSC['title'])
        # icon_img = pygame.image.load(RSC['img']['icon'])
        # pygame.display.set_icon(icon_img)

        #self.game = UnoGame()
        #self.game.init(['Me', 'Bob', 'Charley'])
        #self.game_view = GameView(size, self.game)

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            #model_update()
            #redraw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(FPS)     # ждать 1/FPS секунды


app = Application()
app.run()
