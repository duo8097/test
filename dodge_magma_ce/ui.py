"""Drawing and UI helpers for the Dodge the Magma game."""

from __future__ import annotations

import pygame

from . import config
from .entities import Player, BlockField


def draw_game(screen: pygame.Surface, player: Player, blocks: BlockField, score: int) -> None:
    screen.fill(config.BLACK)

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, config.WHITE)
    screen.blit(score_text, (10, 10))

    for block in blocks.blocks:
        pygame.draw.rect(screen, config.RED, block.rect)

    player_color = config.GREEN if player.shield_active else config.BLUE
    pygame.draw.rect(screen, player_color, player.rect)

    if player.shield_active:
        center = (player.x + player.size // 2, player.y + player.size // 2)
        pygame.draw.circle(screen, config.CYAN, center, player.size + 10, 5)


def draw_game_over(screen: pygame.Surface, score: int) -> None:
    screen.fill(config.BLACK)

    title_font = pygame.font.Font(None, 74)
    title = title_font.render(f"Game Over! Score: {score}", True, config.WHITE)
    screen.blit(title, (config.WIDTH // 2 - title.get_width() // 2, config.HEIGHT // 3))

    prompt_font = pygame.font.Font(None, 50)
    prompt = prompt_font.render("Press R to Restart or C to Quit", True, config.WHITE)
    screen.blit(prompt, (config.WIDTH // 2 - prompt.get_width() // 2, config.HEIGHT // 2))

    pygame.display.flip()
