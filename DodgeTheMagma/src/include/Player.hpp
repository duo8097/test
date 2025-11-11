#pragma once
#include <SFML/Graphics.hpp>
#include "Block.hpp"

class Player {
public:
    Player();
    void handleInput();
    void update();
    void draw(sf::RenderWindow& window);
    bool collidesWith(const Block& b) const;
    bool isShieldActive() const;

private:
    sf::Vector2f pos;
    bool jumping;
    int jumpCounter;
    bool shieldActive;
    int shieldDuration;
    int shieldCooldown;

    static constexpr float SIZE = 50.f;
    static constexpr float SPEED = 25.f;
    static constexpr int JUMP_TIME = 10;
};
