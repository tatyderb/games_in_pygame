import pygame

RSC = {
    'title': 'Space Invaders',
    'img': {
        'background': 'resources/img/background.png',
        'icon': 'resources/img/ufo.png',
        'player': 'resources/img/player.png',
        'enemy': 'resources/img/enemy.png',
        'bullet': 'resources/img/bullet.png'
    },
    'sound': {
    }
}

FPS = 60


class Game:
    def __init__(self):
        pass

    def model_update(self):
        pass

    def redraw(self):
        pass

    def event_process(self, event):
        pass


class Application:
    def __init__(self):
        pygame.init()

        self.width = 800
        self.height = 600
        self.size = (self.width, self.height)

        self.display = pygame.display.set_mode(self.size)
        pygame.display.set_caption(RSC['title'])
        pygame.display.set_icon(pygame.image.load(RSC['img']['icon']))

        self.running = False

    def run(self):
        # приложение уже запущено
        if self.running:
            return
        self.running = True
        clock = pygame.time.Clock()

        game = Game()

        while self.running:
            game.model_update()
            game.redraw()
            for event in pygame.event.get():
                if self.event_close_application(event):
                    self.running = False
                game.event_process(event)
                clock.tick(FPS)

    def event_close_application(self, event):
        return event.type == pygame.QUIT


app = Application()
app.run()
