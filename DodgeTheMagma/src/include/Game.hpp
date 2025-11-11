#pragma once
#include <SFML/Graphics.hpp>
#include <vector>
#include "Player.hpp"
#include "Block.hpp"

class Game {
public:
    Game(sf::RenderWindow& window, sf::Font& font);
    int run();

private:
    void handleInput();
    void update();
    void render();
    void resetBlocks();
    void checkCollision();

    sf::RenderWindow& window;
    sf::Font& font;
    Player player;
    std::vector<Block> blocks;
    int score;
    bool running;
};
