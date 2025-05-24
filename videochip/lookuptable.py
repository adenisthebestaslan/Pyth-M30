def SetcolourGraphicsDrawing(colour):
    #  later when we hit 100 colours, we will add headers, like if colour > 10, so we can look up the colour.
    rgb = None
    if colour == 10:
        rgb = (255, 0, 0)
    elif colour == 20:
        rgb = (0, 255, 0)
    elif colour == 30:
        rgb = (0, 0, 255)
    elif colour == 0:
        rgb = (255, 255, 255)
        print("Colour 0 is white")
    else:
        rgb = (0, 0, 0)  # Default to black or handle as needed
    print(f"Colour set to: {rgb}")
    return rgb
    

 
