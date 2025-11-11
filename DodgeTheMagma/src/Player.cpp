#include "Player.hpp"

const int WIDTH = 1000;
const int HEIGHT = 600;

Player::Player()
    : pos(WIDTH / 2.f, HEIGHT - 2 * SIZE),
      jumping(false),
      jumpCounter(0),
      shieldActive(true),
      shieldDuration(100),
      shieldCooldown(0)
{}

void Player::handleInput() {
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::A) && pos.x > 0) pos.x -= SPEED;
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::D) && pos.x < WIDTH - SIZE) pos.x += SPEED;

    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Space) && !jumping) {
        jumping = true;
        jumpCounter = JUMP_TIME;
    }

    if (sf::Keyboard::isKeyPressed(sf::Keyboard::E) && shieldCooldown <= 0) {
        shieldActive = true;
        shieldCooldown = 200;
    }
}

void Player::update() {
    if (jumping) {
        pos.y -= 20.f;
        jumpCounter--;
        if (jumpCounter <= 0) jumping = false;
    } else {
        pos.y = HEIGHT - 2 * SIZE;
    }

    if (shieldActive) {
        shieldDuration--;
        if (shieldDuration <= 0) {
            shieldActive = false;
            shieldDuration = 100;
        }
    }

    if (shieldCooldown > 0) shieldCooldown--;
}

void Player::draw(sf::RenderWindow& window) {
    sf::RectangleShape rect(sf::Vector2f(SIZE, SIZE));
    rect.setPosition(pos);
    rect.setFillColor(shieldActive ? sf::Color::Green : sf::Color::Blue);
    window.draw(rect);

    if (shieldActive) {
        sf::CircleShape aura(SIZE + 10.f);
        aura.setOrigin(SIZE + 10.f, SIZE + 10.f);
        aura.setPosition(pos.x + SIZE / 2.f, pos.y + SIZE / 2.f);
        aura.setOutlineColor(sf::Color::Cyan);
        aura.setOutlineThickness(5.f);
        aura.setFillColor(sf::Color::Transparent);
        window.draw(aura);
    }
}

bool Player::collidesWith(const Block& b) const {
    return (b.pos.x < pos.x + SIZE &&
            b.pos.x + b.SIZE > pos.x &&
            b.pos.y < pos.y + SIZE &&
            b.pos.y + b.SIZE > pos.y);
}

bool Player::isShieldActive() const {
    return shieldActive;
}
