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
        while running:

            for event in pygame.event.get():
                if self.event_close_application(event):
                    running = False

    def event_close_application(self, event):
        return event.type == pygame.QUIT


app = Application()
app.run()
