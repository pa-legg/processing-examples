import random

window_width = 800
window_height = 600

def random_number(max):
  return random.random() * max

def setup():
  size(window_width, window_height)
  
def draw():
  x = random_number(window_width)
  y = random_number(window_height)
  box_width = random_number(200)
  box_height = random_number(200)
  colour = [random_number(255), random_number(255), random_number(255)]
  fill(colour[0], colour[1], colour[2])
  rect(x, y, box_width, box_height)
