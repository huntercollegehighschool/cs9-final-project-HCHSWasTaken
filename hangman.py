"""
Drawing stuff for hangman
"""
import curses

class hangman:
  def __init__(self, stdscr: curses.window) -> None:
    self.stdscr = stdscr
    
  def head(self, y: int, x: int, c: str) -> None:
    """Draw head at y, x using c as eyes"""
    self.stdscr.addstr(y + 0, x, " ___ ")
    self.stdscr.addstr(y + 1, x, f"/{c} {c}\\")
    self.stdscr.addstr(y + 2, x, "| U |")
    self.stdscr.addstr(y + 3, x, "\___/")

  def body(self, y: int, x: int) -> None:
    """Draw body at y, x"""
    self.stdscr.addstr(y + 0, x, "|")
    self.stdscr.addstr(y + 1, x, "|")
    self.stdscr.addstr(y + 2, x, "|")

  def left_limb(self, y:int, x: int) -> None:
    """Draw left limb at y, x"""
    self.stdscr.addstr(y + 0, x, "/")
    self.stdscr.addstr(y + 1, x - 1, "/")

  def right_limb(self, y:int, x: int) -> None:
    """Draw right limb at y, x"""
    self.stdscr.addstr(y + 0, x, "\\")
    self.stdscr.addstr(y + 1, x + 1, "\\")

  def hang(self, y: int, x: int) -> None:
    """Draws hanger at y, x"""
    for i in range(13):
      self.stdscr.addstr(y, x + i, '_')
    for i in range(10):
      self.stdscr.addstr(y + 1 + i, x, '|')
    self.stdscr.addstr(y + 1, x + 12, "|")
    self.stdscr.addstr(y + 1, x + 1, '/')

  def draw(self, y: int, x : int, guesses: int) -> None:
    """Draws hangman at y, x"""
  
    if guesses == 0:
      return
    self.head(y + 2, x + 10, ".")
    if guesses == 1:
      return
    self.body(y + 6, x + 12)
    if guesses == 2:
      return
    self.right_limb(y + 7, x + 13)
    if guesses == 3:
      return
    self.left_limb(y + 7, x + 11)
    if guesses == 4:
      return
    self.right_limb(y + 9, x + 13)
    if guesses == 5:
      return
    self.left_limb(y + 9, x + 11)
    if guesses == 6:
      return
    self.head(y + 2, x + 10, "X")

  def getch(self) -> str:
    """get a single character from curses"""
    return str(chr(self.stdscr.getch())).strip()

  def addstr(self, y: int, x: int, s: str) -> None:
    """Add str at y, x clearing the line first"""
    self.stdscr.move(y, x)
    self.stdscr.clrtoeol()
    self.stdscr.addstr(y, x, s)

  def prompt(self, y: int, x: int, p: str) -> str:
      """prompt the user with p at y, x and return a character"""
      self.addstr(y, x, p)
      self.stdscr.move(y, x + len(p))
      return self.getch()

  def get_low_letter(self, y: int, x: int, p: str) -> str:
    """Prompt the user with p at y, x and keep at it until they type a low case letter"""
    while True:
      letter_guess = self.prompt(y, x, p).lower()
      if letter_guess.islower():
        return letter_guess
      
