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
        'background': 'audio/background.wav',
        'explosion': 'audio/explosion.wav',
        'laser': 'audio/laser.wav',
        'endless_big': 'audio/Time-to-Spare-An-Jone.wav'
    },
    'font': {

    }
}


class Game:
    def __init__(self, display_size):
        pass

    def model_update(self):
        pass

    def redraw(self, display):
        pass

    def event_process(self, event):
        pass


class Application:
    def __init__(self):
        pygame.init()
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
                if event.type == pygame.QUIT:
                    running = False
                game.event_process(event)

Application().run()
