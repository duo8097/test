#include <SFML/Graphics.hpp>
#include "Game.hpp"
#include <iostream>
#include <vector>

int main() {
    sf::RenderWindow window(sf::VideoMode(1000, 600), "Dodge the Magma with Shield!");

    // Load font
    sf::Font font;
    if (!font.loadFromFile("assets/arial.ttf")) {
        std::cerr << "⚠️ Warning: Font not found. Score text won't display.\n";
    }

    while (window.isOpen()) {
        Game game(window, font);
        int score = game.run();

        // Game Over Screen
        window.clear(sf::Color::Black);

        if (font.getInfo().family != "") {
            sf::Text over("Game Over! Score: " + std::to_string(score), font, 64);
            over.setFillColor(sf::Color::White);
            over.setPosition(200, 200);
            window.draw(over);

            sf::Text hint("Press R to Restart or C to Quit", font, 36);
            hint.setFillColor(sf::Color::White);
            hint.setPosition(200, 300);
            window.draw(hint);
        }

        window.display();

        bool waiting = true;
        while (waiting && window.isOpen()) {
            sf::Event e;
            while (window.pollEvent(e)) {
                if (e.type == sf::Event::Closed) { window.close(); waiting = false; }
                if (e.type == sf::Event::KeyPressed) {
                    if (e.key.code == sf::Keyboard::R) waiting = false;
                    if (e.key.code == sf::Keyboard::C) { window.close(); waiting = false; }
                }
            }
            sf::sleep(sf::milliseconds(50));
        }
    }
}
