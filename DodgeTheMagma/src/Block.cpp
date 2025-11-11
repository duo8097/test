#include "Block.hpp"

Block::Block(sf::Vector2f position) : pos(position) {}

void Block::draw(sf::RenderWindow& window) {
    sf::RectangleShape rect(sf::Vector2f(SIZE, SIZE));
    rect.setPosition(pos);
    rect.setFillColor(sf::Color::Red);
    window.draw(rect);
}
