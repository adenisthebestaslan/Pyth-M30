# Make sure spritedrawer.py and spriteediting.py are in the same directory as this file, or adjust the import paths accordingly.
import spritedrawer
import spriteediting


def SpriteimporterConsole(size, stretch,name):
  print("Importing sprite...")
  spriteediting.size(name, size)
  spriteediting.StrechSprite(name, stretch)
  spritedrawer.DrawConsole(name)

SpriteimporterConsole(0,0,"C:\\Users\\adena\\OneDrive\\Desktop\\Pyth-M20\\videochip\\test.txt")