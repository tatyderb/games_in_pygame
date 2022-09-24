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
        'background': 'audio/background.wav',
        'explosion': 'audio/explosion.wav',
        'laser': 'audio/laser.wav',
        'endless_big': 'audio/Time-to-Spare-An-Jone.wav'
    },
    'font': {

    }
}


class Player:
    YGAP = 10           # расстояние между игроком и низом экрана
    SPEED = 0.5         # скорость игрока при движении

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

    def rect(self):
        return self.x, self.y, self.width, self.height


class Bullet:
    SPEED = 0.5     # скорость пули (абсолютная величина)

    def __init__(self, player_rect):
        self.img = pygame.image.load(RSC['img']['bullet'])
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        px, py, pw, ph = player_rect
        self.x = px + pw // 2 - self.width // 2
        self.y = py - self.height
        self.dy = -Bullet.SPEED

    def model_update(self):
        self.y += self.dy

    def redraw(self, display):
        display.blit(self.img, (self.x, self.y))

    def rect(self):
        return self.x, self.y, self.width, self.height

    @staticmethod
    def fire(event):
        """ Return True, if press FIRE!!! button. """
        if event.type == pygame.MOUSEBUTTONDOWN:
            key = pygame.mouse.get_pressed()
            if key[0]:
                return True
        return False


class Enemy:
    DEFAULT_DX = 0
    DEFAULT_DY = 0.1
    DEFAULT_Y = 30

    def __init__(self, display_size):
        self.bound_size = self.bound_width, self.bound_height = display_size
        self.img = pygame.image.load(RSC['img']['enemy'])
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        # self.x, self.y, self.dx, self.dy = self.create_at_random_position()
        self.x, self.y, self.dx, self.dy = self.create_at_center()

    def rect(self):
        return self.x, self.y, self.width, self.height

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

    def redraw(self, display):
        display.blit(self.img, (self.x, self.y))


class Game:
    def __init__(self, display_size):
        self.display_size = display_size
        w, h = self.display_size
        self.bound_rect = pygame.Rect(0, 0, w, h)
        self.player = Player(display_size)
        self.bullet = None
        self.enemy = None

    def model_update(self):
        self.player.model_update()
        if self.bullet:
            # если пуля есть, надо ее двигать
            self.bullet.model_update()
            if not self.in_bound(self.bullet.rect()):
                # если пуля вылетела за границы экрана, удаляем ее
                self.bullet = None

        if self.enemy is None:
            # если врага нет, его надо сделать
            self.enemy = Enemy(self.display_size)
        self.enemy.model_update()
        if not self.in_bound(self.enemy.rect()):
            # если враг вылетел за экран, он исчез
            self.enemy = None

        # enemy - bullet
        if self.intersection(self.enemy, self.bullet):
            self.enemy = None
            self.bullet = None

    def redraw(self, display):
        # заливаем фон
        display.fill((0, 0, 0), self.bound_rect)
        # рисуем игровые элементы
        self.player.redraw(display)
        if self.bullet:
            self.bullet.redraw(display)
        if self.enemy:
            self.enemy.redraw(display)
        # запрашиваем обновление экрана
        pygame.display.update()

    def event_process(self, event):
        self.player.event_process(event)
        if Bullet.fire(event) and self.bullet is None:
            self.bullet = Bullet(self.player.rect())

    def in_bound(self, rect):
        """Возвращает True если rect в границах экрана"""
        return self.bound_rect.contains(rect)

    @staticmethod
    def intersection(orect1, orect2):
        if orect1 is None or orect2 is None:
            return False
        return pygame.Rect(orect1.rect()).colliderect(orect2.rect())


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
