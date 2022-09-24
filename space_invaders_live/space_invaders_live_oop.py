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


class Player:
    YGAP = 10
    SPEED = 0.5

    def __init__(self, display_size):
        self.bound_size = self.bound_width, self.bound_height = display_size
        self.img = pygame.image.load(RSC['img']['player'])
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = self.bound_width // 2 - self.width // 2
        self.y = self.bound_height - self.height - self.YGAP
        self.dx = 0

    def model_update(self):
        self.x += self.dx
        # не дадим игроку выходить за пределы окна
        if self.x < 0:
            self.x = 0
        if self.x > self.bound_width - self.width:
            self.x = self.bound_width - self.width

    def redraw(self, display):
        display.blit(self.img, (self.x, self.y))

    def event_process(self, event):
        # нажали клавишу
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.dx = -self.SPEED
            elif event.key == pygame.K_RIGHT:
                self.dx = self.SPEED
        # отпустили клавишу
        if event.type == pygame.KEYUP:
            self.dx = 0


class Game:
    def __init__(self, size):
        self.player = Player(size)

    def model_update(self):
        self.player.model_update()

    def redraw(self, display, size):
        width, height = size
        display.fill((0, 0, 0), (0, 0, width, height))
        self.player.redraw(display)
        pygame.display.update()

    def event_process(self, event):
        self.player.event_process(event)


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
            game.redraw(self.display, self.size)
            for event in pygame.event.get():
                if self.event_close_application(event):
                    running = False
                game.event_process(event)

    def event_close_application(self, event):
        return event.type == pygame.QUIT


app = Application()
app.run()
