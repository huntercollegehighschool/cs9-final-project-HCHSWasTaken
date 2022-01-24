from typing import List
import curses

import hangman
from util import xindex, get_word
from constants import (
  STATUS_LINE, BAD_LINE, GUESS_LINE, CURRENT_LINE, INPUT_LINE,
  PROMPT, HANG_Y, HANG_X
)

def gamelogic(stdscr: curses.window, h: hangman, words: List[str]) -> bool:
  """Play one game, return True to keep playing """
  def winlose(msg: str) -> bool:
    """Handle winning and losing"""
    h.addstr(CURRENT_LINE, 1, f"The word is {word}")
    h.addstr(INPUT_LINE, 1, msg)
    h.addstr(STATUS_LINE, 1, "")
    h.addstr(GUESS_LINE, 1, "")
    while True:
      curse_state = h.get_low_letter(BAD_LINE, 1, "Enter 'q' to quit or 'a' to play again.")
      if curse_state == 'a':
          return True
      if curse_state == 'q':
          return False

  stdscr.clear()
  word = get_word(words, 5)
  total_guess = "_" * len(word)
  bad_guess = ""
  h.hang(HANG_Y, HANG_X)
  while True:
    h.addstr(CURRENT_LINE, 1, f"Your current guess is {total_guess}")
    h.addstr(GUESS_LINE, 1, f"You have {7-len(bad_guess)} guesses left.")
    h.addstr(BAD_LINE, 1, f"Bad guesses made: {bad_guess}")
    
    letter_guess = h.get_low_letter(INPUT_LINE, 1, PROMPT).lower()
    h.addstr(STATUS_LINE, 1, "")
    
    if xindex(bad_guess, letter_guess) != -1 or xindex(total_guess, letter_guess) != -1:
      h.addstr(STATUS_LINE, 1, f"You've already guessed {letter_guess}.")
      continue

    position = xindex(word, letter_guess)
    if position == -1:
      h.addstr(STATUS_LINE, 1, f"Letter {letter_guess} not in word")
      bad_guess += letter_guess
      h.draw(HANG_Y, HANG_X, len(bad_guess))
      if len(bad_guess) >= 7:
        return winlose("You lost; you ran out of guesses.")
      continue
    
    while position != -1:
      total_guess = total_guess[:position] + letter_guess + total_guess[position + 1:]
      position = xindex(word, letter_guess, position + 1)

    if total_guess == word:
      return winlose(f"You won with {6 - len(bad_guess)} guesses left!")
     
    h.addstr(CURRENT_LINE, 1, f"Your current guess is {total_guess}")

stdscr = curses.initscr()

with open("words", "r") as file:
  words = file.read().split('\n')

h = hangman.hangman(stdscr)

while gamelogic(stdscr, h, words):
  continue

curses.endwin()
print("Thanks for playing!\nMade by Stamos Z., Big thanks to Mr. Cheng.\n")