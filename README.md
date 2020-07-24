# Python3 JetPack Joyride <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->
- [Running](#running)
- [Controls](#controls)
- [Requirements Implemented](#requirements-implemented)
  - [OOPS Concepts](#oops-concepts)
  - [Movement](#movement)
  - [Background](#background)
  - [Enemy](#enemy)
  - [Obstacles](#obstacles)
    - [Fire Beams](#fire-beams)
    - [Magnet](#magnet)
  - [Boss Enemy](#boss-enemy)
  - [Score and Lives](#score-and-lives)
  - [Power-Ups](#power-ups)
    - [Speed boost](#speed-boost)
    - [Shield](#shield)
  - [Bonus](#bonus)
- [Directory Structure](#directory-structure)

## Running

- Install dependencies in `requirements.txt`
- Run game using `python3 main.py`

## Controls

| Key   | Function        |
| ----- | --------------- |
| W     | Up Movement     |
| A     | Left Movement   |
| D     | Right Movement  |
| Q     | Quit game       |
| B     | Shoot Bullet    |
| Space | Activate Shield |
| H     | Speed Boost     |

## Requirements Implemented

### OOPS Concepts

- Inheritance
  - Player & Boss class inherit from Person Class
  - Vertical Firebeam,Horizontal Firebeam & Cross Firebeam class inherit from Beams
- Polymorphism
  - The method for finding dimensions of beams  
- Encapsulation
  - Class based approach to construct the game
- Abstraction
  - Methods are used for movement, shooting, shield

### Movement

- A for Left
- D for right
- W for Jetpack
- B for Bullets
- Gravity

### Background

- Obstacles change as player moves
- Screen continuously moves
- When player reaches near right end, map is shifted forward
- Player can't go left from the screen
- Player can't go above sky or below ground

### Enemy

- Enemies are flying and cannot be killed using bullets
- Once player collides with enemy, he looses a life

### Obstacles

#### Fire Beams

- Horizontal, Angled, Vertical Beams are implemented
- Beams can be removed by shooting bullets on them
- Player looses life when collided with Beam

#### Magnet

- Player is attracted towards magnet when he gets in range of magnet
- Magnet attracts using constant force

### Boss Enemy

- Follows Player allong Y axis
- When Player is in range of Height of Boss Enemy, then Dragon shoots iceballs towards player
- Boss enemy has multiple lives which will decrease when player shoots bullets towards it

### Score and Lives

- Score is increased by 30 when player collects a coin
- Player has 5 lives

### Power-Ups

#### Speed boost

- Lasts for 60s

#### Shield

- Lasts for 10s
- Passes through beams and enemies, but can still collect coins

### Bonus

- Implemented Colors

## Directory Structure


├── man.py
├── README.md
├── board.py
├── design
│   ├── boss.txt
│   ├── yoda.txt
│   ├── magnet.txt
│   └── lost.txt
├── objects.py
├── beams.py
├── main.py
└── requirements.txt