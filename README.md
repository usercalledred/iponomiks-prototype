# IPONOMIKS

**IPONOMIKS** is a simple student budget and expense tracker built in Python.
The name combines *"ipon"* (Filipino for savings) and *"economics"* reflecting
the app's goal of helping students manage their money.

This repository currently contains the **initial console-based prototype**.
It demonstrates the core idea of the system before the full graphical
version is built out.

---

## Purpose

Students often struggle to keep track of where their allowance or budget
goes. IPONOMIKS lets a user (students) set a monthly budget, log expenses by category,
and immediately see how much of their budget remains helping them spot
overspending before it happens.

---

## Features (Prototype)

- Set a monthly budget with input validation
- Add expenses under predefined categories (Food, Transportation, Bills,
  School Supplies, Others)
- View a running list of all logged expenses
- View a budget summary showing:
  - Total budget
  - Total spent
  - Remaining balance
  - Percentage of budget used
  - Status: **On Track**, **Nearly Over Budget**, or **Over Budget**
- Input validation throughout (rejects invalid numbers, empty amounts,
  out-of-range menu choices, etc.)

---

## How to Run

**Requirements:** Python 3 (no external libraries needed)

```bash
python iponomiks.py
```

Follow the on-screen menu:
```
1. Add an Expense
2. View All Expenses
3. View Budget Summary
4. Exit
```

---

## Project Status

This is an **early prototype** built to demonstrate the core logic (budget
tracking, expense logging, input validation) using plain Python —
variables, loops, conditionals, and basic validation only.

Planned for later versions:
- Graphical user interface (GUI)
- Persistent data storage (SQLite database)
- Multiple saved trackers per user
- Object-oriented structure

A more advanced GUI build (Tkinter-based, with themed visuals and a
database backend) is in progress separately as the project evolves toward
its final version.

---

## File Structure

```
iponomiks/
├── iponomiks.py     # Console prototype (this version)
└── README.md        # Project documentation
```

---

## Author

Developed as a initial working prototype project.
