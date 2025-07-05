# 🎲 Multiplayer Dice Game (Python CLI)

A simple and fun **Multiplayer Dice Game** built using Python. Roll the dice, avoid rolling a 1, and race to 50 points to win!

---

## 📌 Features

- 🎮 2 to 4 player support
- 🎲 Realistic dice roll simulation
- 💥 Roll a `1` and lose your round’s progress
- 🏆 First to reach 50 points wins (_adjustable_)
- 📊 Live scoreboard after each round

---

## ▶️ How to Run

Make sure you have **Python 3** installed. Then run the script:

```bash
python dice_game.py
````

---

## 🎮 How to Play

1. Choose the number of players (2–4).
2. On your turn, press `y` to roll the dice.
3. You can roll multiple times per turn to accumulate points.
4. If you roll a `1`, your round ends and you lose that round’s points.
5. First player to reach **50 total points** wins. (_adjustable_)

---

## 🖥️ Sample Gameplay

```bash
Enter the number of players (2-4): 2

=== PLAYER 1 ===
Turn of player 1 to roll the dice:

Enter 'y' to roll dice: y
You rolled a  5
You score in this round is 5

Enter 'y' to roll dice: y
You rolled a  3
You score in this round is 8

Enter 'y' to roll dice: n

=== SCOREBOARD ===
Total score of player 1 is 8
Total score of player 2 is 0
```

---

## 💡 Game Logic Summary

* Rolling a number other than 1 adds to your **current round score**
* Rolling a `1` cancels your round score
* Accumulated round score is added to total only when player chooses to **stop rolling**

---

## 🛠️ Future Improvements I have in Mind

* Add win/lose messages
* Track and display round number
* Implement restart/new game feature
* Add player names

---

## 🤝 Contributing

Found a bug or want to suggest a new feature? Fork the repo and submit a pull request!

---
