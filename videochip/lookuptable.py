def SetcolourGraphicsDrawing(colour):
    #  later when we hit 100 colours, we will add headers, like if colour > 10, so we can look up the colour.
    rgb = None
    if colour <= 10:
        Subtractor = 10 * colour
        NewValue = 255 - Subtractor
        rgb = (NewValue, 0, 0)
        print(f"Colour set to: {rgb} for value {colour}")
    elif colour <= 20 and colour >= 10:
        Subtractor = 10 * colour
        NewValue = 255 - Subtractor
        rgb = (0, NewValue, 0)
        print(f"Colour set to: {rgb} for value {colour}")    
    elif colour <= 30 and colour >= 20 :
        Subtractor = 5 * colour
        NewValue = 255 - Subtractor
        rgb = (0, 0, NewValue)
        print(f"Colour set to: {rgb} for value {colour}")    
    elif colour <= 40 and colour >= 30 :
        Subtractor = 2 * colour
        NewValue = 128 - Subtractor
        rgb = (NewValue, 0, NewValue)
        print(f"Colour set to: {rgb} for value {colour}") 
    elif colour <= 50 and colour >= 40 :
        Subtractor = 3 * colour
        NewValueR = 255 - Subtractor
        NewValueG = 185 - Subtractor
        rgb = (NewValueR, NewValueG, 0)
        print(f"Colour set to: {rgb} for value {colour}")
    elif colour <= 60 and colour >= 50 :
        Subtractor = 3 * colour
        NewValue = 255 - Subtractor
        rgb = (NewValue,NewValue, 0)
        print(f"Colour set to: {rgb} for value {colour}") 
    elif colour <= 70 and colour >= 60 :
        Subtractor = 20 * colour
        NewValue = 255 - Subtractor
        rgb = (NewValue,NewValue, NewValue)
        print(f"Colour set to: {rgb} for value {colour}") 
    else:
        rgb = (0, 0, 0)  # Default to black or handle as needed
    print(f"Colour set to: {rgb}")
    return rgb
    

 
