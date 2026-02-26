"""Core game loop logic for Dodge the Magma."""

from __future__ import annotations

import pygame

from . import config
from .entities import Player, BlockField
from .ui import draw_game, draw_game_over


def intersects(a: tuple[int, int, int, int], b: tuple[int, int, int, int]) -> bool:
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    return ax < bx + bw and ax + aw > bx and ay < by + bh and ay + ah > by


def run_round(screen: pygame.Surface, clock: pygame.time.Clock) -> int:
    player = Player(config.WIDTH // 2, config.HEIGHT - 2 * config.PLAYER_SIZE)
    blocks = BlockField.random()
    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.move_left()
        if keys[pygame.K_d]:
            player.move_right()
        if keys[pygame.K_SPACE]:
            player.start_jump()
        if keys[pygame.K_e]:
            player.activate_shield()

        player.update_jump()
        player.update_shield()

        for block in blocks.blocks:
            if block.update():
                score += 1

            if intersects(player.rect, block.rect) and not player.shield_active:
                running = False
                break

        draw_game(screen, player, blocks, score)
        pygame.display.flip()
        clock.tick(config.FPS)

    return score


def wait_for_restart(screen: pygame.Surface, score: int) -> bool:
    draw_game_over(screen, score)
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                if event.key == pygame.K_c:
                    return False
    return False
