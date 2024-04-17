# Game of Life Simulator

This application is a Python-based implementation of John Conway's Game of Life, a cellular automaton devised in 1970. The Game of Life is not a typical game played by players, but rather a set of rules applied to a grid of cells.

The game simulates the birth and death of cells based on initial states and the rules applied to subsequent generations. In this simulation, you can explore different logic gates visualized through the Game of Life mechanics. The application uses Pygame for rendering the game state, allowing for real-time interaction and visualization.

![Menu](/assets/menu.png)

## Features

+ ***Multiple Menus***: Navigate through different logic gates and informational menus using keyboard inputs.
+ ***Dynamic Updates***: Watch the cells evolve in real time as the game applies the rules of the Game of Life.
+ ***Logic Gate Simulation***: Experiment with NOT, AND, and OR gates visualized through cellular automata.
+ ***Interactive Controls***: Use keyboard inputs to manipulate the simulation and navigate through different functionalities.

## Game Rules

1. **Survival**: A cell survives to the next generation if it has two or three live neighbors.
2. **Birth**: A dead cell becomes alive in the next generation if it has exactly three live neighbors.
3. **Death**: A cell dies due to underpopulation (fewer than two live neighbors) or overpopulation (more than three live neighbors).

## Setup and Running

To run the simulation, you need Python and Pygame installed. Follow these steps to get started:
1. Install Pygame: pip install pygame
2. Install Numpy: pip install numpy

## Controls

+ *Arrow Keys*: Navigate through the menus and select options.
+ *Enter*: Confirm selection.
+ *Backspace*: Return to the previous menu.
+ *Space*: Specific actions in different contexts (e.g., pause the simulation).

## How to Play

After starting the application, use the *arrow keys* to select different logic gates from the main menu. Press *enter* to view the simulation for the selected gate. You can experiment by changing the initial configuration of cells to see how it affects the output.

![Gate](/assets/gate.png)
