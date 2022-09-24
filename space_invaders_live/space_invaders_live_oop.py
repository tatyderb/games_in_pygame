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


class Game:
    def __init__(self, size):
        pass

    def model_update(self):
        pass

    def redraw(self, display):
        pass

    def event_process(self):
        pass


class Application:
    def __init__(self):
        pygame.init()
        # self.width = 800
        # self.height = 600
        # tuple
        self.size = (self.width, self.height) = (800, 600)
        self.display = pygame.display.set_mode(self.size)
        pygame.display.set_caption(RSC['title'])
        icon_img = pygame.image.load(RSC['img']['icon'])
        pygame.display.set_icon(icon_img)

    def run(self):
        running = True
        game = Game(self.size)
        while running:
            game.model_update()
            game.redraw(self.display)
            for event in pygame.event.get():
                if self.event_close_application(event):
                    running = False
                game.event_process()

    def event_close_application(self, event):
        return event.type == pygame.QUIT


app = Application()
app.run()
