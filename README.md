# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Game Purpose**

This is a number guessing game built with Streamlit. The player selects a difficulty (Easy, Normal, or Hard), and the game generates a secret number within a range for that difficulty. The player has a limited number of attempts to guess the secret number, receiving hints after each guess to guide them higher or lower.

**Bugs Found**

- The hint direction was inverted — "Go Higher" showed when the guess was too high, and vice versa.
- The secret number regenerated on every Streamlit rerun (every button click), making it impossible to win since the target kept changing.
- The difficulty ranges were wrong: Normal (1–100) was harder than Hard (1–50), and Easy had the same range as Hard.
- The attempt counter was off by one — the sidebar showed 8 attempts but the game ended after 7.
- The game info always displayed "1 to 100" regardless of selected difficulty.
- The "New Game" button didn't work after winning — a page refresh was required to play again.
- The first guess was not displayed in the history until the second guess was submitted, causing the history to always appear one step behind.
- Empty strings and non-numeric inputs were accepted, and could be spammed to grow the guess history indefinitely.

**Fixes Applied**

- Corrected the hint logic in `check_guess()` in [logic_utils.py](logic_utils.py) — "Too High" now says "Go LOWER!" and "Too Low" now says "Go HIGHER!".
- Fixed the secret number state by storing it in `st.session_state` so it persists across reruns instead of regenerating each time.
- Fixed the difficulty ranges in `get_range_for_difficulty()`: Easy is 1–20, Normal is 1–50, Hard is 1–100.
- Fixed the attempt counter by reordering code blocks to respect Streamlit's top-to-bottom render order — the debug expander was moved below the attempt-update logic so the counter reflects the correct value.
- Updated the game info display to read the actual range from session state rather than hardcoding "1 to 100".
- Fixed the "New Game" button by resetting the relevant session state keys on click.
- Fixed input validation in `parse_guess()` to reject empty strings and non-numeric values before they are processed.

## 📸 Demo

![Picture of PyTest validating 19 checks][https://imgur.com/a/RP9UDdA]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
