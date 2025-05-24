from PIL import Image
from lookuptable import SetcolourGraphicsDrawing

def GetrownumbersSpritedrawer(FilepathSpritedrawer):
    #opens up the file and reads the lines
    with open(FilepathSpritedrawer, 'r') as file:
        RowsSprite = file.readlines()
        #removes white space, splits the lines by commas. It does this for each line in the file.
        row_numbers = [line.strip().split(",") for line in RowsSprite]
        print(row_numbers)
        return row_numbers

def SizefinderSpritedrawer(FilepathSpritedrawer):
    #opens up the file and reads the lines
    row_numbers = GetrownumbersSpritedrawer(FilepathSpritedrawer)
    #finds the length of the longest line
    LengthSprite = max(len(line) for line in row_numbers)
    WidthSprite = len(row_numbers)

    #returns the length and width
    print(LengthSprite, WidthSprite)
    return LengthSprite, WidthSprite
    
def DrawConsole(FilepathGraphics):
    LengthSprite, WidthSprite = SizefinderSpritedrawer(FilepathGraphics)
    img = Image.new("RGB", (LengthSprite, WidthSprite), "white")
    RownumbersSize = GetrownumbersSpritedrawer(FilepathGraphics)
    RownumberDrawer = 0
    for item in RownumbersSize:
        print(item)
        CurrentrowtoDraw = item
        PixelnumberDrawer = 0
        for i in CurrentrowtoDraw:
            print(i)
            PixelcolourDrawer = SetcolourGraphicsDrawing(i)
            print(PixelcolourDrawer)
            PixelcolourDrawer = int(PixelcolourDrawer)
            # Set the pixel color in the image
            img.putpixel((PixelnumberDrawer, RownumberDrawer), PixelcolourDrawer)
            PixelnumberDrawer += 1
        RownumberDrawer += 1

DrawConsole("videochip/test.txt")
SizefinderSpritedrawer("videochip/test.txt")
