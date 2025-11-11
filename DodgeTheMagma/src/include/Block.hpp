#pragma once
#include <SFML/Graphics.hpp>

class Block {
public:
    Block(sf::Vector2f position);
    void draw(sf::RenderWindow& window);
    sf::Vector2f pos;
    static constexpr float SIZE = 50.f;
};
