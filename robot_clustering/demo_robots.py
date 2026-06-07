#!/usr/bin/env python3
"""Simplified robot random-walk demo inspired by MITx 6.00.2x pset2."""

import math
import random


class Position:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def move(self, angle_deg, speed):
        angle = math.radians(angle_deg)
        return Position(self.x + speed * math.cos(angle), self.y + speed * math.sin(angle))


def simulate(n_robots=10, steps=200, room=10.0):
    robots = [Position(random.uniform(0, room), random.uniform(0, room)) for _ in range(n_robots)]
    for _ in range(steps):
        robots = [p.move(random.uniform(0, 360), 0.5) for p in robots]
    dists = [math.hypot(p.x - room / 2, p.y - room / 2) for p in robots]
    return sum(dists) / len(dists)


if __name__ == "__main__":
    random.seed(0)
    avg = simulate()
    print("MITx 6.00.2x — Robot clustering demo")
    print(f"Mean distance to room center after random walk: {avg:.3f}")
    print("Full pset2.py included (requires ps2_verify_movement module from course).")
