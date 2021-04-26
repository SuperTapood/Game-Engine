## FLAPPY BIRD ##
## ENGINE TEST PASSED ##
## AVERAGE SPF (Seconds Per Frame) - 0.004126925945281982 ##
## ABOUT 242.3111083791625 FPS :D:D:D ##


import random

import pygame

from indigo.collide import *
from indigo.colors import *


def close(a, b):
    exit()


def add_passed(passed, new):
    for obj in new:
        if not new in passed:
            passed.append(new)
    return passed


class Bird(Player):
    def flap(self):
        self.move_smoothly("y", -50, 50)
        self.img = Image("test_3_assets\\bird1.png")
        self.img.rotate(25)
        self.img = self.img.get_img()
        return

    def fall(self):
        if not self.smooth_y:
            self.img = Image("test_3_assets\\bird1.png")
            self.img.rotate(-25)
            self.img = self.img.get_img()
            self.move_smoothly("y", 0.5, 1)
        return

    pass


class Pipe(Placeholder):
    def __init__(self, scr, img, x=None, y=None):
        super().__init__(scr, img, x, y)
        self.set_rect()
        return

    def blit(self):
        super().blit()
        self.x -= 0.1

    def clone(self, x, y):
        return Pipe(self.scr, self.img, x, y)


class Base(Engine_Object):
    def __init__(self, scr, x):
        self.img = "test_3_assets\\base.png"
        self.scr = scr
        self.x = x
        self.y = 400
        super().__init__()
        self.set_rect()
        return

    def blit(self):
        self.scr.blit(self.img, self.x, self.y)
        self.x -= 1
        return


if __name__ == "__main__":
    # print(1 / 0.004126925945281982)
    # exit()
    scr = Screen(700, 700, BLACK, "FLAPPY BIRD")
    scr.resize_for_bg(Image("test_3_assets\\bg.png").get_img())
    bases = Group()
    bases.append(Base(scr, 0))
    bird = Bird(scr, "test_3_assets\\bird1.png", 50, 200)
    bird.set_rect()
    pipes = Group()
    pipe_image_down = Image("test_3_assets\\pipe.png").get_img()
    pipe_image_up = Image("test_3_assets\\pipe.png")
    pipe_image_up.rotate(180)
    pipe_up = Pipe(scr, pipe_image_up.get_img())
    pipe_down = Pipe(scr, pipe_image_down)
    upper_pipes = Group()
    lower_pipes = Group()
    test = Test_Counter()
    passed = []
    score = 0
    for i in range(5000):
        print(i)
        test.start()
        bases.eliminate(lambda obj: obj.x + obj.w <= 0)
        lower_pipes.eliminate(lambda obj: obj.x + obj.w <= 0)
        upper_pipes.eliminate(lambda obj: obj.x + obj.w <= 0)
        if len(bases) < 2:
            bases.append(Base(scr, 336))
        assert len(lower_pipes) == len(upper_pipes)
        if len(lower_pipes) < 1:
            lower_pipes.append(pipe_down.deploy(300, random.uniform(250, 400)))
        if len(upper_pipes) < 1:
            upper_pipes.append(pipe_up.deploy(300, random.uniform(-200, -150)))
        if upper_pipes[-1].x <= 200:
            lower_pipes.append(pipe_down.deploy(300, random.uniform(250, 300)))
            upper_pipes.append(pipe_up.deploy(300, random.uniform(-200, -150)))
        scr.set_bg_img(Image("test_3_assets\\bg.png").get_img())
        bird.blit()
        lower_pipes.blit()
        upper_pipes.blit()
        bases.blit()
        Label(scr, str(score), 20, 20, 50, WHITE).blit()
        for event in pygame.event.get():
            scr.quit_handler(event)
            if event.type == pygame.locals.KEYDOWN:
                if event.unicode == " ":
                    bird.flap()
        bird.fall()
        sprite_group_collision(bird, bases, close)
        sprite_group_collision(bird, upper_pipes, close)
        sprite_group_collision(bird, lower_pipes, close)
        score = (len(passed) + 1) // 2
        passed = add_passed(passed, upper_pipes.fit(lambda obj: obj.x <= bird.x))
        pygame.display.update()
        test.lap()
    print(test)
