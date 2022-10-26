import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
import hashlib, uuid

string=''
hashed_password=''
current_string_p=[]
display_p=[]
symbol='*'

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, consts.COLOR_BLACK,
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)
  pygame.draw.rect(screen, consts.COLOR_WHITE,
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)

  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, consts.COLOR_WHITE),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def ask(screen, question):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string_un = []
  display_box(screen, question + ": " + string.join(current_string_un))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string_un = current_string_un[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_LSHIFT or inkey == K_RSHIFT:
      inkey=get_key()
      if inkey <= 127:
        upper_case=inkey-32
        current_string_un.append(chr(upper_case))
    elif inkey <= 127:
      current_string_un.append(chr(inkey))
    display_box(screen, question + ": " + string.join(current_string_un))
  return string.join(current_string_un)
#password
  global display_p
  global current_string_p
  current_string_p = []
  display_p=[]
  pro=''.join(display_p)
  display_box(screen, question + ": " + pro)
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string_p = current_string_p[0:-1]
      display_p = display_p[0:-1]
    elif inkey == K_RETURN:
##      print(display_p))
      break
    elif inkey == K_LSHIFT or inkey == K_RSHIFT:
      inkey=get_key()
      if inkey <= 127:
        upper_case=inkey-32
        for character in current_string_p:
          display_p.append(symbol)
        pro=''.join(display_p)
        display_box.blit(screen, question + ": " + pro)
        current_string_p.append(chr(upper_case))
    elif inkey <= 127:
      for character in current_string_p:
        display_p.append(symbol)
      pro=''.join(display_p)
      display_box.blit(screen, question + ": " + pro)
      current_string_p.append(chr(inkey))


##  return string.join(display_p)
  return display_p
##  return string.join(current_string_p)


def main():
  global display_p
  display_p=[]
  screen = pygame.display.set_mode((320,240))
  print (ask(screen, "Username") + " was entered")
  x = ask(screen, "Password")
  for character in x:
    display_p.append(symbol)
  pro=''.join(display_p)
  print (x + " was entered")
  print(pro)
  #check password security
  #hash password
  salt = "5gz"
  hashing_password = x+salt
  h = hashlib.md5(hashing_password.encode())



if __name__ == '__main__':
      main()
