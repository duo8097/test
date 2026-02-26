"""Entry point for the pygame-ce Dodge the Magma game."""

from __future__ import annotations

import pygame

from . import config
from .game import run_round, wait_for_restart


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    pygame.display.set_caption("Dodge the Magma with Shield! (pygame-ce)")
    clock = pygame.time.Clock()

    try:
        while True:
            score = run_round(screen, clock)
            if not wait_for_restart(screen, score):
                break
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
