# import the pygame module, so you can use it
import pygame
from . import artist
from . import world
from . import inputmanager
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()

    #Initialize screen
    artist.init_screen()

    #Initialize world
    player_obj = world.add_test_object()

    #Get input handler ready
    inputmanager.init_input()

    #Start drawing
    artist.draw_update()

    # define a variable to control the main loop
    running = True


    xpos = 10
    ypos = 10
    xstep = 1
    ystep = 1
     
    # main loop
    timer = 0
    timecap = 1
    timeadd = 0.005
    moving_left = True
    while running:
        #Call inputmanager's thing every frame. It returns false if we quit, so
        running = inputmanager.check_input()
        artist.draw_update()
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()