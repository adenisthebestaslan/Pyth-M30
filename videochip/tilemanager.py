import pygame
import sys

# Initialize Pygame
pygame.init()
screen = 0
# Set up display
def setup(name):
    global screen
    screen = pygame.display.set_mode((400, 300))  # width x height
    pygame.display.set_caption(f"{name}:made with the PYTH-M20.")
def singledraw(x,y,image,name):
    global screen
    setup(name)
    
# Load image
    imagefielTielset = pygame.image.load(image)  # Replace with your image file
    print("Haiii")
    running = True
    while running:
        
        screen.fill((255, 255, 255))
    # Draw image at position (x, y)
        screen.blit(imagefielTielset, (x, y))
        pygame.display.flip()
    # Update display
        pygame.display.flip()
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                running = False
                print(event.type)
            else:
                pass
    print("bai")
    # Fill screen with white (optional)

# singledraw(1,1,r"C:\Users\adena\OneDrive\Desktop\Pyth-M20\output_sprite.png", "pacman")


def tilefill(image, name):
    global screen
    setup(name)
    imagetoload = pygame.image.load(image)
    running = True
    while running:
        #while the program is runing
        screen.fill((255, 255, 255))
        # fills the screen whit white
        for i in range(0, 400, imagetoload.get_width()): #for i in range 400  
            for j in range(0, 300, imagetoload.get_height()):  # for j in rang 300
                screen.blit(imagetoload, (i, j))
                #draw a image at positon i,j
        pygame.display.flip()
        for event in pygame.event.get():
            #meanwhile, for every user input
            if event.type == pygame.QUIT:
                #if we quit the game
                running = False
                #stop running the program


tilefill(r"C:\Users\adena\OneDrive\Desktop\Pyth-M20\output_sprite.png", "pacman")
