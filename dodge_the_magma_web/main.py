import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1000, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Magma with Shield!")

# Clock for controlling frame rate
clock = pygame.time.Clock()

def game_loop():
    # Player properties
    player_size = 50
    player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
    player_speed = 25
    player_jump = False
    player_jump_duration = 10
    jump_counter = 0
    shield_active = True
    shield_duration = 100
    shield_cooldown = 0

    # Block properties
    block_size = 50
    block_speed = 10
    num_blocks = 5
    blocks = [
        [random.randint(0, WIDTH - block_size), random.randint(-HEIGHT, 0)]
        for _ in range(num_blocks)
    ]

    # Score
    score = 0

    # Game loop
    running = True
    while running:
        screen.fill(BLACK)
        # Display score in real-time
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player_pos[0] > 0:  # Move left
            player_pos[0] -= player_speed
        if keys[pygame.K_d] and player_pos[0] < WIDTH - player_size:  # Move right
            player_pos[0] += player_speed

        # Jump ability
        if keys[pygame.K_SPACE] and not player_jump:  # Jump
            player_jump = True
            jump_counter = player_jump_duration

        if player_jump:
            player_pos[1] -= 20  # Jump up
            jump_counter -= 1
            if jump_counter <= 0:
                player_jump = False

        # Gravity effect
        if not player_jump:
            player_pos[1] = HEIGHT - 2 * player_size

        # Shield ability
        if keys[pygame.K_e] and shield_cooldown <= 0:  # Activate shield
            shield_active = True
            shield_cooldown = 200  # Cooldown for shield activation

        if shield_active:
            shield_duration -= 1
            if shield_duration <= 0:
                shield_active = False
                shield_duration = 100

        if shield_cooldown > 0:
            shield_cooldown -= 1

        # Update block positions
        for block in blocks:
            block[1] += block_speed
            if block[1] > HEIGHT:
                block[1] = random.randint(-HEIGHT, 0)
                block[0] = random.randint(0, WIDTH - block_size)
                score += 1

            # Check collision
            if (
                block[1] + block_size > player_pos[1]
                and block[1] < player_pos[1] + player_size
                and block[0] + block_size > player_pos[0]
                and block[0] < player_pos[0] + player_size
            ):
                if not shield_active:
                    print(f"Game Over! Your Score: {score}")
                    running = False

            # Draw block
            pygame.draw.rect(screen, RED, (*block, block_size, block_size))

        # Draw player
        player_color = GREEN if shield_active else BLUE
        pygame.draw.rect(screen, player_color, (*player_pos, player_size, player_size))

        # Draw shield aura
        if shield_active:
            pygame.draw.circle(
                screen,
                CYAN,
                (player_pos[0] + player_size // 2, player_pos[1] + player_size // 2),
                player_size + 10,
                5,  # Thickness of the aura
            )

        # Update screen
        pygame.display.flip()

        # Frame rate
        clock.tick(40)

    return score

def main():
    while True:
        score = game_loop()
        # Game Over screen
        screen.fill(BLACK)
        font = pygame.font.Font(None, 74)
        text = font.render(f"Game Over! Score: {score}", True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 3))

        play_again_text = pygame.font.Font(None, 50).render(
            "Press R to Restart or C to Quit", True, WHITE
        )
        screen.blit(play_again_text, (WIDTH // 2 - play_again_text.get_width() // 2, HEIGHT // 2))

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Restart game
                        waiting = False
                    if event.key == pygame.K_c:  # Quit game
                        pygame.quit()
                        sys.exit()

if __name__ == "__main__":
    main()
