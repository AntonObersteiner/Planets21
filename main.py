#!/usr/bin/env python3
from Vector import Vector
from Planet import Planet
from random import random
from time import sleep
import turtle as T
def T_setup():
    T.speed(0)
    T.delay(0)
    T.tracer(0, 0)
    T.ht()

def main(iterations = 100):
    T_setup()
    planets = [
        Planet.random()
        for _ in range(50)
    ]

    #custom sum: momenta of all planets
    sum_momentum = sum([
        planet.vel * planet.mass
        for planet in planets
    ], start = Vector(0, 0))

    #calculating the average momentum per planet and subtracting it ==> galaxy stays in the center
    each_momentum = sum_momentum / len(planets)
    print(f"Ʃp = {sum_momentum}, ¯p = {each_momentum}")
    for planet in planets:
        planet.vel -= each_momentum / planet.mass

    for _ in range(iterations):
        #gravitational acceleration
        for p in range(len(planets)):
            for q in range(p):
                planets[p].accelerate(planets[q])
                planets[q].accelerate(planets[p])

        #combine close planets and remove mass-0 planets
        p = 0
        while p < len(planets):
            for q in range(p - 1, -1, -1):
                planets[q].check_combine(planets[p])
                #check removal
                if planets[p].mass == 0:
                    planets.pop(p)
                    if (p == len(planets)):
                        break
            p += 1

        #draw planets
        for p in range(len(planets)):
            planets[p].update()
            planets[p].draw(T)

        #tell the turtle to update the canvas
        T.update()
        # sleep(.1)

    #so we can look at the final state
    input("[ENTER] to quit")

if __name__ == '__main__':
    #reading the number of iteration from the command line input
    from sys import argv
    iterations = 100
    if len(argv) > 1:
        try:
            iterations = int(argv[1])
        except ValueError:
            print(f"Argument 1: expected number of iterations, found '{argv[1]}'")
    main(iterations)
