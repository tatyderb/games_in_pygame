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


class Enemy:
    DEFAULT_DX = 0
    DEFAULT_DY = 0.1
    DEFAULT_Y = 30

    def __init__(self, display_size):
        self.bound_size = self.bound_width, self.bound_height = display_size
        self.img = pygame.image.load(RSC['img']['enemy'])
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x, self.y, self.dx, self.dy = self.create_at_random_position()
        # self.x, self.y, self.dx, self.dy = self.create_at_center()

    def create_at_center(self):
        x = self.bound_width // 2 - self.width // 2
        y = self.DEFAULT_Y
        dx = self.DEFAULT_DX
        dy = self.DEFAULT_DY
        return x, y, dx, dy

    def create_at_random_position(self):
        x = random.randint(0, self.bound_width)
        y = self.DEFAULT_Y
        dx = random.randint(-2, 3) / 10
        dy = random.randint(1, 3) / 20
        return x, y, dx, dy

    def model_update(self):
        self.x += self.dx
        self.y += self.dy

    def into_bounds(self):
        bound = pygame.Rect(0, 0, self.bound_width, self.bound_height)
        return bound.contains(self.x, self.y, self.width, self.height)

    def redraw(self, display):
        display.blit(self.img, (self.x, self.y))


class Bullet:
    def __init__(self):


class Game:
    def __init__(self, size):
        self.size = size
        self.player = Player(size)
        self.enemy = None
        self.bullet = None

    def model_update(self):
        self.player.model_update()

        if self.enemy is None:
            self.enemy = Enemy(self.size)
        self.enemy.model_update()
        if not self.enemy.into_bounds():       # если вышли за границу
            self.enemy = None

        if self.bullet:
            self.bullet.model_update()
            if not self.bullet.into_bounds():       # если вышли за границу
                self.bullet = None

    def redraw(self, display, size):
        width, height = size
        display.fill((0, 0, 0), (0, 0, width, height))
        self.player.redraw(display)
        if self.enemy:
            self.enemy.redraw(display)
        if self.bullet:
            self.bullet.redraw(display)
        pygame.display.update()

    def event_process(self, event):
        self.player.event_process(event)
        # обрабатываю события (пули может еще не быть, поэтому Bullet. метод не объекта, а класса)
        # может вернуть созданную пулю, если так, то ее сохраняем в self.bullet
        b = Bullet.event_process(event, self.player.size())
        if b:
            self.bullet = b


class Application:
    def __init__(self):
        random.seed(10) # убрать во время релиза
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
