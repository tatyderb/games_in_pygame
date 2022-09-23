import pygame
import random

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

FPS = 24


class Enemy:
    Y_START_POSITION = 30

    def __init__(self, bound_size):
        self.display_width, self.display_height = bound_size
        self.bound_rect = pygame.Rect(0, 0, self.display_width, self.display_height)

        self.img = pygame.image.load(RSC['img']['enemy'])
        self.width = self.img.get_width()
        self.height = self.img.get_height()

        self.x = random.randint(0, self.display_width)
        self.y = self.Y_START_POSITION
        self.dx = random.randint(-2, 3) / 10
        self.dy = random.randint(1, 3) / 10

    def model_update(self):
        # return in_bounds status
        self.x += self.dx
        self.y += self.dy
        return self.bound_rect.contains(self.x, self.y, self.width, self.height)

    def redraw(self, display):
        display.blit(self.img, (self.x, self.y))

    def event_process(self, event):
        pass


class Player:
    GAP = 10  # расстояние до низа экрана
    SPEED = 0.5

    def __init__(self, bound_size):
        self.display_width, self.display_height = bound_size

        self.img = pygame.image.load(RSC['img']['player'])
        self.width = self.img.get_width()
        self.height = self.img.get_height()

        self.x = self.display_width // 2 - self.width // 2
        self.y = self.display_height - self.height - self.GAP
        self.dx = 0

    def model_update(self):
        self.x += self.dx
        # не дадим игроку выходить за пределы окна
        if self.x < 0:
            self.x = 0
        if self.x > self.display_width - self.width:
            self.x = self.display_width - self.width

    def redraw(self, display):
        display.blit(self.img, (self.x, self.y))

    def event_process(self, event):
        # нажали клавишу - поехали
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.dx = -Player.SPEED
            elif event.key == pygame.K_RIGHT:
                self.dx = Player.SPEED
        # отпустили клавишу - остановились
        if event.type == pygame.KEYUP:
            self.dx = 0


class Game:
    def __init__(self, size):
        self.width, self.height = size
        self.rect = (0, 0, self.width, self.height)

        self.player = Player(size)
        self.enemy = None

    def model_update(self):
        self.player.model_update()
        if self.enemy:
            if not self.enemy.model_update():
                # вылетел за границы
                self.enemy = None
        else:
            self.enemy = Enemy((self.width, self.height))

    def redraw(self, display):
        display.fill((0, 0, 0), self.rect)
        self.player.redraw(display)
        if self.enemy:
            self.enemy.redraw(display)

        pygame.display.update()

    def event_process(self, event):
        self.player.event_process(event)


class Application:
    def __init__(self):
        pygame.init()
        random.seed(10)

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

        game = Game(self.size)

        while self.running:
            game.model_update()
            game.redraw(self.display)
            for event in pygame.event.get():
                if self.event_close_application(event):
                    self.running = False
                game.event_process(event)
                clock.tick(FPS)

    def event_close_application(self, event):
        return event.type == pygame.QUIT


app = Application()
app.run()
