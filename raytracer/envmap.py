from raytracer.utils import Color, dword
from math import acos, atan2, pi

BLACK = Color(0, 0, 0)

class Envmap(object):
  def __init__(self, path):
    self.path = path
    self.read()

  def read(self):
    image = open(self.path, 'rb')
    image.seek(10)
    header_size = dword(image.read(4))[0]

    image.seek(14 + 4)
    self.width = dword(image.read(4))[0]
    self.height = dword(image.read(4))[0]
    image.seek(header_size)

    self.pixels = []
    for y in range(self.height):
      self.pixels.append([])
      for x in range(self.width):
        b = ord(image.read(1))
        g = ord(image.read(1))
        r = ord(image.read(1))
        self.pixels[y].append(Color(r,g,b))

    image.close()

  def get_color(self, direction):
    direction = norm(direction)
    x = int( (atan2( direction[2], direction[0]) / (2 * pi) + 0.5) * self.width)
    y = int( acos(-direction[1]) / pi * self.height )
    
    if x < self.width and y < self.height:
      return self.pixels[y][x]
    
    return BLACK