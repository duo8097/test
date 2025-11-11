#include "Game.hpp"
#include <random>
#include <iostream>

const int WIDTH = 1000;
const int HEIGHT = 600;
const float BLOCK_SIZE = 50.f;
const float BLOCK_SPEED = 10.f;
const int NUM_BLOCKS = 5;

Game::Game(sf::RenderWindow& window, sf::Font& font)
    : window(window), font(font), player(), score(0), running(true)
{
    resetBlocks();
}

void Game::resetBlocks() {
    blocks.clear();
    std::mt19937 rng((unsigned)time(nullptr));
    std::uniform_int_distribution<int> distX(0, WIDTH - (int)BLOCK_SIZE);
    std::uniform_int_distribution<int> distY(-HEIGHT, 0);

    for (int i = 0; i < NUM_BLOCKS; i++) {
        blocks.push_back(Block({(float)distX(rng), (float)distY(rng)}));
    }
}

void Game::handleInput() {
    player.handleInput();
}

void Game::update() {
    player.update();

    // Move blocks
    for (auto& b : blocks) {
        b.pos.y += BLOCK_SPEED;
        if (b.pos.y > HEIGHT) {
            b.pos.y = -BLOCK_SIZE;
            b.pos.x = rand() % (WIDTH - (int)BLOCK_SIZE);
            score++;
        }
    }

    checkCollision();
}

void Game::checkCollision() {
    for (auto& b : blocks) {
        if (player.collidesWith(b)) {
            if (!player.isShieldActive()) {
                running = false;
                break;
            }
        }
    }
}

void Game::render() {
    window.clear(sf::Color::Black);

    // Score
    if (font.getInfo().family != "") {
        sf::Text scoreText("Score: " + std::to_string(score), font, 24);
        scoreText.setFillColor(sf::Color::White);
        scoreText.setPosition(10, 10);
        window.draw(scoreText);
    }

    for (auto& b : blocks) b.draw(window);
    player.draw(window);
    window.display();
}

int Game::run() {
    window.setFramerateLimit(40);
    while (running && window.isOpen()) {
        sf::Event e;
        while (window.pollEvent(e)) {
            if (e.type == sf::Event::Closed) {
                window.close();
                return score;
            }
        }

        handleInput();
        update();
        render();
    }
    return score;
}
