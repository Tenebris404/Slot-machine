# 🎰 Python Slot Machine

A simple command-line Slot Machine game built with Python. Players can deposit money, choose the number of betting lines, place bets, spin the slot machine, and win rewards based on matching symbols.

---

## 📌 Features

* 💰 Deposit virtual money
* 🎯 Choose between 1–3 betting lines
* 💵 Place a custom bet per line
* 🎲 Randomly generated slot machine reels
* 🏆 Automatic win detection and payout calculation
* 📊 Displays the remaining balance after each game
* ✅ Input validation to prevent invalid entries

---

## 🛠️ Technologies Used

* Python 3
* Built-in `random` module

---

## 📂 Project Structure

```
Slot-Machine/
│
├── slot_machine.py
└── README.md
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Slot-Machine.git
```

### 2. Navigate to the project folder

```bash
cd Slot-Machine
```

### 3. Run the program

```bash
python slot_machine.py
```

---

## 🎮 How to Play

1. Enter the amount you want to deposit.
2. Select the number of betting lines (1–3).
3. Enter your bet amount for each line.
4. The slot machine spins randomly.
5. If all symbols on a selected row match, you win!
6. Your winnings are added back to your balance.

---

## 💎 Symbol Values

| Symbol | Payout Multiplier |
| ------ | ----------------: |
| A      |            8× Bet |
| B      |            6× Bet |
| C      |            4× Bet |
| D      |            2× Bet |

---

## 📷 Sample Output

```text
Enter deposit amount: $100
Enter number of lines (1-3): 2
Enter bet per line ($1-$100): 10

Spinning...

A | B | A
B | B | B
C | D | C

Line 2 won! (+$60)

You won: $60
Remaining Balance: $140
```

---

## 🌱 Future Improvements

* Play Again option
* Jackpot feature
* Bonus rounds
* Save player balance
* Leaderboard
* Colorful terminal output
* Graphical User Interface (GUI) using Tkinter or Pygame

---

## 📚 What I Learned

This project helped me practice:

* Functions
* Loops
* Dictionaries
* Lists
* Input validation
* Random number generation
* Game logic
* Clean code organization

---

## 👨‍💻 Author

**Kanishk Chauhan**

Computer Science (Cyber Security) Student

Interested in Python, Cybersecurity, and Software Development.

---

## ⭐ Support

If you found this project helpful or interesting, consider giving the repository a ⭐ on GitHub.
