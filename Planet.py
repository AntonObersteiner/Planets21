#!/usr/bin/env python3
from random import random
from math import log
from Vector import Vector

class Planet(Vector):
    """
    has a mass and coordinates and velocity in (x, y)
    can move, be accelerated and combined and
        draw its path
    """

    def __init__(self, mass, pos, vel = Vector(0, 0)):
        super(Planet, self).__init__(pos.x, pos.y)
        self.mass = mass
        self.vel = vel.copy()
        self.acc = Vector(0, 0)
        self.trace = []

    def __repr__(self):
        return "P[{self.mass:.0f}]@({self.x:.0f}, {self.y:.0f})" % (self.mass, self.x, self.y)

    def random(mass = 5, pos = Vector(400, 400), vel = Vector(10, 10)):
        return Planet(
            mass * random(),
            Vector.random(pos) * 2 - pos,
            Vector.random(vel) * 2 - vel
        )

    def update(self, dt = .1):
        self.vel += self.acc * dt
        self     += self.vel * dt
        self.acc = Vector(0, 0)

        if abs(self) > 2000:
            pass
            # self.mass = 0
            # self.pos = [random() * 200 - 100, random() * 200 - 100]
        else:
            self.trace += [self.copy()]

    def accelerate(self, other, g = -100):
        diff = self - other
        dist = abs(diff)
        if dist > 0:
            factor = other.mass / dist ** 2 * g  #*mass
            self.acc += diff * factor            #/mass

    def check_combine(self, other, threshhold = 1):
        diff = self - other
        dist = abs(diff)
        if dist == 0:
            self.combine(other)
            return True
        factor = self.mass * other.mass / dist ** 2
        if factor > threshhold:
            self.combine(other)
            return True
        else:
            return False

    def combine(self, other):
        other_proportion = other.mass / (self.mass + other.mass)

        #Vector-combine this and the other vector
        # super(Planet, self).combine(other, other_proportion)
        self.vel.combine(other.vel, other_proportion)

        self.mass += other.mass
        other.mass = 0

    def draw(self, T):
        if len(self.trace) < 2:
            return
        T.pensize(log(2.8 * max(1, self.mass)))
        T.pu(); T.goto(self.trace[-2] * .5)
        T.pd(); T.goto(self * .5)

    def draw_trace(self, T):
        if len(self.trace) < 2:
            return

        T.pensize(log(2.8 * max(1, self.mass)))
        T.pu(); T.goto(self.trace[0] * .5)
        T.pd(); T.goto(self.trace[1] * .5)
        for tr in self.trace:
            T.goto(tr)
