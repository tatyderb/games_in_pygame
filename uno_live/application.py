import pygame

from uno_live.card import Card
from uno_live.card_view import CardView
from uno_live.data import GEOM, RSC

FPS = RSC['FPS']


class GameView:
    def __init__(self, size: (int, int)):
        self.size = (self.width, self.height) = size
        self.cv = CardView(Card('red', 4), 10, 50)

    def redraw(self, display: pygame.Surface):
        display.fill((0, 81, 44), (0, 0, self.width, self.height))
        self.cv.redraw(display)
        pygame.display.update()

    def event_process(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # нажата левая кнопка
            # 0 - 1 - 2
            # 0 - 1 - 2 - 3 - 4
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if self.cv.r().collidepoint(x, y):
                    self.cv.flip()


class Application:
    def __init__(self):
        pygame.init()
        size = GEOM['display']
        self.display = pygame.display.set_mode(size)
        pygame.display.set_caption(RSC['title'])
        # icon_img = pygame.image.load(RSC['img']['icon'])
        # pygame.display.set_icon(icon_img)

        self.game_view = GameView(size)

        #self.game = UnoGame()
        #self.game.init(['Me', 'Bob', 'Charley'])
        #self.game_view = GameView(size, self.game)

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            #model_update()
            self.game_view.redraw(self.display)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.game_view.event_process(event)

            clock.tick(FPS)     # ждать 1/FPS секунды


app = Application()
app.run()
