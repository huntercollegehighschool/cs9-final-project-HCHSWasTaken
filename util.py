from typing import List
import random

def xindex(s: str, c: str, start: int=0) -> int:
  """Return the position of c in s starting 
  at position start or -1 if not found"""
  s = s[start:]
  return s.index(c) + start if c in s else -1

def get_word(words: List[str], l: int) -> str:
  """return a random word from the list of words
  at least l characters long"""
  r = len(words)
  while True:
    word = words[random.randrange(0, r)]
    if len(word) >= l:
      return word