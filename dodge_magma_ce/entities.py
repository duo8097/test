"""Entity models for the Dodge the Magma game."""

from __future__ import annotations

from dataclasses import dataclass, field
import random

from . import config


@dataclass
class Player:
    x: int
    y: int
    size: int = config.PLAYER_SIZE
    speed: int = config.PLAYER_SPEED
    jump_duration: int = config.PLAYER_JUMP_DURATION
    jump_height: int = config.PLAYER_JUMP_HEIGHT

    jumping: bool = False
    jump_counter: int = 0
    shield_active: bool = True
    shield_duration: int = config.SHIELD_DURATION
    shield_cooldown: int = 0

    def move_left(self) -> None:
        self.x = max(0, self.x - self.speed)

    def move_right(self) -> None:
        self.x = min(config.WIDTH - self.size, self.x + self.speed)

    def start_jump(self) -> None:
        if not self.jumping:
            self.jumping = True
            self.jump_counter = self.jump_duration

    def update_jump(self) -> None:
        if self.jumping:
            self.y -= self.jump_height
            self.jump_counter -= 1
            if self.jump_counter <= 0:
                self.jumping = False

        if not self.jumping:
            self.y = config.HEIGHT - 2 * self.size

    def activate_shield(self) -> None:
        if self.shield_cooldown <= 0:
            self.shield_active = True
            self.shield_cooldown = config.SHIELD_COOLDOWN_FRAMES

    def update_shield(self) -> None:
        if self.shield_active:
            self.shield_duration -= 1
            if self.shield_duration <= 0:
                self.shield_active = False
                self.shield_duration = config.SHIELD_DURATION

        if self.shield_cooldown > 0:
            self.shield_cooldown -= 1

    @property
    def rect(self) -> tuple[int, int, int, int]:
        return self.x, self.y, self.size, self.size


@dataclass
class FallingBlock:
    x: int
    y: int
    size: int = config.BLOCK_SIZE
    speed: int = config.BLOCK_SPEED

    def update(self) -> bool:
        """Move block down. Returns True when it wrapped to top (score event)."""
        self.y += self.speed
        if self.y > config.HEIGHT:
            self.y = random.randint(-config.HEIGHT, 0)
            self.x = random.randint(0, config.WIDTH - self.size)
            return True
        return False

    @property
    def rect(self) -> tuple[int, int, int, int]:
        return self.x, self.y, self.size, self.size


@dataclass
class BlockField:
    blocks: list[FallingBlock] = field(default_factory=list)

    @classmethod
    def random(cls, count: int = config.NUM_BLOCKS) -> "BlockField":
        return cls(
            blocks=[
                FallingBlock(
                    x=random.randint(0, config.WIDTH - config.BLOCK_SIZE),
                    y=random.randint(-config.HEIGHT, 0),
                )
                for _ in range(count)
            ]
        )
